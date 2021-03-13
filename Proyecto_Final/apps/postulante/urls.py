from django.urls import path
from apps.postulante import views


urlpatterns = [
    path('confirmar_postulacion/', views.confirmar_postulacion, name='confirmar_postulacion'),
    path('postularce/', views.postularce, name='postularce'),
    path('elegir_duenio/', views.elegir_duenio, name='elegir_duenio'),
    path('hacer_duenio/', views.hacer_duenio, name='hacer_duenio'),
]
