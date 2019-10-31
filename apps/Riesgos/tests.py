from django.test import TestCase, Client
from django.urls import reverse

from apps.Riesgos.views import poblacionEliminar

class Tests(TestCase):
    def setUp(self):
        self.client = Client()

    def testEliminar(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertContains(response, 'Iniciar Sesión')
# Create your tests here.
