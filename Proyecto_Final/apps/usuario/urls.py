from django.urls import path
from apps.usuario import views


urlpatterns = [
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
]
