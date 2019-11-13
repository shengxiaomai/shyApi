from unittest import TestCase

from api.login import Login


class TestLogin(TestCase):
    def test_login(self):
        login=Login()
        token=login.login()
        assert token !=None

