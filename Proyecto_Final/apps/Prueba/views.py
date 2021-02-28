from django.http import HttpResponse
from django.template import loader
from .models import Usuarios


def hola(request):
    """
    u = Usuarios(
        email="Agustin3555@hotmail.com",
        contrasenia="tabebulla12",
        nombres="Juan Agustín",
        apellidos="Lovera",
        ciudad="Resistencia",
        descripcion_propia="Yo",
        promedio_calificacion=None,
        publicaciones=None,
        denuncias=None
    )

    u.save()
    """

    u = Usuarios.objects.get(usuario_id=1)

    template = loader.get_template("ver_publicaciones.html")

    context = {"usuario": u.ciudad}

    return HttpResponse(template.render(context, request))
