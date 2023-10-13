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
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password')
