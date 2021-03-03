from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from Proyecto_Final.apps.usuario.models import Usuario


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


def registro(request):
    context = {'formulario': CustomUserCreationForm}

    if request.method == 'POST':

        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")

            return redirect(to="home/")

        context['formulario'] = formulario

    template = loader.get_template("registrate.html")

    return HttpResponse(template.render(context, request))
