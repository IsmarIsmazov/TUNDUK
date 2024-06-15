from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .manager import CustomUserManager
from .constants import *


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    verify_code = models.CharField(max_length=6, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')
    is_active = models.BooleanField(default=True)
    code_user = models.IntegerField(default=0)
    class_user = models.CharField(max_length=50)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    time = models.DateTimeField()
