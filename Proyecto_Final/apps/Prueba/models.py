from django.db import models


class Usuarios(models.Model):  # ————————————————————————————————————————————————————————————————————————————— USUARIOS
    usuario_id = models.AutoField(primary_key=True)

    email = models.EmailField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=30, null=False)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    descripcion_propia = models.CharField(max_length=500, null=True)
    promedio_calificacion = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    publicaciones = models.ForeignKey("Publicaciones", on_delete=models.CASCADE, related_name="+", null=True)
    denuncias = models.ForeignKey("Denuncias", on_delete=models.CASCADE, related_name="+", null=True)


class Denuncias(models.Model):  # ——————————————————————————————————————————————————————————————————————————— DENUNCIAS
    id_denuncias = models.AutoField(primary_key=True)

    primer_nodo = models.ForeignKey("Nodo_Denuncia", on_delete=models.CASCADE, related_name="+", null=False)
    ultimo_nodo = models.ForeignKey("Nodo_Denuncia", on_delete=models.CASCADE, related_name="+", null=False)
    cantidad = models.IntegerField(null=False)


class Nodo_Denuncia(models.Model):
    id_nodo_denuncia = models.AutoField(primary_key=True)

    nodo_anterior = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=True)
    datos = models.ForeignKey("Datos_Denuncia", on_delete=models.CASCADE, related_name="+", null=True)
    nodo_siguiente = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=False)


class Datos_Denuncia(models.Model):
    id_datos_denuncia = models.AutoField(primary_key=True)

    usuario_denunciado = models.ForeignKey("Usuarios", on_delete=models.CASCADE, related_name="+", null=False)
    fecha = models.DateField(null=False)
    tipo = models.CharField(max_length=1, null=False)
    comentario = models.CharField(max_length=500, null=False)
    estado = models.BooleanField(null=False)


class Publicaciones(models.Model):  # ——————————————————————————————————————————————————————————————————— PUBLICACIONES
    id_publicaciones = models.AutoField(primary_key=True)

    primer_nodo = models.ForeignKey("Nodo_Publicacion", on_delete=models.CASCADE, related_name="+", null=False)
    ultimo_nodo = models.ForeignKey("Nodo_Publicacion", on_delete=models.CASCADE, related_name="+", null=False)
    cantidad = models.IntegerField(null=False)


class Nodo_Publicacion(models.Model):
    id_nodo_publicacion = models.AutoField(primary_key=True)

    nodo_anterior = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=True)
    datos = models.ForeignKey("Datos_Publicacion", on_delete=models.CASCADE, related_name="+", null=True)
    nodo_siguiente = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=False)


class Datos_Publicacion(models.Model):
    id_datos_publicacion = models.AutoField(primary_key=True)

    mascotas = models.ForeignKey("Mascotas", on_delete=models.CASCADE, related_name="+", null=True)
    fecha = models.DateField(null=False)
    descripcion = models.CharField(max_length=500, null=True)
    estado = models.BooleanField(null=False)


class Mascotas(models.Model):  # ————————————————————————————————————————————————————————————————————————————— MASCOTAS
    id_mascotas = models.AutoField(primary_key=True)

    primer_nodo = models.ForeignKey("Nodo_Mascota", on_delete=models.CASCADE, related_name="+", null=False)
    ultimo_nodo = models.ForeignKey("Nodo_Mascota", on_delete=models.CASCADE, related_name="+", null=False)
    cantidad = models.IntegerField(null=False)


class Nodo_Mascota(models.Model):
    id_nodo_mascota = models.AutoField(primary_key=True)

    nodo_anterior = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=True)
    datos = models.ForeignKey("Datos_Mascota", on_delete=models.CASCADE, related_name="+", null=True)
    nodo_siguiente = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=False)


class Datos_Mascota(models.Model):
    id_datos_mascota = models.AutoField(primary_key=True)

    sexo = models.BooleanField(null=False)
    especie = models.CharField(max_length=25, null=False)
    raza = models.CharField(max_length=25, null=False)
    edad = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=100, null=False)
    postulantes = models.ForeignKey("Postulantes", on_delete=models.CASCADE, related_name="+", null=False)
    futuro_duenio = models.ForeignKey("Usuarios", on_delete=models.CASCADE, related_name="+", null=True)


class Postulantes(models.Model):  # ———————————————————————————————————————————————————————————————————————— POSTULANTES
    id_postulantes = models.AutoField(primary_key=True)

    primer_nodo = models.ForeignKey("Nodo_Postulante", on_delete=models.CASCADE, related_name="+", null=False)
    ultimo_nodo = models.ForeignKey("Nodo_Postulante", on_delete=models.CASCADE, related_name="+", null=False)
    cantidad = models.IntegerField(null=False)


class Nodo_Postulante(models.Model):
    id_nodo_postulante = models.AutoField(primary_key=True)

    nodo_anterior = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=True)
    datos = models.ForeignKey("Datos_Postulante", on_delete=models.CASCADE, related_name="+", null=True)
    nodo_siguiente = models.ForeignKey("self", on_delete=models.CASCADE, related_name="+", null=False)


class Datos_Postulante(models.Model):
    id_datos_postulante = models.AutoField(primary_key=True)

    usuario_postulado = models.ForeignKey("Usuarios", on_delete=models.CASCADE, related_name="+", null=False)
    fecha = models.DateField(null=False)
    comentario = models.CharField(max_length=250, null=True)
