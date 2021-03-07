from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.mascota.models import Mascota
from apps.publicacion.models import Publicacion


class Pet_Form(ModelForm):

    class Meta:
        model = Mascota
        fields = ['foto', 'sexo', 'raza', 'edad', 'descripcion']
        labels = {'foto': 'Foto',
                  'sexo': 'Sexo',
                  'raza': 'Raza',
                  'edad': 'Edad',
                  'descripcion': 'Descripción'}


def crear_mascota(request, n):

    form = Pet_Form()

    if request.method == 'POST':

        publicacion = Mascota(usuario_creador=request.user,
                              estado=True)

        form = Pet_Form(data=request.POST, instance=publicacion)

        if form.is_valid():

            form.save()
            return

        else:
            return render(request, 'publicacion/crear_publicacion.html', {'exception': 'Error'})  # Mensaje

    return render(request, 'publicacion/crear_publicacion.html', {'form': form})


# __________________ELIMINAR MASCOTA
# __________________EDICION DE DATOS DE MASCOTAS
# __________________LISTAR MASCOTAS
