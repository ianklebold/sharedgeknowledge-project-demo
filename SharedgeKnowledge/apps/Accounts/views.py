from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.

def inicio(request):
    return render(request,'index.html')

def muro_aux(request): #ELIMINAR CUANDO SE CREE LA APP WALL
    return render(request,'Wall/muro_apuntes.html')

def inicioSesion(request):
    return render(request,'Accounts/inicioSesion.html')

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
