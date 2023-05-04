from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("<str:room_name>/", room, name="room"),
    path('messages/', MessageList.as_view()),
]

