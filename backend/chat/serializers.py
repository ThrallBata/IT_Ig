from rest_framework import serializers
from appsite.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'content', 'client', 'file', )
        read_only_fields = ('id', 'user')
