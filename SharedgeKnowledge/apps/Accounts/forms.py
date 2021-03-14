from django import forms #Importante para los formularios
from django.contrib.auth.models import User #Modelo de usuario, importante para el login
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
#A partir de UserCreationForm obtenemos el formulario para poder crear nuestra cuenta 

class RegistrationForm(UserCreationForm):
    #Formulario para registrar una cuenta
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'first_name',
                'last_name']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su usuario','title': 'Ingrese su usuario'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'Correo electronico','title': 'Correo electronico'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Ingrese su nombre','title': 'Ingrese su nombre'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Ingrese su apellido','title': 'Ingrese su apellido'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Ingrese su contraseña','title': 'Ingrese su contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder':'Repita su contraseña','title': 'Repita su contraseña'}))

class UpdateForm(forms.ModelForm):
    #Formulario para registrar una cuenta
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'first_name',
                'last_name',]

class UpdateImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'carrera',
            'estado',
        ]
