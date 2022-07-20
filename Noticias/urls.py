from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='hola'),
	
	path('registrarnoticia/', views.FormularioNoticiaView.index, name = 'prueba1' ),
	
]