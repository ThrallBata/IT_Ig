from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index, name="chat"),
    path("<str:room_name>/", room, name="room"),
]

