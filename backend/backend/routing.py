
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path, path, include
from chat.consumers import ChatConsumer
from chat.urls import urlpatterns as chaturls
websocket_urlpatterns = [
    re_path(r'chat/', ChatConsumer.as_asgi()),
]

urlpatterns = [

    #Authentication:
    path('auth/', include('djoser.urls')), #Authentication
    re_path(r'^auth/', include('djoser.urls.authtoken')), #get token
    
    #Chat:
    path('', include(chaturls)),
]