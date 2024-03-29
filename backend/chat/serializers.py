from rest_framework import serializers
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'content', 'chat', 'file', )
        read_only_fields = ('id', 'user')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'client', 'staff', )
        read_only_fields = ('id',)


class ChatPerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'client', 'staff', 'username')
        read_only_fields = ('id',)
