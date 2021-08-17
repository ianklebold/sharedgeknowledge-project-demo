from django.shortcuts import render
from SharedgeKnowledge.apps.Create_Post.models import Post
from .models import Profile
from .forms import RegistrationForm, UpdateForm, UpdateImage
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

def profile_notas(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        notas = user.notas.all()
    else:
        notas = current_user.notas.all()
        user = current_user
    return render(request, 'Accounts/Perfil_Notas.html',{'user':user,'notas':notas})


def update(request):
    if request.method == 'POST':
        u_fm = UpdateForm(data=request.POST ,instance=request.user)
        i_fm = UpdateImage(data=request.POST, files=request.FILES  ,instance=request.user.profile)
        if u_fm.is_valid() and i_fm.is_valid():
            u_fm.save()
            i_fm.save()
            messages.success(request, 'Profile Update')
    else:
        u_fm = UpdateForm(instance=request.user)
        i_fm = UpdateImage(instance=request.user.profile)
    return render(request, 'Accounts/update-profile.html',{'u_fm':u_fm, 'i_fm':i_fm})

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
    return render(request,'Accounts/Registrarse.html',{'fm':fm})
