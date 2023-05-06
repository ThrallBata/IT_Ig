from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="start-chat"),
    path("1/admin/", UserChatAPIView.as_view(), name='chat-user'),
    # path("<str:room_name>/", ChatAPIView.as_view(), name='chat-user'),
    path("<str:room_name>/", room, name="room"),
]

