from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.publicacion.models import Publicacion
from apps.publicacion.models import Contador
from apps.mascota.models import Mascota


class Post_Form(ModelForm):

    class Meta:
        model = Publicacion
        fields = {'descripcion', 'foto', 'especie', 'cantidad_de_mascotas'}
        labels = {'descripcion': 'Descripción General'}


def crear_publicacion(request):

    if request.method == 'POST':

        publicacion = Publicacion(usuario_creador=request.user,
                                  estado=True)

        form = Post_Form(request.POST, request.FILES, instance=publicacion)

        if form.is_valid():

            form.save()

            contador = Contador.objects.create(publicacion=publicacion, i=request.POST['cantidad_de_mascotas'])
            contador.save()

            return redirect(to='crear_mascota')

    else:
        form = Post_Form()

    return render(request, 'publicacion/crear_publicacion.html', {'form': form})


def ver_publicaciones(request):

    context = {'publicaciones': Publicacion.objects.all,
               'mascotas': Mascota.objects.all}

    return render(request, 'publicacion/ver_publicaciones.html', context)


def filtrar_por_especie(request):

    if request.GET['prd']:

        especie = request.GET['prd']

        context = {'publicaciones': Publicacion.objects.filter(especie=especie),
                   'mascotas': Mascota.objects.all}

    return HttpResponse()


def filtrar_por_sexo(request):

    context = {'publicaciones': Publicacion.objects.all,
               'mascotas': Mascota.objects.all}

    return render(request, 'publicacion/ver_publicaciones.html', context)


# __________________ELIMINAR PUBLICACION
# __________________LISTAR PUBLICACIONES
