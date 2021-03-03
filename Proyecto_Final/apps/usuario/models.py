from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    sexo = models.CharField(max_length=30, blank=True, null=False, choices=('masculino', 'femenino', 'otro'))
    ciudad = models.CharField(max_length=50, null=False)
    descripcion_propia = models.CharField(max_length=500, null=True)
    promedio_calificacion = models.DecimalField(max_digits=2, decimal_places=2, null=True)
