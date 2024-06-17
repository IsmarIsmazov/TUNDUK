from rest_framework import serializers
from .models import SubSystems, Services, SecurityServers
from users.serializers import CustomUserSerializer


class SubSystemSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = SubSystems
        fields = ('id', 'title', 'description', 'user', 'code', 'code_sub_system')


class ServicesSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Services
        fields = ('id', 'subsystem', 'title', 'date_register', 'description', 'code_service', 'status', 'user')


class SecurityServersSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = SecurityServers
        fields = ('id', 'title', 'description', 'user', 'address')
