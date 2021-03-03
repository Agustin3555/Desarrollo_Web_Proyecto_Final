from django.db import models
from Proyecto_Final.apps.mascota.models import Mascota
from Proyecto_Final.apps.usuario.models import Usuario


class Correo(models.Model):
    id_correo = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="+", null=False)
    futuro_duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    estado = models.BooleanField(null=False)


class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True)

    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, related_name="+", null=False)
    usuario_emisor = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    mensaje = models.CharField(max_length=250, null=True)
    fecha = models.DateField(null=False)
