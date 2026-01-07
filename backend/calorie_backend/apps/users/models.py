from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('用户名必须提供')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='最后登录时间')
    photo = models.CharField(max_length=255, null=True, blank=True, verbose_name='头像')
    background = models.CharField(max_length=255, null=True, blank=True, verbose_name='背景图')
    introduction = models.TextField(null=True, blank=True, verbose_name='个人简介')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    is_staff = models.BooleanField(default=False, verbose_name='是否为管理员')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'User'
        verbose_name = '用户'
        verbose_name_plural = '用户'


class BodyData(models.Model):
    GENDER_CHOICES = [
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        (1, '久坐'),
        (2, '轻度'),
        (3, '中度'),
        (4, '高度'),
        (5, '极高'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    height = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='身高(cm)')
    weight = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='体重(kg)')
    fat_rate = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='体脂率(%)')
    bmi = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, verbose_name='BMI')
    basic_activity_level = models.IntegerField(choices=ACTIVITY_LEVEL_CHOICES, null=True, blank=True, verbose_name='基础活动量')
    basal_metabolic_rate = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True, verbose_name='基础代谢率(kcal)')

    class Meta:
        db_table = 'BodyData'
        verbose_name = '身体数据'
        verbose_name_plural = '身体数据'


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    event_record = models.CharField(max_length=500, verbose_name='饮食总记录')
    event_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    remarks = models.CharField(max_length=200, null=True, blank=True, verbose_name='备注')

    class Meta:
        db_table = 'Event'
        verbose_name = '饮食总表'
        verbose_name_plural = '饮食总表'


class FoodDict(models.Model):
    food_name = models.CharField(max_length=50, unique=True, verbose_name='食物名称')
    calorie = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='热量(kcal/100g)')

    class Meta:
        db_table = 'FoodDict'
        verbose_name = '食物字典'
        verbose_name_plural = '食物字典'


class FoodRecord(models.Model):
    MEAL_TYPE_CHOICES = [
        (1, '早餐'),
        (2, '午餐'),
        (3, '晚餐'),
        (4, '加餐'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    food = models.ForeignKey(FoodDict, on_delete=models.CASCADE, verbose_name='食物')
    intake_time = models.DateTimeField(auto_now_add=True, verbose_name='摄入时间')
    meal_type = models.IntegerField(choices=MEAL_TYPE_CHOICES, verbose_name='餐次类型')
    intake_amount = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='摄入量(g)')

    class Meta:
        db_table = 'FoodRecord'
        verbose_name = '食物摄入记录'
        verbose_name_plural = '食物摄入记录'


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, verbose_name='管理员用户名')
    password = models.CharField(max_length=255, verbose_name='密码')

    class Meta:
        db_table = 'Admin'
        verbose_name = '管理员'
        verbose_name_plural = '管理员'
