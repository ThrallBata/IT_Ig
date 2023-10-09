from django.urls import path

from .views import *


urlpatterns = [
    path('', RegistrationAPIView.as_view(), name='registration'),
    path('code_entry/', authenticate_codeAPIView, name='entry_by_code'),
    path('refresh/', authenticate_refresh_tokenAPIView, name='refresh_token'),

]
