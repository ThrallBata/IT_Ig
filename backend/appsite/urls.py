from django.urls import include, path, re_path

from .views import *

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', index, name='home'),
    path('api/progectlist/', ProjectAPIView.as_view()),

    path('api/order', OrderAPIView.as_view(), name='create-order'),
    path('api/order/<int:pk>/', OrderChangeAPIUpdate.as_view(), name='update-order'),
    path('api/order/<int:pk>/confim/', OrderConfimAPIUpdate.as_view(), name='update-status'),
    path('api/order/all/', OrderListAPIView.as_view(), name='order-list'),


    path('api/userid/', UserByTokenAPIView.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
