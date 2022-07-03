from cProfile import label
from ctypes import resize
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ImageField, PasswordInput, Textarea
from clase.models import Posts

class NuestraCreacionUser(UserCreationForm):
    username = forms.CharField(label="Nombre de Usuario", required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre", required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name",'email', 'password1', 'password2']
        help_texts = { k: '' for k in fields }
        
class NuestraEdicionUser(forms.Form):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(label="Nombre", max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido", max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    more_info = forms.CharField(required=False,max_length=300, label="Biografia", widget=forms.Textarea(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
