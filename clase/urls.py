from unicodedata import name
from django import views
from django.urls import URLPattern
from django.urls import path
from . import views


urlpatterns = [
    # CRUD Usuarios CBV 
    path('posts/', views.ListaPosts.as_view(), name="posts_list"),
    path('posts/crear/', views.CrearPosts.as_view(), name="posts_crear"),
    path('posts/<int:pk>/', views.DetallePosts.as_view(), name="posts_detalle"),
    path('posts/<int:pk>/editar/', views.EditarPosts.as_view(), name="posts_editar"),
    path('posts/<int:pk>/borrar/', views.BorrarPosts.as_view(), name="posts_borrar"),
]
