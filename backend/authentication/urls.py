from django.urls import path

from .views import *


urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='registration'),
    path('code_send/', AuthenticationAPIView.as_view(), name='send_code'),
    path('verify_code/', AuthenticateCodeAPIView.as_view(), name='verify_code'),
    path('refresh/', authenticate_refresh_tokenAPIView, name='refresh_token'),

]
