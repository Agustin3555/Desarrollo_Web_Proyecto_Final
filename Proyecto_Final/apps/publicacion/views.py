from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.publicacion.models import Publicacion
from apps.mascota.views import crear_mascota


class Post_Form(ModelForm):

    class Meta:
        model = Publicacion
        fields = ['foto', 'descripcion', 'especie', 'cantidad_de_mascotas']
        labels = {'foto': 'Foto General',
                  'descripcion': 'Descripción General',
                  'especie': 'Especie',
                  'cantidad_de_mascotas': 'Número de Mascotas'}


def crear_publicacion(request):

    form = Post_Form()

    if request.method == 'POST':

        publicacion = Publicacion(usuario_creador=request.user,
                                  estado=True)

        form = Post_Form(data=request.POST, instance=publicacion)

        if form.is_valid():

            form.save()

            return redirect(to='home')

    return render(request, 'publicacion/crear_publicacion.html', {'form': form})


# __________________ELIMINAR PUBLICACION
# __________________LISTAR PUBLICACIONES
