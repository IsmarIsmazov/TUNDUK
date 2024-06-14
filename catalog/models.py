from django.utils import timezone

from django.db import models
from rest_framework.authtoken.admin import User

from common.models import BaseModel


# Create your models here.

class SubSystems(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    code_sub_system = models.CharField(max_length=255)


class Services(BaseModel):
    subsystem = models.ForeignKey(SubSystems, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date_register = models.DateTimeField(default=timezone.now())
    description = models.TextField()
    code_service = models.CharField(max_length=255)
    status = models.BooleanField(default=False)


class SecurityServers(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
