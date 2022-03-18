import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def formulario(request):
    return render(request,"form/formulario.html")
