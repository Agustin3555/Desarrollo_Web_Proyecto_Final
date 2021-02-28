from django.http import HttpResponse
from django.template import loader


def publicaciones(request):

    template = loader.get_template("ver_publicaciones.html")

    context = {}

    return HttpResponse(template.render(context, request))
