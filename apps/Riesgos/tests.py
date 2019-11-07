from nose.tools import assert_true
from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):
    def test_home(self):
        response = self.client.get('http://127.0.0.1:8000/login')
        self.assertEquals(response.status_code, 200)