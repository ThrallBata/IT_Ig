from rest_framework import serializers
from appsite.models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'content', 'chat', 'file', )
        read_only_fields = ('id', 'user')


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields =('__all__')


