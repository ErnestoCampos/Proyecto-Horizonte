from cProfile import label
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ImageField, PasswordInput, Textarea
from clase.models import Posts

class NuestraCreacionUser(UserCreationForm):
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name",'email', 'password1', 'password2']
        help_texts = { k: '' for k in fields }
        
class NuestraEdicionUser(forms.Form):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(), required=False)
    first_name = forms.CharField(label="Nombre", max_length=20, required=False)
    last_name = forms.CharField(label="Apellido", max_length=20, required=False)
    link = forms.URLField(required=False)
    more_info = forms.CharField(required=False,max_length=300, label="Biografia")
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Posts
        fields=('email','password1','password2','first_name','last_name','link','more_info','imagen')

    widget={
        'email': forms.TextInput(attrs={'class':'form-control'}),
        'password1': forms.PasswordInput(attrs={'class':'form-control'}),
        'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        'link': forms.TextInput(attrs={'class':'form-control'}),
        'more_info': forms.Textarea(attrs={'class':'form-control'}),
        'imagen': forms.ImageField(attrs={'class':'form-control'})
        }