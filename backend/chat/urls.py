
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path, path, include
from .views import ChatAPIView

urlpatterns = [
    path('chat', ChatAPIView),
    path('chat/<int:chat_id>', ChatAPIView),
    ]