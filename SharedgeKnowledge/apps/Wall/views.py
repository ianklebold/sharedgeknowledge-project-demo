from django.shortcuts import render

def muro(request):
    return render(request,'Wall/muro_apuntes.html')