from django import forms
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class formPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['categoria', 'titulo', 'texto', 'video', 'enlace_web','imagen','archivo']
        ordering = ['-fecha_creacion']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto', 'video', 'enlace_web','imagen','archivo']