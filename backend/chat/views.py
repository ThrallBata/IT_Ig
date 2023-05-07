from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from appsite.models import Message, User
from .serializers import MessageSerializer


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
        print(self.request.user.id)
        return Message.objects.filter(user_id=user)

    def perform_create(self, serializer):
        user_id = Token.objects.get(key=self.request.auth.key).user_id
        user = get_object_or_404(User, id=user_id)
        print(user)
        return serializer.save(user=user)


def index(request):
    user = request.user.id
    return render(request, "chat/index.html", {'user': user})


def room(request, room_name):
    if str(request.user.id) == str(room_name):
        return render(request, "chat/room.html", {"room_name": room_name})
    else:
        return redirect('start-chat')


