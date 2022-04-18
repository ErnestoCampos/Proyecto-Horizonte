from unicodedata import name
from django.urls import URLPattern
from django.urls import path
from .views import login_proyecto, register_proyecto, editar_user, info_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_proyecto , name="login"),
    path("register", register_proyecto, name="register"),
    path('logout/', LogoutView.as_view(template_name="index/index.html") , name="logout"),
    path("editar/", editar_user, name="EditarPerfil"),
    path("datos/", info_user, name="InfoUsuario")
]