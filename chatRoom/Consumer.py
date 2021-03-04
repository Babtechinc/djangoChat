# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatModel
from channels.db import database_sync_to_async

class chatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "texter": self.room_name,
            }

        )

    async def chat_message(self, event):
        texter = event['texter']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'texter': texter
        }))
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message =  text_data_json['message']

        user =  text_data_json['user']
        msg = await self.Pushdata(text_data_json['message'],text_data_json['user'])

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_msg',
                'message': message,
                'user':user
            }
        )

    @database_sync_to_async
    def Pushdata(self,message,user):
        msg = ChatModel.objects.get_or_create(text=message, room=self.room_group_name,user=user)


    async def chat_msg(self, event):
            texter = event['message']
            user  = event['user']

            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': texter,
                'user':user
            }))
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)