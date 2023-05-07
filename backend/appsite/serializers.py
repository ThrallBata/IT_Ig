from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'resource', 'photo')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'description', 'status')


class OrderConfimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status')
