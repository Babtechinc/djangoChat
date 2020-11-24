from . import Consumer
from django.urls import path,re_path
websocket_urlpatterns = [

    re_path(r'ws/chat/(?P<room_name>\w+)/$', Consumer.chatRoomConsumer.as_asgi()),
    ]