from django.shortcuts import render, redirect
from apps.mascota.models import Mascota
from apps.mascota.views import get_first_number_found
from apps.postulante.models import Postulante


def confirmar_postulacion(request):

    context = {}

    if request.GET['mascota']:

        mascota = get_first_number_found(request.GET['mascota'])
        postulantes = Postulante.objects.filter(mascota=mascota)

        context = {'postulantes': postulantes,
                   'mascota': mascota}

    return render(request, 'publicacion/postularce.html', context)


def postularce(request):

    if request.GET['mascota']:

        mascota = Mascota.objects.filter(id_mascota=get_first_number_found(request.GET['mascota']))[0]

        postulante = Postulante(mascota=mascota, usuario_postulado=request.user)
        postulante.save()

    return redirect(to='ver_publicaciones')


def elegir_duenio(request):

    context = {}

    if request.GET['mascota']:

        mascota = get_first_number_found(request.GET['mascota'])
        postulantes = Postulante.objects.filter(mascota=mascota)

        context['postulantes'] = postulantes
        context['mascota'] = mascota

    return render(request, 'publicacion/elegir_duenio.html', context)


def hacer_duenio(request):

    if request.GET['postulante']:

        mascota = request.GET['mascota']
        postulante = get_first_number_found(request.GET['postulante'])

        Mascota.objects.filter(id_mascota=mascota).update(usuario_futuro_duenio=postulante)
        Mascota.objects.filter(id_mascota=mascota).update(estado=False)

    return redirect(to='ver_mis_publicaciones')
