from django.urls import path, include

from .views import *
from .routing import *

urlpatterns = [
    path("chat/", index, name="start-chat"),
    path("chat/<str:room_name>/", room, name="room"),
    path("api/messageslist/", MessageAPIList.as_view()),
    path("api/chatlist/", ChatListAPIList.as_view()),
    path('ws/', include(websocket_urlpatterns)),
]

