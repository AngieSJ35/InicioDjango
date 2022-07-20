from django import forms
from Noticias.models import Noticia

class FormularioNoticia(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = '__all__'
