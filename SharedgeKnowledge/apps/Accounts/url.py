from django.urls import path
from . import views #El punto indica que en esta misma carpeta accounts existe views
from django.contrib.auth import views as authview


urlpatterns = [
    path('registration/',views.registration, name='Register'),
    path('Login/',authview.LoginView.as_view(template_name='Accounts/inicioSesion.html'),name='Login'),
    path('Logout/',authview.LoginView.as_view(template_name='index.html'),name='Logout'),
    path('aux/',views.muro_aux,name='aux'), #ELIMINAR CUANDO SE CREE LA APP WALL
    path('', views.inicio, name='index'),
]