from django.shortcuts import render
from apps.publicacion.models import Publicacion
from apps.mascota.models import Mascota


def ver_perfil(request):

    context = {'n_calificaciones': 0,
               'publicaciones_usuario': Publicacion.objects.filter(usuario_creador=request.user),
               'mascotas': Mascota.objects.all}

    return render(request, "usuario/ver_perfil.html", context)


# __________________DAR DE ALTA UN USUARIO
# __________________DAR DE BAJA UN USUARIO
# __________________LISTAR POSTULANTES
# __________________VISUALIZAR DENUNCIAS
# __________________VISUALIZAR PERFIL
