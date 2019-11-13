from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from apps.Registro.formularios import RegistroUsuario
from django.contrib.auth.models import Group
from django.urls import reverse


# Create your views here.
def registro(request):
    print('RegistroUsuario')
    print(request.POST)
    return render(request,'registro.html')

def login(request):
    return render(request,'login.html')



class PersonaCreate(CreateView):
    model = User
    form_class = RegistroUsuario
    template_name = 'registro.html'

    def get_success_url(self):
       
        username_form = self.request.POST.get('username')
        usuario = User.objects.filter(username = username_form ).get()
        g = Group.objects.get(name = 'Usuarios')
        g.user_set.add(usuario)
        return reverse('login')

    



