from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='img_profile/',default='batman.png')
    carrera = models.CharField('Estudio la carrera',max_length= 90, blank= False, null = False, default='Carrera sin especificar')
    estado = models.CharField('Mi estado es',max_length= 100, blank= False, null = False, default='Bienvenido a mi perfil')
    joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Perfil : {self.user.username}'
