from django.shortcuts import render
from django.http import HttpResponse
from .models import Enfermedad

# Create your views here.
def enfermedad1(request):
    enfermedades = Enfermedad.objects.all().order_by('fecha')
    return render(request,'enfermedades.html',{'enfermedades': enfermedades})