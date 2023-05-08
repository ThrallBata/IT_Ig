from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.authtoken.models import Token
from appsite.models import Message, User, Chat
from .serializers import *


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,) #token-only access

    def get_queryset(self):
        """
        Фильтруем сообщения по пользователю который отправил запрос
        """
        user = self.request.user
        user_id = self.request.user.id
        if User.objects.get(id=int(user_id)).is_staff == True:
            return Message.objects.filter(user_id=user)
        else:
            chat = Chat.objects.filter(client_id=user)
            if list(chat.values()) == []:
                Chat.objects.create(
                    id=int(user_id),
                    client_id=int(user_id),
                    status_view=False
                )
                Message.objects.create(
                    chat_id=int(user_id),
                    user_id=int(user_id),
                    content=' '
                )
            return Message.objects.filter(user_id=user)

    def perform_create(self, serializer):
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        user = get_object_or_404(User, id=user_id)

        return serializer.save(user=user)


class ChatListAPIList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


def index(request):
    user = request.user.id
    return render(request, "chat/index.html", {'user': user})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
    # if str(request.user.id) == str(room_name):
    #     return render(request, "chat/room.html", {"room_name": room_name})
    # else:
    #     return redirect('start-chat')


