from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum
from .models import User, BodyData, Event, FoodDict, FoodRecord
from .serializers import (UserSerializer, UserCreateSerializer, BodyDataSerializer, 
                          EventSerializer, FoodDictSerializer, FoodRecordSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def update_profile(self, request, pk=None):
        user = self.get_object()
        if request.user != user:
            return Response({'error': '无权修改其他用户信息'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BodyDataViewSet(viewsets.ModelViewSet):
    queryset = BodyData.objects.all()
    serializer_class = BodyDataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return BodyData.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def calculate_bmi(self, request):
        height = request.data.get('height')
        weight = request.data.get('weight')
        if not height or not weight:
            return Response({'error': '身高和体重必须提供'}, status=status.HTTP_400_BAD_REQUEST)
        
        height_m = height / 100
        bmi = weight / (height_m * height_m)
        return Response({'bmi': round(bmi, 1)})

    @action(detail=False, methods=['post'])
    def calculate_bmr(self, request):
        gender = request.data.get('gender')
        age = request.data.get('age')
        height = request.data.get('height')
        weight = request.data.get('weight')
        
        if not all([gender, age, height, weight]):
            return Response({'error': '所有参数必须提供'}, status=status.HTTP_400_BAD_REQUEST)
        
        if gender == 1:
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        
        return Response({'bmr': round(bmr, 1)})


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class FoodDictViewSet(viewsets.ModelViewSet):
    queryset = FoodDict.objects.all()
    serializer_class = FoodDictSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        foods = FoodDict.objects.filter(food_name__icontains=query)
        serializer = self.get_serializer(foods, many=True)
        return Response(serializer.data)


class FoodRecordViewSet(viewsets.ModelViewSet):
    queryset = FoodRecord.objects.all()
    serializer_class = FoodRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return FoodRecord.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def daily_summary(self, request):
        date = request.query_params.get('date')
        if not date:
            return Response({'error': '日期必须提供'}, status=status.HTTP_400_BAD_REQUEST)
        
        records = FoodRecord.objects.filter(
            user=request.user,
            intake_time__date=date
        )
        
        total_calories = 0
        meal_summary = {}
        
        for record in records:
            calories = (record.food.calorie * record.intake_amount) / 100
            total_calories += calories
            
            meal_type = record.get_meal_type_display()
            if meal_type not in meal_summary:
                meal_summary[meal_type] = {'count': 0, 'calories': 0}
            meal_summary[meal_type]['count'] += 1
            meal_summary[meal_type]['calories'] += calories
        
        return Response({
            'date': date,
            'total_calories': round(total_calories, 1),
            'meal_summary': meal_summary,
            'record_count': records.count()
        })
