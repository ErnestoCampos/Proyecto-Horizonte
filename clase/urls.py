from django.urls import URLPattern
from django.urls import path
from .views import formulario_publicacion, formulario_usuario, busqueda


urlpatterns = [
    path('Busqueda/', busqueda , name="Busqueda"),
    path('Formulario/', formulario_usuario, name="Formulario"),
    path('Publicaciones/', formulario_publicacion, name="Publicaciones"),
]
