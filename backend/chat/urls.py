from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="chat"),
    path("<str:room_name>/", room, name="room"),
]

