from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index, name="start-chat"),
    path("admin/", ChatAPIView.as_view(), name='chat-user'),
    # path("<str:room_name>/", ChatAPIView.as_view(), name='chat-user'),
    # path("<str:room_name>/", room, name="room"),
]

