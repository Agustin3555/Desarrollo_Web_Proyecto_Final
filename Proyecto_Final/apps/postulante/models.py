from django.db import models
from apps.mascota.models import Mascota
from apps.usuario.models import Usuario


class Postulante(models.Model):
    id_postulante = models.AutoField(primary_key=True)

    mascota_postulado = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="+", null=True)
    usuario_p = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateField(null=False)
    comentario = models.CharField(max_length=250, null=True)
