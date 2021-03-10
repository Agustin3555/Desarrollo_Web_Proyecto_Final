from django.urls import path
from apps.publicacion import views


urlpatterns = [
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('ver_publicaciones/', views.ver_publicaciones, name='ver_publicaciones'),
]
