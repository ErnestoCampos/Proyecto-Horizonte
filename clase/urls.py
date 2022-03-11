from django.urls import URLPattern
from django.urls import path
from .views import nuevo_curso

urlpatterns = [
    path('Curso/', nuevo_curso)
]
