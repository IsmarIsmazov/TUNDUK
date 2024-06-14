from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import SubSystems, Services, SecurityServers
from .serializers import SubSystemSerializer, ServicesSerializer, SecurityServersSerializer


class SubSystemsViewSet(ModelViewSet):
    queryset = SubSystems.objects.all()
    serializer_class = SubSystemSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class SecurityServersViewSet(ModelViewSet):
    queryset = SecurityServers.objects.all()
    serializer_class = SecurityServersSerializer
