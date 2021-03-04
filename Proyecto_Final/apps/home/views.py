from django.shortcuts import render

'''def index(request):
	template = loader.get_template("index.html")
	context = {}
	return HttpResponse(template.render(context,request))
'''

def index(request):

    context = {}

    return render(request, "index.html", context)
