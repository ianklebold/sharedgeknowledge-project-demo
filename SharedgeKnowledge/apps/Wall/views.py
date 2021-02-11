from django.shortcuts import render
from SharedgeKnowledge.apps.Create_Post.models import Post
from django.contrib.auth.decorators import login_required
#Con esto hacemos una peticion a la BD para mostrarnos los post creados

def muro(request):
    no_publicaciones = Post.objects.count()
    publicaciones = Post.objects.all()
    return render(request, 'Wall/muro_apuntes.html', {'publicaciones' : publicaciones, 'no_publicaciones':no_publicaciones})