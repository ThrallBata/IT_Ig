from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from appsite.models import Message, User, Chat
from .serializers import MessageSerializer, ChatSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
@authentication_classes([TokenAuthentication,])
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

            chatRecord = Chat.objects.create(client_id=int(request.user.id), staff=None)
            Message.objects.create(user_id=1, content="Здравствуйте, здесь вы можете задать свои вопросы. Работник свяжется с вами в ближайшее время.", chat_id=chatRecord.id)
        return Response(MessageSerializer(Message.objects.filter(chat=int(chatRecord.pk)), many=True).data)

#
#
#
#
#
#
#
#
#
#

def index(request):
    user = request.user.id
    return render(request, "chat/index.html", {'user': user})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
    # if str(request.user.id) == str(room_name):
    #     return render(request, "chat/room.html", {"room_name": room_name})
    # else:
    #     return redirect('start-chat')


