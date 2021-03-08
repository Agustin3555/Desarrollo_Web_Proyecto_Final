from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.publicacion.models import Publicacion
import datetime


class Post_Form(ModelForm):

    class Meta:
        model = Publicacion
        fields = {'descripcion', 'foto', 'especie', 'cantidad_de_mascotas'}
        labels = {'descripcion': 'Descripción General', }


def crear_publicacion(request):

    form = Post_Form()

    if request.method == 'POST':

        publicacion = Publicacion(usuario_creador=request.user,
                                  estado=True)

        form = Post_Form(data=request.POST, instance=publicacion)

        print(request.POST)

        if form.is_valid():

            form.save()
            return redirect(to='home')

        else:
            return render(request, 'publicacion/crear_publicacion.html', {'exception': 'Error'})

    return render(request, 'publicacion/crear_publicacion.html', {'form': form})


# __________________ELIMINAR PUBLICACION
# __________________LISTAR PUBLICACIONES
