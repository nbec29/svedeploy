from django.urls import path
from apps.Enfermedades.views import enfermedad1

from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^', login_required(enfermedad1), name='enfermedad'),
]