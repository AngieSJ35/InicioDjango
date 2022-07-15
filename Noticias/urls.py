from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='hola'),
	path('crearnoticia.html/', views.crearNoticia, name='CrearNoticia'),
	path('infoNoticia/<str:nombreNoticia>/', views.infoNoticia, name='infoNoticia'),
]