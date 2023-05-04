from django.urls import path
from .views import *


urlpatterns = [
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
    # path("chat/<str:chat_box_name>/", chat_box, name="chat"),
]
