from django.db import models

class Noticia(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=500)
	autor = models.CharField(max_length=50)
