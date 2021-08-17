from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de categoria',  max_length=100, null= False, blank=False)
    fecha_creacion= models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self): 
        return self.nombre

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts') #
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE) #
    titulo = models.CharField('Titulo', max_length= 90, blank= False, null = False) #
    texto = models.CharField('Descripcion', max_length=280, blank=True, null=True)
    video = models.URLField('Enlace de Youtube',max_length = 400, blank=True, null=True)
    enlace_web = models.URLField('Enlace web',max_length = 400, blank=True, null=True)
    imagen = models.ImageField(upload_to="imagenes/",blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion',auto_now=False, auto_now_add = True) #
    archivo = models.FileField(upload_to="documentos/",blank=False,null=False) #

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
