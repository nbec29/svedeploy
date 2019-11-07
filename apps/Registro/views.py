from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.Registro.formularios import RegistroUsuario
from django.urls import reverse
from django.contrib.auth.models import Group

# Create your views here.
def registro(request):
    return render(request, 'registro.html')


def login(request):
    return render(request, 'login.html')


class PersonaCreate(CreateView):
    model = User
    form_class = RegistroUsuario
    template_name = 'registro.html'

    def get_success_url(self):
        return reverse('login')
