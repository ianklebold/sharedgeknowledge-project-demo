from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('detalle/<titulo>/',login_required(views.mostrarDetalle), name="mostrarDetalle"),
    path('nuevo_post/',login_required(views.crear_post), name="crear_post"),

]