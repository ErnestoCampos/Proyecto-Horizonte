from django.db import models
from django.forms import CharField

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    profesion = models.CharField(max_length=15)


class Curso(models.Model):
    nombre = models.CharField(max_length=15)
    camada = models.IntegerField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=15)
    FechaDeEntrega = models.DateTimeField(max_length=15)
    entregado = models.BooleanField()

# class Usuario(models.Model):
#     nombre = models.CharField(max_length=15)
#     email = models.EmailField(max_length=40) 
#     contraseña = models.CharField(max_length=25)
#     registrado = models.BooleanField()

# class Posts(models.Model):
#     Autor = models.CharField(max_length= 30)
#     FechaDePublicacion = models.DateTimeField()
    
    

    