from django.urls import path
from apps.mascota import views


urlpatterns = [
    path('crear_mascota/', views.crear_mascota, name='crear_mascota'),
    path('ver_mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('ver_mis_mascotas/', views.ver_mis_mascotas, name='ver_mis_mascotas'),
]
