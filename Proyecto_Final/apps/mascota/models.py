from django.db import models
from apps.usuario.models import Usuario
from apps.publicacion.models import Publicacion
# Create your models here.
class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)

    publicacion = models.OneToOneField(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    especie = models.CharField(max_length=25, null=False)
    sexo = (
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
        )
    sexo = models.CharField(max_length=30, blank=True, null=False, choices=sexo)
    raza = models.CharField(max_length=25, null=False)
    edad = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=100, null=False)
    futuro_duenio = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    estado = models.BooleanField(null=True)