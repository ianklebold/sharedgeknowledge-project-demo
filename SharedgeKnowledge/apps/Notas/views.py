from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import formNota


def crear_nota(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = formNota(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.user = current_user
            nota.save()
            messages.success(request, 'Nota creada')
            return redirect('wall')
    else:
        form = formNota()

    return render(request, 'Notas/crear_nota.html', {'form':form})


def mostrar_nota(request, titulo):
    user =  request.user
    nota = Notas.objects.get(titulo=titulo)
    return render(request, 'Wall/detalle_nota.html', {'user':user, 'nota':nota})


def editar_nota(request, id_nota):
    nota = Notas.objects.get(id=id_nota)
    if request.method == 'GET':
        form = formNota(instance=nota)
    else:
        form = formNota(data=request.POST, instance = nota)
        if form.is_valid:
            form.save()
        return redirect('wall')
    return render(request, 'Notas/editar_nota.html', {'form': form})

def borrar_nota(request, id_nota):
    nota = Notas.objects.get(id=id_nota)
    if request.method == 'POST':
        nota.delete()
        return redirect('wall')
    return render(request, 'crear_post/delete_post.html', {'nota': nota})        