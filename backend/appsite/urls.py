from django.urls import include, path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('api/progectlist/', ProjectAPIView.as_view()),
    path('api/userid', UserByTokenAPIView.as_view(), name='userid'),
    path('api/order', OrderAPIView.as_view(), name='create-order'),
    path('api/order/<int:pk>/', OrderConfimAPIUpdate.as_view(), name='update-status'),

    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
