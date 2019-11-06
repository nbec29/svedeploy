from django.contrib.auth.models import User
from nose.tools import assert_true
from django.test import SimpleTestCase
from django.http import HttpRequest

class HomePageTests(SimpleTestCase):
    def test_home(self):
        response = self.client.get('/login')
        self.assertEquals(response.status_code, 200)

def test_numbers_3_4():
    assert 4 * 3 == 12
