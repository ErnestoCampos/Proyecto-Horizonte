from django.urls import URLPattern
from django.urls import path
from .views import formulario


urlpatterns = [
    path('Formulario/', formulario, name="Formulario")
]
