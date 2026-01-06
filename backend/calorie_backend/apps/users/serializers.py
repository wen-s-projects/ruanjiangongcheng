from rest_framework import serializers
from .models import User, BodyData, Event, FoodDict, FoodRecord, Admin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'photo', 'background', 'introduction', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'photo', 'background', 'introduction']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class BodyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyData
        fields = ['id', 'user', 'gender', 'age', 'height', 'weight', 'fat_rate', 'bmi', 
                  'basic_activity_level', 'basal_metabolic_rate']
        read_only_fields = ['id', 'bmi', 'basal_metabolic_rate']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'user', 'event_record', 'event_time', 'remarks']
        read_only_fields = ['id', 'event_time']


class FoodDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDict
        fields = ['id', 'food_name', 'calorie']


class FoodRecordSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.food_name', read_only=True)
    calorie = serializers.DecimalField(source='food.calorie', read_only=True, max_digits=6, decimal_places=1)

    class Meta:
        model = FoodRecord
        fields = ['id', 'user', 'food', 'food_name', 'calorie', 'intake_time', 'meal_type', 'intake_amount']
        read_only_fields = ['id', 'intake_time']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['admin_id', 'username']
        read_only_fields = ['admin_id']
