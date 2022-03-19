from unittest.util import _MAX_LENGTH
from django import forms

class Formulario_Usuario(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    contraseña = forms.CharField(max_length=40, widget=forms.PasswordInput)