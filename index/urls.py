
from unicodedata import name
from django.urls import path
from .views import Año , inicio, sobre_mi

urlpatterns = [
    path('', inicio, name="inicio"),
    path('Año/<int:numero>', Año),
    path('About/', sobre_mi, name="About"),
]