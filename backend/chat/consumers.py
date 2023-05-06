import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from appsite.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def create_message(self, message, user): #def create_message(self, message, user_id):
        message_obj = Message.objects.create(
            content=message,
            user_id=int(user)
        )
        return message_obj

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        user = data['room']

        # Create a new message object and save it to the database
        message_obj = await self.create_message(message, user)# message_obj = await self.create_message(message, user_id)

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_obj.content,
                'user': message_obj.user_id,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send the message to the websocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))
