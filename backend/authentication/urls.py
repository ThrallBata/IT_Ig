from django.urls import path

from .views import *


urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='registration'),
    path('code_send/', AuthenticationAPIView.as_view(), name='send_code'),
    path('verify_code/', AuthenticationCodeAPIView.as_view(), name='verify_code'),
    path('refresh/', AuthenticationRefreshTokenAPIView.as_view(), name='refresh_token'),

]
