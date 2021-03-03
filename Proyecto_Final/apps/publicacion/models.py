from django.db import models
from apps.usuario.models import Usuario


class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)

    usuario_publicista = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    fecha = models.DateField(null=False)
    descripcion = models.CharField(max_length=500, null=True)
    estado = models.BooleanField(null=False)
