from django.db import models
from apps.publicacion.models import Publicacion
from apps.usuario.models import Usuario


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="+", null=True)
    foto = models.ImageField(upload_to='media', null=False)
    especie = models.CharField(max_length=25, null=False)
    sexo = models.CharField(max_length=30, blank=True, null=False, choices=(('macho', 'Macho'), ('hembra', 'Hembra')))
    raza = models.CharField(max_length=25, null=False)
    edad = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=100, null=False)
    usuario_duenio = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    estado = models.BooleanField(null=True)
