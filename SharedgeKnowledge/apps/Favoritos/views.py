from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from SharedgeKnowledge.apps.Create_Post.models import Post
from .forms import FormFav
from .models import Favorito

def marcar_destacado(request, id_post):
    current_post = Post.objects.get(id=id_post)
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = FormFav(request.POST)
        if form.is_valid():
            destacado= form.save(commit=False)
            destacado.user = current_user
            destacado.referencia_post = current_post
            destacado.save()
            return redirect('wall')
    else:
        form = FormFav()
    return render(request, 'Favoritos/marcar_favorito.html', {'form':form, 'referencia':current_post})    


def listar_destacados(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        post_destacados = user.favoritos.all()
    else:
        post_destacados =  current_user.favoritos.all()
        user = current_user
    return render(request, 'Favoritos/favoritos_post.html', {'user':user, 'destacados':post_destacados} )

def update_destacados(request, id_dest):
    destacado = Favorito.objects.get(id=id_dest)
    referencia_post = destacado.referencia_post
    if request.method == 'GET' :
        form = FormFav(instance=destacado)
    else:
        form = FormFav(data=request.POST, instance = destacado)
        if form.is_valid:
            form.user = request.user
            form.referencia_post = referencia_post
            form.save()
        return redirect('wall')
    return render(request, 'Favoritos/editar_favorito.html', {'form': form , 'destacado': destacado})


def delete_destacado(request, id_dest):
    destacado = Favorito.objects.get(id=id_dest)
    if request.method == 'POST':
        destacado.delete()
        return redirect('wall')
    return render(request, 'Favoritos/delete_favorito.html', {'destacado': destacado})

