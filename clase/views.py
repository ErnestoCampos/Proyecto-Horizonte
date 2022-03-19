from django.shortcuts import render
from clase.models import Usuario
from clase.forms import Formulario_Usuario


# Create your views here.

def busqueda(request):
    return(request, "form/busqueda.html")

def formulario_usuario(request):
    print(request.method)

    # if request.method == "POST":
    #      = Usuario(nombre=request.POST["Nombre"],email=request.POST["Email"],contraseña=request.POST["Contraseña"],registrado=True)
    #     .save()
    #     print(request.POST)
    # return render(request,"form/formulario.html", {"formulario": formulario})

    # Forma con Django Forms
    if request.method == 'POST': 
        formulario = Formulario_Usuario(request.POST)    
    
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_usuario = Usuario(nombre=data['nombre'],email=data['email'], contraseña=data['contraseña'],registrado=True)
            nuevo_usuario.save()
            return render(request, 'index/index.html', {'nuevo_usuario': nuevo_usuario})
        
    else:
        formulario = Formulario_Usuario()
        return render(request, 'form/formulario.html', {'formulario': formulario})
