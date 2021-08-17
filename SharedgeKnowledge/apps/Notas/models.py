from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Notas(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='notas') #
    #Aqui tendremos que poner una relacion con el calendario, clave foranea (Una fecha puede tener muchas notas)
    titulo = models.CharField('Titulo', max_length= 90, blank= False, null = False) #
    texto = models.CharField('Descripcion', max_length=560, blank=False, null=False)
    enlace = models.URLField('Enlace web',max_length = 400, blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion',auto_now=False, auto_now_add = True)
    visible= models.BooleanField('Todos lo pueden ver/Solo yo la puedo ver', default=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return self.titulo