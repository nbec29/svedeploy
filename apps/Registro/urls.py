from django.urls import path
from apps.Registro.views import login, PersonaCreate


urlpatterns = [
    path('registro/', PersonaCreate.as_view(), name='Registro'),
    path('login/', login,name='login'),

]