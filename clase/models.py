from django.db import models
from django.forms import CharField

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.EmailField(max_length=40) 
    contraseña = models.CharField(max_length=25)
    registrado = models.BooleanField()

class Posts(models.Model):
    Autor = models.CharField(max_length= 30)
    FechaDePublicacion = models.DateTimeField()
    
class Comentario(models.Model):
    Autor = models.CharField(max_length= 30)
    FechaDePublicacion = models.DateTimeField()