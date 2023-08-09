from django.urls import path, include

from .views import *
from .routing import *

urlpatterns = [
    path('api/chat/', ChatAPIView),
    path('api/chat/<int:chat_id>', ChatAPIView),
    path('ws/', include(websocket_urlpatterns)),
]

