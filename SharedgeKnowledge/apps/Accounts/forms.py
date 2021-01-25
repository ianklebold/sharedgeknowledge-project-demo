from django import forms #Importante para los formularios
from django.contrib.auth.models import User #Modelo de usuario, importante para el login
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
