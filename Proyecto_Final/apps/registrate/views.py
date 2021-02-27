from django.shortcuts import render


def registrate(request):
	ctx = {
	}
	return render(request, "registrate.html", ctx)
