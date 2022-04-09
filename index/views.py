from urllib import request
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import NuestraCreacionUser

from index.forms import NuestraCreacionUser
def inicio(request):
    return render(request,"index/index.html")

def sobre_mi(request):
    return render(request, "index/About.html")

def publicaciones(request):
    return render(request, "index/Publicaciones.html")

def Log_In(request):
    return render(request, "index/Log_In.html")

def Registro(request):
    return render(request, "index/Registro.html")

def Año(request,numero):
    resultado = 2022 - numero
    return HttpResponse(f"<h1>Naciste en el año: {resultado}</h1>") 

def login_proyecto(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "index/index.html", {"mensaje":"Te Logueaste correctamente!"})
            else:
                return render(request, "index/login.html", {"form": form, "mensaje":"No se autentico"})
        else: 
            return render(request, "index/login.html", {"form": form, "mensaje":"Formulario con datos incorrectos"})
    else:
        form = AuthenticationForm()   
        return render(request, "index/login.html", {"form": form, "mensaje":""})

def register_proyecto(request):
    if request.method == "POST":
        form = NuestraCreacionUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"index/index.html", {"mensaje":f"Usuario {username} Creado"}) 
        else:
            return render(request, "index/register.html", {"form": form, "mensaje":""}) 

    form = NuestraCreacionUser()
    return render(request,"index/register.html",{"form": form,"mensaje":""})