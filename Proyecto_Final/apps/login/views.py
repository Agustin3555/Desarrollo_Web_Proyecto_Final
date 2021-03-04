from django.shortcuts import render


def entrar(request):

    context = {}

    return render(request, 'entrar.html', context)
