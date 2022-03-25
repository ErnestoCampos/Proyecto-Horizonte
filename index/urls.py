
from django.urls import URLPattern
from django.urls import path
from .views import Registro, Año , inicio, sobre_mi

urlpatterns = [
    path('', inicio, name="inicio"),
    path('Año/<int:numero>', Año),
    path('About/', sobre_mi, name="About"),
    path('Registro/', Registro, name="Registro"),
]