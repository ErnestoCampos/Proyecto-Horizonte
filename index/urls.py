
from django.urls import URLPattern
from django.urls import path
from .views import Año , Plantilla, inicio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('Año/<int:numero>', Año),
    path('Plantilla/', Plantilla, name="plantilla")
]