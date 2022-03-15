import random
from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso 

# Create your views here.


def nuevo_curso(request):
    camada = random.randrange(1, 100)
    nuevo_curso = Curso(nombre = "Arquitectura de castillos de naipes", camada = camada)
    nuevo_curso.save()
    return HttpResponse(f"Inscribite al nuevo curso de {nuevo_curso.nombre} en la camada numero {nuevo_curso.camada}")  


def formulario(request):
    return render(request,"clase\formulario.html")
