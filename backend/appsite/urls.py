from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('api/v1/progectlist/', ProjectAPIView.as_view()),

]
