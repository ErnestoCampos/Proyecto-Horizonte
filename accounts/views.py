from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Avatar
from .forms import NuestraCreacionUser, NuestraEdicionUser

# Create your views here.

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
                return render(request, "login.html", {"form": form, "mensaje":"No se autentico"})
        else: 
            return render(request, "login.html", {"form": form, "mensaje":"Formulario con datos incorrectos"})
    else:
        form = AuthenticationForm()   
        return render(request, "login.html", {"form": form, "mensaje":""})

def register_proyecto(request):
    if request.method == "POST":
        form = NuestraCreacionUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"index/index.html", {"mensaje":f"Usuario {username} Creado"}) 
        else:
            return render(request, "register.html", {"form": form, "mensaje":""}) 

    form = NuestraCreacionUser()
    return render(request,"register.html",{"form": form, "mensaje":""})

@login_required
def editar_user(request): 
    mensaje = ""
    extension_logued_user, _ = Avatar.objects.get_or_create(user=request.user)
    if request.method == "POST":
        FormularioUser = NuestraEdicionUser(request.POST, request.FILES)

        if FormularioUser.is_valid(): 

            data = FormularioUser.cleaned_data

            logued_user = request.user #intancia del Usuario
            logued_user.email = FormularioUser.cleaned_data['email']
            logued_user.first_name = FormularioUser.cleaned_data['first_name']
            logued_user.last_name = FormularioUser.cleaned_data['last_name']
            extension_logued_user.imagen = FormularioUser.cleaned_data['imagen']
            extension_logued_user.link = FormularioUser.cleaned_data['link']
            extension_logued_user.more_info = FormularioUser.cleaned_data['more_info']

            if FormularioUser.cleaned_data['password1'] != '' and FormularioUser.cleaned_data['password1'] == FormularioUser.cleaned_data['password2']:
                logued_user.set_password(data.get("password1"))
            else:
                mensaje = ""
            
            logued_user.save()
            extension_logued_user.save()

            return render(request, "index/index.html", {"mensaje":mensaje}) 
        else:
            return render(request, "EditUser.html", {"FormularioUser":FormularioUser,"mensaje":mensaje})

    FormularioUser = NuestraEdicionUser(
        initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'imagen': extension_logued_user.imagen,
            'link': extension_logued_user.link,
            'more_info': extension_logued_user.more_info,
        }
    )

    return render(request, "EditUser.html", {"FormularioUser": FormularioUser, "mensaje":mensaje}) 
            
@login_required
def info_user(request):
    return render(request, "infoUser.html", {}) 