from django.db import models


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)

    nombre_cuenta = models.CharField(max_length=40, null=True) 
    email = models.EmailField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=30, null=False)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    descripcion_propia = models.CharField(max_length=500, null=True)
    promedio_calificacion = models.DecimalField(max_digits=2, decimal_places=2, null=True)
