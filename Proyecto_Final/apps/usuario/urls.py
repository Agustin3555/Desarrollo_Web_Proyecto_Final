from django.urls import path
from apps.usuario import views


urlpatterns = [
    path('ver_perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil')
]
