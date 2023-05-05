from django.urls import path
from .views import *

urlpatterns = [
    path("<str:room_name>/", room, name="room"),
    path('messages/', MessageList.as_view()),
]

