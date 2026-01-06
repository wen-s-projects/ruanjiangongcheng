from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, BodyDataViewSet, EventViewSet, 
                     FoodDictViewSet, FoodRecordViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'body-data', BodyDataViewSet, basename='bodydata')
router.register(r'events', EventViewSet, basename='event')
router.register(r'foods', FoodDictViewSet, basename='fooddict')
router.register(r'food-records', FoodRecordViewSet, basename='foodrecord')

urlpatterns = [
    path('', include(router.urls)),
]
