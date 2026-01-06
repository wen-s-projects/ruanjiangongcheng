from django.contrib import admin
from .models import User, BodyData, Event, FoodDict, FoodRecord, Admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_active', 'is_staff', 'created_at']
    list_filter = ['is_active', 'is_staff', 'created_at']
    search_fields = ['username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(BodyData)
class BodyDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gender', 'age', 'height', 'weight', 'bmi']
    list_filter = ['gender', 'basic_activity_level']
    search_fields = ['user__username']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'event_record', 'event_time']
    list_filter = ['event_time']
    search_fields = ['user__username', 'event_record']


@admin.register(FoodDict)
class FoodDictAdmin(admin.ModelAdmin):
    list_display = ['id', 'food_name', 'calorie']
    search_fields = ['food_name']


@admin.register(FoodRecord)
class FoodRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'food', 'intake_time', 'meal_type', 'intake_amount']
    list_filter = ['meal_type', 'intake_time']
    search_fields = ['user__username', 'food__food_name']


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['admin_id', 'username']
    search_fields = ['username']
