from unittest.util import _MAX_LENGTH
from django import forms
from ckeditor.fields import RichTextFormField


class Formulario_Usuario(forms.Form):
    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contraseña = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class Formulario_Publicacion(forms.Form):
    autor = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_de_publicacion = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    descripcion = RichTextFormField(required=False) 

class Formulario_Comentario(forms.Form):
    autor = forms.CharField(max_length=20)
    fecha_de_publicacion = forms.DateTimeField(widget = forms.SelectDateWidget)

class Usuario_Busqueda(forms.Form):
    nombre = forms.CharField(max_length=20)

class Publicacion_Crear(forms.Form):
    autor = forms.CharField(max_length=20)
    fecha_de_publicacion = forms.DateTimeField(widget = forms.SelectDateWidget)
