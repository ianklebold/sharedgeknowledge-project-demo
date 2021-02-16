from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('detalle_nota/<titulo>/',login_required(views.mostrar_nota), name="DetalleNota"),
    path('nuevo_nota/',login_required(views.crear_nota), name="crear_nota"),
    path('detalle_nota/<int:id_nota>/update_nota/',login_required(views.editar_nota), name="update_nota"),
    path('detalle_nota/<int:id_nota>/delete_nota/',login_required(views.borrar_nota), name="delete_nota"),
]