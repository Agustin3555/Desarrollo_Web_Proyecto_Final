from django.db import models
#from apps.mascota.models import Mascota
from apps.usuario.models import Usuario

# Create your models here.
class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)

    publicista = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="+", null=False)
    #mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateField(null=False)
    descripcion = models.CharField(max_length=500, null=True)
    estado = models.BooleanField(null=False)