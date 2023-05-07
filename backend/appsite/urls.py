from django.urls import include, path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('api/progectlist/', ProjectAPIView.as_view()),

    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
