from rest_framework import serializers
from appsite.models import *


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    token = serializers.CharField(max_length=255, read_only=True)
    token_refresh = serializers.CharField(max_length=255, read_only=True)



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'password')


class AuthenticationSerializer(serializers.Serializer):
    phone = serializers.CharField()


class AuthenticateCodeSerializer(AuthenticationSerializer):
    authcode = serializers.CharField()

