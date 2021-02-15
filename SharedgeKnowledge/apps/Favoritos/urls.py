from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('detalle/<int:id_post>/marcar_fav/', login_required(views.marcar_destacado), name="marcar_destacado"),
    path('favoritos/', login_required(views.listar_destacados), name="listar_destacados"),
    path('favoritos/<int:id_dest>/editar_destacado/', login_required(views.update_destacados), name="editar_destacado"),
    path('favoritos/<int:id_dest>/eliminar_destacado/',login_required(views.delete_destacado), name="eliminar_destacado"),
    
]