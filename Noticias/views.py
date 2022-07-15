from django.shortcuts import render
from django.http import HttpResponse

noticias = {"1" : ["a", 'descrpcion', 'autor'] , "2" : ["b", 'descrpcion', 'autor']}

def index(request):
	context = {'noticias' : noticias}
	return render(request, 'Noticias/index.html', context = {"noticias" : noticias})

def crearNoticia(request):
	return render(request, "Noticias/crearnoticia.html")

def infoNoticia(request, nombreNoticia):
	context = {'name' : nombreNoticia}
	return render(request, 'Noticias/infoNoticia.html', context)

