from ast import For
from urllib import request
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


def inicio(request):
    return render(request,"index/index.html", {})

def sobre_mi(request):
    return render(request, "index/About.html", {})

def publicaciones(request):
    return render(request, "index/Publicaciones.html")

def Log_In(request):
    return render(request, "index/Log_In.html")

def Registro(request):
    return render(request, "index/Registro.html")

def Año(request,numero):
    resultado = 2022 - numero
    return HttpResponse(f"<h1>Naciste en el año: {resultado}</h1>") 

