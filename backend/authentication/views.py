from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from appsite.models import User
from .serializers import UserSerializer, RegistrationSerializer, AuthenticationSerializer, AuthenticateCodeSerializer
from .tasks import send_authcode
from .utils import *


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'responce': 'You are registered!',}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthenticationAPIView(APIView):
    def post(self, request):   # получения номера телефона, создание и отправка кода
        serializer = AuthenticationSerializer(data=request.data)

#TODO поставить валидацию телефона в модели

        if serializer.is_valid():
            print(serializer.data.get('phone'))
            phone = serializer.data.get('phone')
            if User.objects.filter(phone_number=phone).exists() == True:
                if redis_auth_code.exists(phone) == 0:
                    authcode = create_auth_code(phone)
                    send_authcode.delay(phone, authcode)

                return Response({'responce': 'Code sent'}, status=status.HTTP_200_OK)
            return Response({'responce': 'Incorrect data'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthenticateCodeAPIView(APIView):
    def post(self, request):
        serializer = AuthenticateCodeSerializer(data=request.data)
        print(request.data.get('phone'))
        if serializer.is_valid():
            print(serializer.data.get('authcode'))
            authcode = serializer.data.get('authcode')
            phone = serializer.data.get('phone')

            code_redis = redis_auth_code.get(phone)
            if code_redis:
                code_redis = code_redis.decode("utf-8")

                if code_redis == authcode:
                    token_dict = get_tokens(phone)
                    return Response(UserSerializer(
                        {'phone': phone, 'token': token_dict['jwt'],
                         'token_refresh': token_dict['refresh']}, ).data)

        return Response({'error': 'неверные данные',}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def authenticate_refresh_tokenAPIView(request):
    # token_refresh_elem = request.data.get('token_refresh')
    # phone = request.data.get('phone')

    token_refresh_redis = redis_refresh_token.get(phone)

    redis_refresh_token.delete(phone)
    redis_auth_code.delete(phone)

    if token_refresh_redis:
        token_refresh_redis = token_refresh_redis.decode("utf-8")
        if token_refresh_elem == token_refresh_redis:
            token = get_tokens(phone)
            return Response({'token': token['jwt'], 'token_refresh': token['refresh']}, )

    return Response({'error': 'Неверные данные', }, status=status.HTTP_400_BAD_REQUEST)
