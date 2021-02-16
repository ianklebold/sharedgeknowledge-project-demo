from django.shortcuts import render
from SharedgeKnowledge.apps.Create_Post.models import Post, Categoria
from SharedgeKnowledge.apps.Notas.models import Notas
from django.contrib.auth.decorators import login_required
from django.db.models import Q
#Con esto hacemos una peticion a la BD para mostrarnos los post creados

def muro(request):

    #Este es el motor de busqueda

    queryset = request.GET.get("buscar")  #Guardamos en la variable queryset todo lo que se guarde en el buscador con palabra clave buscar
    publicaciones = Post.objects.all() #Traemos todos los post
    if queryset: #Si se escribió en el buscador se pasa a lo siguiente
        publicaciones = Post.objects.filter( #Filtramos las publicaciones segun su titulo o categoria
            Q(titulo__icontains = queryset) | Q(categoria__nombre = queryset)
        ).distinct() #Distrinct para que traiga a ambos en caso de repetir
        #ATENCION! categoria es una clave foranea. Se la representa por un nombre. por eso se pone categoria__nombre(palabra de definicion)
        #icontanins es para que traiga parecidos no exactamente iguales
        
    return render(request, 'Wall/muro_apuntes.html', {'publicaciones' : publicaciones})

def muro_notas(request):

    queryset = request.GET.get("buscar")
    notas = Notas.objects.filter(visible = True)
    if queryset: 
        publicaciones = Post.objects.filter( 
            Q(titulo__icontains = queryset) | Q(categoria__nombre = queryset)
        ).distinct() 
        notas = Notas.objects.filter( Q(titulo__icontains = queryset) )
        
        
    return render(request, 'Wall/muro_notas.html', {'notas':notas})

