from django import forms

class Formulario_Usuario(forms.Form):
    nombre = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)
    contraseña = forms.CharField(max_length=25)