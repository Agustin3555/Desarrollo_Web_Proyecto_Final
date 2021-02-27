from django.http import HttpResponse
from django.template import loader


def test(request):

	template = loader.get_template("test.html")

	context = {"profesor": "hola"}

	return HttpResponse(template.render(context, request))
