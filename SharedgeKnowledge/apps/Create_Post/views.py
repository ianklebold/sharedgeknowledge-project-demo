from django.shortcuts import render, redirect, get_object_or_404
from .forms import formPost
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


#Con esto accedemos al detalle de cada post
@login_required(login_url='Register')
def mostrarDetalle(request, titulo):
    user = request.user #Hacemos una request del usuario logueado actualmente
    publicaciones = Post.objects.get(titulo=titulo)
    return render(request, 'Wall/detalle_post.html',{'publicaciones':publicaciones, 'user':user})

def crear_post(request):
    #Encontramos el usuario logueado para asignarle el post
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = formPost(request.POST, request.FILES or None)
        if form.is_valid():
            post= form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('wall')
    else:
        form = formPost()
    return render(request, 'crear_post/crear_post.html', {'form':form})

def update_post(request, id_post):
    post = Post.objects.get(id=id_post)
    if request.method == 'GET':
        form = formPost(instance=post)
    else: 
        form = formPost(data=request.POST, files=request.FILES , instance = post)
        if form.is_valid:
            form.save()
        return redirect('wall')
    return render(request, 'crear_post/editar_post.html', {'form': form})


def delete_post(request, id_post):
    post = Post.objects.get(id=id_post)
    if request.method == 'POST':
        post.delete()
        return redirect('wall')    
    return render(request, 'crear_post/delete_post.html', {'post': post})