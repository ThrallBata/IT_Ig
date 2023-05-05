from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from appsite.models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Фильтруем сообщения по пользователю который отправил запрос
        """
        user = self.request.user
        print(self.request.user)
        return Message.objects.filter(user_id=user)


def index(request):

    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


