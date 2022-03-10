
from django.urls import URLPattern
from django.urls import path
from .views import Año , Plantilla

urlpatterns = [
    path('Año/<int:numero>', Año),
    path('Plantilla/', Plantilla),
]