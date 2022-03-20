from django.urls import URLPattern
from django.urls import path
from .views import formulario_comentario, formulario_publicacion, formulario_usuario, busqueda


urlpatterns = [
    path('Busqueda/', busqueda , name="Busqueda"),
    path('Formulario/', formulario_usuario, name="Formulario"),
    path('Publicaciones/', formulario_publicacion, name="Publicaciones"),
    path('Comentarios/', formulario_comentario, name="Comentarios"),
]
