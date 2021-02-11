from django.shortcuts import render, redirect, get_object_or_404
from .forms import formPost, UpdateForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


#Con esto accedemos al detalle de cada post
@login_required(login_url='Register')
def mostrarDetalle(request, titulo):
    publicaciones = Post.objects.get(titulo=titulo)
    return render(request, 'Wall/detalle_post.html',{'publicaciones':publicaciones})

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
        
