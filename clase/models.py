from django.db import models
from django.forms import CharField
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.EmailField(max_length=40) 
    contraseña = models.CharField(max_length=25)
    registrado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"

class Posts(models.Model):
    Descripcion = models.TextField(max_length=340, default='Escribe Aqui')
    Imagen = models.ImageField(null=False, blank=False, upload_to="imagenes/")
    Autor = models.CharField(max_length= 30)
    FechaDePublicacion = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"Publicacion de {self.Autor}" 
    
class Comentario(models.Model):
    Autor = models.CharField(max_length= 30)
    FechaDePublicacion = models.DateTimeField()