from django.shortcuts import render
from SharedgeKnowledge.apps.Create_Post.models import Post
from .forms import RegistrationForm, UpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def inicioSesion(request):
    return render(request,'Accounts/inicioSesion.html')

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'Accounts/Perfil.html',{'user':user,'posts':posts})


def update(request):
    if request.method == 'POST':
        u_fm = UpdateForm(data=request.POST, instance=request.user)
        if u_fm.is_valid():
            u_fm.save()
            messages.success(request, 'Profile Update')
    else:
        u_fm = UpdateForm(instance=request.user)
    return render(request, 'Accounts/update-profile.html',{'u_fm':u_fm})

def registration(request):
    #El metodo POST se utilizado para mandar algun tipo de recurso al servidor y causar un impacto.
    #En este caso damos un POST para enviar el formulario de registro y guardarlo en la BD 
    if request.method == 'POST':
        fm= RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Registration Created Succesfully!!!')
        
    else:
        fm = RegistrationForm()
    return render(request,'Accounts/registrarse.html',{'fm':fm})
