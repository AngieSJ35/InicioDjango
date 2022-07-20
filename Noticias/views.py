from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

noticias = {"1" : ["a", 'descrpcion', 'autor'] , "2" : ["b", 'descrpcion', 'autor']}

class FormularioNoticiaView(HttpRequest):

	def index(request):
		return render(request,'Noticias/NoticiaIndex.html')

	"""def procesar_form(request):
		noticia = FormularioNoticia(request.POST)
		if noticia.is_valid():
			noticia.save()
			noticia = FormularioNoticia()
		return render(request,'NoticiaIndex.html', {'form' : noticia, 'mensaje' : 'ok' } )"""
def index(request):
	context = {'noticias' : noticias}
	return render(request, 'Noticias/Index.html', context = {"noticias" : noticias})

def crearNoticia(request):
	return render(request, "Noticias/crearnoticia.html")

def infoNoticia(request, nombreNoticia):
	context = {'name' : nombreNoticia}
	return render(request, 'Noticias/infoNoticia.html', context)

