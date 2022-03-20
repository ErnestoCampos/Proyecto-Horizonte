from django.shortcuts import render
from clase.models import Posts, Usuario
from clase.forms import Formulario_Publicacion, Formulario_Usuario, Buscador


# Create your views here.

def busqueda(request):
    return(request, "form/busqueda.html")

def formulario_publicacion(request):
    print(request.method)
    if request.method == 'POST': 
        Formulario = Formulario_Publicacion(request.POST)    
    
        if Formulario.is_valid():
            data = Formulario.cleaned_data
            nueva_publicacion = Posts(Autor=data["Autor"],FechaDePublicacion=data["FechaDePublicacion"])
            nueva_publicacion.save()
            return render(request, 'index/index.html', {'nueva_publicacion': nueva_publicacion})
        
    
    Formulario = Formulario_Publicacion()
    return render(request,'form/Publicaciones.html', {'Formulario': Formulario})

def formulario_usuario(request):
    print(request.method)
    # Forma con Django Forms
    if request.method == 'POST': 
        formulario = Formulario_Usuario(request.POST)    
    
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_usuario = Usuario(nombre=data['nombre'],email=data['email'], contraseña=data['contraseña'],registrado=True)
            nuevo_usuario.save()
            return render(request, 'index/index.html', {'nuevo_usuario': nuevo_usuario})
        
   
    formulario = Formulario_Usuario()
    return render(request, 'form/formulario.html', {'formulario': formulario})


