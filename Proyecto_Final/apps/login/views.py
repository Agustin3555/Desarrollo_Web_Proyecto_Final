from django.shortcuts import render


def entrar(request):

    context = {}

    render(request, 'entrar.html', context)
