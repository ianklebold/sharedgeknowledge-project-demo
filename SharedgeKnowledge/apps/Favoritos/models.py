from django.db import models
from SharedgeKnowledge.apps.Accounts.models import Profile
from django.contrib.auth.models import User
from SharedgeKnowledge.apps.Create_Post.models import Post
# Create your models here.

class Favorito(models.Model):
    id = models.AutoField(primary_key = True)
    referencia_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='favoritos')
    titulo = models.CharField('Titulo para post favorito',  max_length=100, null= False, blank=False)
    descripcion = models.CharField('Describe para que servirá este post', max_length=200, null= False, blank=False )

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

