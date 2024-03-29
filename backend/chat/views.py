from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message, Chat
from appsite.models import User
from .serializers import MessageSerializer, ChatSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication, ])
def ChatAPIView(request, chat_id=None):
    try:
        userRecord = User.objects.get(pk=int(request.user.id))
    except:
        return Response(data="Error: user cannot be found", status=status.HTTP_400_BAD_REQUEST)
    if (userRecord.is_staff):
        if (chat_id):
            try:
                chatRecord = Chat.objects.get(pk=int(chat_id))
            except:
                return Response(data="Error: chat cannot be found", status=status.HTTP_400_BAD_REQUEST)
            Chat.objects.filter(pk=int(chat_id)).update(status_view=True)
            return Response(MessageSerializer(Message.objects.filter(chat=int(chat_id)), many=True).data)
        return Response(ChatSerializer(Chat.objects.all(), many=True).data)
    else:
        try:
            chatRecord = Chat.objects.get(client=int(request.user.id))
        except:

            chatRecord = Chat.objects.create(client_id=int(request.user.id))
            Message.objects.create(user_id=1, content="Здравствуйте, можете задать свои вопросы. Работник свяжется с вами в ближайшее время.", chat_id=chatRecord.id)
        return Response(MessageSerializer(Message.objects.filter(chat=int(chatRecord.pk)), many=True).data)

