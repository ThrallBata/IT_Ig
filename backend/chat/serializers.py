from rest_framework import serializers
from appsite.models import Message,Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'content', )
        read_only_fields = ('id',)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'client', 'staff', )
        read_only_fields = ('id',)