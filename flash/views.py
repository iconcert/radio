from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import List, Services
from .forms import Users, Autorization

def index(request):
	template = loader.get_template('flash/index.html')
	lls = List.objects.order_by('title')
	context = {'lls': lls}
	return HttpResponse(template.render(context, request))

def information(request):
	return render(request, 'flash/information.html')

def menu(request):
	return render(request, 'flash/menu.html')

def registration(request):
	if request.method == "POST":
		users = Users(request.POST)
		if users.is_valid():
			username = users.cleaned_data["username"]
			password = users.cleaned_data["password"]
			email = users.cleaned_data["email"]
			firstname = users.cleaned_data["firstname"]
			lastname = users.cleaned_data["lastname"]
			return HttpResponse("<h2>Hello, {0}<h2>".format(username))
		else:
			return HttpResponse("Invalid data")
	else:
	    users = Users()
	    return render(request, 'flash/registration.html', {"form": users})

def autorization(request):
	if request.method == "POST":
		autorization = Autorization(request.POST)
		if autorization.is_valid():
			username = autorization.cleaned_data["username"]
			password = autorization.cleaned_data["password"]
			return HttpResponse("<h1>Успешно<h1>")
		else:
			return HttpResponse("Invalid data")
	else:
	    autorization = Autorization()
	    return render(request, 'flash/autorization.html', {"form": autorization})

def police(request):
	return render(request, 'flash/police.html')

def regulations(request):
	return render(request, 'flash/regulations.html')

def services(request):
	template = loader.get_template('flash/services.html')
	lls = Services.objects.order_by('title')
	context = {'lls': lls}
	return HttpResponse(template.render(context, request))

def sitemap(request):
	return render(request, 'flash/sitemap.html')