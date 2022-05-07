from datetime import datetime
from email.policy import default
from django.db import models
from django.forms import CharField
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.EmailField(max_length=40) 
    contraseña = models.CharField(max_length=25)
    registrado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"

class Posts(models.Model):
    descripcion = RichTextField(max_length=10000, default='Escribe Aqui', blank=True, null=True)
    imagen = models.ImageField(null=False, blank=False, upload_to="imagenes/", default=datetime.now)
    autor = models.CharField(max_length= 30)
    fecha_de_publicacion = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"Publicacion de {self.Autor}" 
    
class Comentario(models.Model):
    autor = models.CharField(max_length= 30)
    fecha_de_publicacion = models.DateTimeField()