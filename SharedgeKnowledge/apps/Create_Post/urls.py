from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('detalle_post/<titulo>/',login_required(views.mostrarDetalle), name="mostrarDetalle"),
    path('nuevo_post/',login_required(views.crear_post), name="crear_post"),
    path('detalle_post/<int:id_post>/update_post/',login_required(views.update_post), name="update_post"),
    path('detalle_post/<int:id_post>/delete_post/',login_required(views.delete_post), name="delete_post"),
]