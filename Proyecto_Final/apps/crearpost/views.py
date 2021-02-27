from django.shortcuts import render

def crearpost(request):
	ctx={
	}
	return render(request, "crearpost.html",ctx)
