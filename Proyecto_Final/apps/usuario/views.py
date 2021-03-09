from django.shortcuts import render


def ver_perfil(request):

    context = {'n_calificaciones': 0}

    return render(request, "usuario/ver_perfil.html", context)


# __________________DAR DE ALTA UN USUARIO
# __________________DAR DE BAJA UN USUARIO
# __________________LISTAR POSTULANTES
# __________________VISUALIZAR DENUNCIAS
# __________________VISUALIZAR PERFIL
