from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Notas

class formNota(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['titulo', 'texto','enlace','visible']
        ordering = ['-fecha_creacion']
