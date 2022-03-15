from django.urls import URLPattern
from django.urls import path
from .views import nuevo_curso, formulario


urlpatterns = [
    path('Curso/', nuevo_curso),
    path('Formulario/', formulario, name="Formulario")
]
