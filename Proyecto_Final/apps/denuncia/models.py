from django.db import models
from apps.usuario.models import Usuario


class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)

    usuario_denunciante = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_denunciado = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateField(null=False)
    tipo = models.CharField(max_length=1, null=False)
    comentario = models.CharField(max_length=500, null=False)
    estado = models.BooleanField(null=True)
