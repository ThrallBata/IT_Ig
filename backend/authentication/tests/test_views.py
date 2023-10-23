from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from appsite.models import User

from authentication.serializers import RegistrationSerializer


class RegistrationAPITestCase(APITestCase):
    def test_post(self):
        url = reverse('registration')
        data = {'username': 'user1', 'email': 'vicortobdel@ma.ry', 'password': '1234wefefef', 'phone': '+79131125437'}
        responce = self.client.post(path=url, data=data)
        # user = User.objects.get(username='user1')
        # serializer_data = RegistrationSerializer(user).data
        self.assertEquals(status.HTTP_201_CREATED, responce.status_code)


class AuthenticationAPITestCase(APITestCase):
    def test_post_correct(self):
        url = reverse('send_code')
        user = User.objects.create(username='user1', email='vicortobdel@ma.ry',
                                   password='1234wefefef', phone='+79131125437')
        data = {'phone': '+79131125437'}
        responce = self.client.post(path=url, data=data)

        self.assertEquals(status.HTTP_200_OK, responce.status_code)

    def test_post_no_correct_phone(self):
        url = reverse('send_code')
        user = User.objects.create(username='user1', email='vicortobdel@ma.ry', password='1234wefefef',
                                   phone='+79131125437')
        data = {'phone': '+79132222237'}
        responce = self.client.post(path=url, data=data)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, responce.status_code)
        self.assertEquals({'responce': 'Incorrect data'}, responce.data)

