from unicodedata import name
from django import views
from django.urls import URLPattern
from django.urls import path
from . import views


urlpatterns = [
    path('Formulario/', views.formulario_usuario, name="Formulario"),
    path('Publicaciones/', views.formulario_publicacion, name="Publicaciones"),
    path('Comentarios/', views.formulario_comentario, name="Comentarios"), 
    path('usuarios/', views.lista_usuarios , name="lista_usuarios"),
    # CRUD publicaciones
    path('publicacion/listado', views.publicacion_listado, name="publicacion_listado"),
    path('publicacion/crear', views.crear_publicacion, name="crear_publicacion"),
    path('publicacion/borrar/<int:id>', views.borrar_publicacion, name="borrar_publicacion"),
    path('publicacion/leer', views.leer_publicacion, name="leer_publicacion"),
    path('publicacion/update/<int:id>', views.update_publicacion, name="update_publicacion"),
    # CRUD Usuarios CBV 
    path('usuario/list', views.ListaUsuarios.as_view(), name="usuario_list"),
]
