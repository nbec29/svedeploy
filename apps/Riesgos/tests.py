from nose.tools import assert_true
import requests

BASE_URL = "https://sveonline.herokuapp.com"


class NewUUID():

    def __init__(self, value):
        self.value = value


def test_request_login():
    response = requests.get('%s/login' % BASE_URL)
    assert_true(response.ok)


def test_request_logout():
    response = requests.get(
        '%s/logout' % BASE_URL)
    assert_true(response.ok)

def test_get_notificaciones():
    response = requests.get(
        '%s/inicio/notificaciones' % BASE_URL)
    assert_true(response.ok)

def test_get_poblacion():
    response = requests.get(
        '%s/inicio/administrarSVE/poblacionSVE' % BASE_URL)
    assert_true(response.ok)

def test_get_administrar():
    response = requests.get(
        '%s/inicio/administrarSVE' % BASE_URL)
    assert_true(response.ok)

def test_get_editar():
       response = requests.get(
          '%s/inicio/administrarSVE/poblacionSVE/editar/1' % BASE_URL)
       assert_true(response.ok)

def test_get_individual_request_404():
    response = requests.get('%s/request/an_incorrect_id' % BASE_URL)
    assert_true(response.status_code == 404)
from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):
    def test_home(self):
        response = self.client.get('http://127.0.0.1:8000/login')
        self.assertEquals(response.status_code, 200)
