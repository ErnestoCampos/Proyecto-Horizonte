from django.db import models
from django.forms import CharField

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.EmailField(max_length=40) 
    contraseña = models.CharField(max_length=25)
    registrado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"

class Posts(models.Model):
    Autor = models.CharField(max_length= 30)
    FechaDePublicacion = models.DateTimeField()
 
    def __str__(self):
        return f"Publicacion de {self.Autor}" 
    
class Comentario(models.Model):
    Autor = models.CharField(max_length= 30)
    Mensaje = models.CharField(max_length= 100, default="Escribe tu mensaje")
    FechaDePublicacion = models.DateTimeField()