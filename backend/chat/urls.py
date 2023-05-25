from django.urls import path, include

from .views import *
from .routing import *

urlpatterns = [
    path("chat/", index, name="start-chat"),
    path("chat/<str:room_name>/", room, name="room"),
    path('api/chat/', ChatAPIView),
    path('api/chat/<int:chat_id>', ChatAPIView),
    path('ws/', include(websocket_urlpatterns)),
]

