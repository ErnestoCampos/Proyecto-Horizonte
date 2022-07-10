from fileinput import FileInput
from unittest.util import _MAX_LENGTH
from django import forms
from ckeditor.fields import RichTextFormField
from clase.models import Posts


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

class Publicacion_Estilos(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Publicacion_Estilos, self).__init__(*args, **kwargs)
        self.fields['autor'].widget.attrs.update({'class' : 'form-control'})
        self.fields['fecha_de_publicacion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['imagen'].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Posts
        fields = ["autor","fecha_de_publicacion","descripcion","imagen"]