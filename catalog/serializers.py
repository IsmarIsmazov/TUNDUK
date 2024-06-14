from rest_framework import serializers
from .models import SubSystems, Services, SecurityServers


class SubSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSystems
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class SecurityServersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityServers
        fields = '__all__'
