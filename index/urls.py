
from django.urls import URLPattern
from django.urls import path
from .views import Log_In, Registro, Año , Plantilla, formulario, inicio, publicaciones, sobre_mi

urlpatterns = [
    path('', inicio, name="inicio"),
    path('Año/<int:numero>', Año),
    path('Plantilla/', Plantilla, name="plantilla"),
    path('About/', sobre_mi, name="About"),
    path('Publicaciones/', publicaciones, name="Publicaciones"),
    path('Inicia-Sesion/', Log_In, name="Log_In"),
    path('Registro/', Registro, name="Registro"),
    path('Formulario/', formulario, name="Formulario")
]