from django.template.loader import get_template
from django.http import HttpResponse


class HomeViews():
	
	def home(self):
		plantilla = get_template('Noticias/HomeIndex.html')
		return HttpResponse(plantilla.render())


