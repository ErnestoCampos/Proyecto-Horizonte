from email.policy import default
from os import link
from tkinter.tix import Tree
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, default='assets\img\fondo.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    more_info = models.CharField(max_length=150, default="Escribe algo sobre ti")