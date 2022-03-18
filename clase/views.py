import email
import random
from django.http import HttpResponse
from django.shortcuts import render
from clase.forms import nuevo_usuario

from clase.models import Usuario


# Create your views here.

def formulario(request):
    print(request.method)

    # Forma Tradicional
    # if request.method == "POST":
    #     nuevo_usuario = Usuario(nombre=request.POST["Nombre"],email=request.POST["Email"],contraseña=request.POST["Contraseña"],registrado=True)
    #     nuevo_usuario.save()
    #     print(request.POST)

    # Forma con Django Forms
    if request.method == "POST":
        formulario = nuevo_usuario(request.POST)
        if formulario.is_valid:
            data = formulario.cleaned_data
            usuario_nuevo = Usuario(nombre=data["Nombre"],email=data["Email"],contraseña=data["Contraseña"],registrado=True)
            usuario_nuevo.save()
            return render(request,"form/formulario.html", {"usuario_nuevo":usuario_nuevo})

    formulario = nuevo_usuario()
    return render(request,"form/formulario.html", {"formulario": formulario})
