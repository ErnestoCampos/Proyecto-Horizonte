from django.shortcuts import render
from clase.models import Comentario, Posts, Usuario
from clase.forms import Formulario_Comentario, Formulario_Publicacion, Formulario_Usuario, Buscador


# Create your views here.

def busqueda(request):
    return(request, "form/busqueda.html")

def formulario_comentario(request):
    print(request.method)
    if request.method == 'POST': 
        formulario_c = Formulario_Comentario(request.POST)    
    
        if formulario_c.is_valid():
            data = formulario_c.cleaned_data
            nuevo_comentario = Comentario(Autor=data["Autor"],FechaDePublicacion=data["FechaDePublicacion"])
            nuevo_comentario.save()
            return render(request, 'index/index.html', {'nuevo_comentario': nuevo_comentario})
        
    
    formulario_c = Formulario_Comentario()
    return render(request,'form/Comentarios.html', {'formulario_c': formulario_c})

def formulario_publicacion(request):
    print(request.method)
    if request.method == 'POST': 
        formulario_p = Formulario_Publicacion(request.POST)    
    
        if formulario_p.is_valid():
            data = formulario_p.cleaned_data
            nueva_publicacion = Posts(Autor=data["Autor"],FechaDePublicacion=data["FechaDePublicacion"])
            nueva_publicacion.save()
            return render(request, 'index/index.html', {'nueva_publicacion': nueva_publicacion})
        
    
    formulario_p = Formulario_Publicacion()
    return render(request,'form/Publicaciones.html', {'formulario_p': formulario_p})

def formulario_usuario(request):
    print(request.method)
    # Forma con Django Forms
    if request.method == 'POST': 
        formulario_u = Formulario_Usuario(request.POST)    
    
        if formulario_u.is_valid():
            data = formulario_u.cleaned_data
            nuevo_usuario = Usuario(nombre=data['nombre'],email=data['email'], contraseña=data['contraseña'],registrado=True)
            nuevo_usuario.save()
            return render(request, 'index/index.html', {'nuevo_usuario': nuevo_usuario})
        
   
    formulario_u = Formulario_Usuario()
    return render(request, 'form/formulario.html', {'formulario_u': formulario_u})


