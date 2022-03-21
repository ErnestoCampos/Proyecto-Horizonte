from django import views
from django.urls import URLPattern
from django.urls import path
from .views import formulario_comentario, formulario_publicacion, formulario_usuario, lista_usuario 


urlpatterns = [
    path('Formulario/', formulario_usuario, name="Formulario"),
    path('Publicaciones/', formulario_publicacion, name="Publicaciones"),
    path('Comentarios/', formulario_comentario, name="Comentarios"), 
    path('usuarios/', lista_usuario , name="lista_usuarios")
]
