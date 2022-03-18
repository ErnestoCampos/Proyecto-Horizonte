import email
from django import forms

class nuevo_usuario(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.CharField(max_length=40)
    contraseña = forms.CharField(max_length=30)