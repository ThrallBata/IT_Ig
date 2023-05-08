from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'resource', 'photo')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'description', 'status', 'client')


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')


class OrderConfimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status')
