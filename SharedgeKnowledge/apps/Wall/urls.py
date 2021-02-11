from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns=[
    path('feed/',login_required(views.muro), name="wall"),
    
]