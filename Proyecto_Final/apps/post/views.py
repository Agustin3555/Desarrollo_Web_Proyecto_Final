from django.shortcuts import render

def test(request):
	ctx={
	}
	return render(request, "test.html",ctx)
