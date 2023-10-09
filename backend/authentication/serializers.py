from rest_framework import serializers
from appsite.models import *


class ProfileSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    token_refresh = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('__all__')

    # def create(self, validated_data):
    #     return Profile.objects.create_profile(**validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

#TODO переопределить пароль абстракт юзер

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password')
