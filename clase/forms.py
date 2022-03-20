from tkinter import Widget
from unittest.util import _MAX_LENGTH
from django import forms

class Formulario_Usuario(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    contraseña = forms.CharField(max_length=40, widget=forms.PasswordInput)

class Formulario_Publicacion(forms.Form):
    Autor = forms.CharField(max_length=20)
    FechaDePublicacion = forms.DateTimeField(widget = forms.SelectDateWidget)

class Formulario_Comentario(forms.Form):
    Autor = forms.CharField(max_length=20)
    FechaDePublicacion = forms.DateTimeField(widget = forms.SelectDateWidget)

class Buscador(forms.Form):
    partial_nombre = forms.CharField(max_length=20)