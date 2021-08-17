from django import forms
from .models import Favorito


class FormFav(forms.ModelForm):
    class Meta:
        model = Favorito
        fields = ['titulo',
                'descripcion']
        