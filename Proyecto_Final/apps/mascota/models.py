from django.db import models
from Proyecto_Final.apps.publicacion.models import Publicacion
from Proyecto_Final.apps.usuario.models import Usuario


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)

    foto = models.ImageField()
    publicacion = models.OneToOneField(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    especie = models.CharField(max_length=25, null=False)
    sexo_item = ('macho', 'hembra')
    sexo = models.CharField(max_length=30, blank=True, null=False, choices=sexo_item)
    raza = models.CharField(max_length=25, null=False)
    edad = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=100, null=False)
    futuro_duenio = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    estado = models.BooleanField(null=True)
