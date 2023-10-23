from django.test import TestCase

from authentication.utils import *


class UtilsTestCase(TestCase):
    def test_create_auth_code(self):
        phone = '88005553535'
        authcode = str(create_auth_code(phone))
        redis_authcode = redis_auth_code.get(phone).decode("utf-8")
        self.assertEquals(redis_authcode, authcode)

    def test_get_token_jwt(self):
        phone = '88005553535'
        token = get_token_jwt(phone)
        redis_token_jwt = redis_jwt.get(phone).decode("utf-8")
        self.assertEquals(redis_token_jwt, token)

    def test_get_token_refresh(self):
        phone = '88005553535'
        token = get_token_refresh(phone)
        redis_token = redis_refresh_token.get(phone).decode("utf-8")
        self.assertEquals(redis_token, token)
