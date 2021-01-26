from django.urls import path
from . import views #El punto indica que en esta misma carpeta accounts existe views
from django.contrib.auth import views as authview


urlpatterns = [
    path('', views.inicio, name='index'),
    path('registration/',views.registration, name='Register'),
    path('Login/',authview.LoginView.as_view(template_name='Accounts/inicioSesion.html'),name='Login'),
    path('Logout/',authview.LoginView.as_view(template_name='index.html'),name='Logout'),
    path('change-password/',authview.PasswordChangeView.as_view(template_name="Accounts/change_pass.html"),name='change-pass'),
    path('password-change-done/',authview.PasswordChangeDoneView.as_view(template_name="Accounts/inicioSesion.html"),name='password_change_done'),
    path('update-profile/',views.update, name="update-profile"),
    
]