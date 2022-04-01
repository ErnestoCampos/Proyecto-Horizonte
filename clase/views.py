from pyexpat import model
from urllib import request
from django.views.generic import ListView
from django.shortcuts import redirect, render
from clase.models import Comentario, Posts, Usuario
from clase.forms import Formulario_Comentario, Formulario_Publicacion, Formulario_Usuario, Usuario_Busqueda, Publicacion_Crear



# Create your views here.

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

def lista_usuarios(request):

    nombre_a_buscar = request.GET.get('nombre', None)

    if nombre_a_buscar is not None:
        usuarios = Usuario.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        usuarios = Usuario.objects.all()

    form = Usuario_Busqueda()
    return render(request, 'form/lista_usuarios.html', {'form': form, 'usuarios': usuarios})

# CRUD Basico

def publicacion_listado(request): 
    publicaciones_listado = Posts.objects.all()
    return render(request, 'form/publicacion_listado.html', {'publicaciones_listado': publicaciones_listado}) 

def crear_publicacion(request): 
    if request.method == 'POST': 
        formulario_cp = Formulario_Publicacion(request.POST)    
    
        if formulario_cp.is_valid():
            data = formulario_cp.cleaned_data
            nueva_publicacion = Posts(
            Autor=data["Autor"],FechaDePublicacion=data["FechaDePublicacion"])
            nueva_publicacion.save()
            return redirect('publicacion_listado')
 
    formulario_cp = Formulario_Publicacion()
    return render(request, 'form/crear_publicaciones.html', {'formulario_cp': formulario_cp})

def update_publicacion(request, id): 

    publicacion = Posts.objects.get(id=id)

    if request.method == 'POST': 
        formulario_ap = Formulario_Publicacion(request.POST)    
    
        if formulario_ap.is_valid():
            data = formulario_ap.cleaned_data
            publicacion.Autor = data["Autor"]
            publicacion.FechaDePublicacion = data["FechaDePublicacion"]
            publicacion.save()
            return redirect('publicacion_listado')
    formulario_ap = Formulario_Publicacion(
        initial={
            'Autor': publicacion.Autor,
            'FechaDePublicacion': publicacion.FechaDePublicacion
        })
    return render(request, 'form/update_publicaciones.html', {'formulario_ap': formulario_ap, 'publicacion': publicacion})

def borrar_publicacion(request, id):
    publicacion = Posts.objects.get(id=id)
    publicacion.delete()
    return redirect('publicacion_listado')

def leer_publicacion(request): pass


# CRUD con Clases Basadas en Vistas (CBV)


class ListaPosts(ListView):
    model = Posts
    template_name = "form/posts_list.html"
