from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import List

def index(request):
	template = loader.get_template('flash/index.html')
	lls = List.objects.order_by('-published')
	context = {'lls': lls}
	return HttpResponse(template.render(context, request))

def information(request):
	return render(request, 'flash/information.html')

def menu(request):
	return render(request, 'flash/menu.html')

def police(request):
	return render(request, 'flash/police.html')

def regulations(request):
	return render(request, 'flash/regulations.html')

def services(request):
	return render(request, 'flash/services.html')

def sitemap(request):
	return render(request, 'flash/sitemap.html')