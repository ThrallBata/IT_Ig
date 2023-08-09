from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import *
from .serializers import *


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        """
        Фильтруем заказы по пользователю который отправил запрос
        """
        user = self.request.user
        return Order.objects.filter(client_id=user)

    def perform_create(self, serializer):
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        user = get_object_or_404(User, id=user_id)
        return serializer.save(client=user)


class OrderConfimAPIUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderConfimSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        """
        Фильтруем заказы по пользователю который отправил запрос
        """
        user = self.request.user
        if User.objects.get(id=int(user.id)).is_staff == True:
            return Order.objects.all()
        return Order.objects.filter(client_id=user)


class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class OrderChangeAPIUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        """
        Фильтруем заказы по пользователю который отправил запрос
        """
        user = self.request.user
        if User.objects.get(id=int(user.id)).is_staff == True:
            return Order.objects.all()
        return Order.objects.filter(client_id=user)


class UserByTokenAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)#token-only access

    def get(self, request):
        user_id = Token.objects.get(key=request.auth.key).user_id
        return Response({'user_id': user_id})

