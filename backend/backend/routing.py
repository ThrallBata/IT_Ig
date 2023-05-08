
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path, path, include
from chat.consumers import ChatConsumer
from chat.views import *

websocket_urlpatterns = [
    re_path(r'chat/', ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('messages/', MessageList.as_view()),
    path('auth/', include('djoser.urls')), #Authentication
    re_path(r'^token/', include('djoser.urls.authtoken')), #get token
]