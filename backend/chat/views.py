from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from appsite.models import Message, User, Chat
from .serializers import MessageSerializer, ChatSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class MessageList(generics.ListCreateAPIView):
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

###
@api_view(['GET'])
@permission_classes([IsAuthenticated,TokenAuthentication,])
def ChatAPIView(request, chat_id=None):
    try:
        userRecord = User.objects.get(pk=int(request.user.id))
    except:
        return Response(data="Error: user cannot be found", status=status.HTTP_400_BAD_REQUEST)
    if (userRecord.is_staff):
        if (chat_id):
            try:
                chatRecord = Message.objects.get(pk=int(chat_id))
            except:
                return Response(data="Error: chat cannot be found", status=status.HTTP_400_BAD_REQUEST)
            return Response(JSONRenderer().render(MessageSerializer(Message.objects.filter(chat=int(chat_id)), many=True).data))
        return Response(JSONRenderer().render(ChatSerializer(Chat.objects.all(), many=True).data))
    else:
        try:
            chatRecord = Chat.objects.get(client=int(request.user.id))
        except:
            chatRecord = Chat.objects.create(client_id=int(request.user.id), staff=None)
        return Response(JSONRenderer().render(MessageSerializer(Message.objects.filter(chat=int(chatRecord.pk)), many=True).data))
        