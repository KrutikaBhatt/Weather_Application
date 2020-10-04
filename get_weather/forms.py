from django.forms import ModelForm,TextInput
from .models import CITY

class CityForm(ModelForm):
	class Meta:
		model =CITY
		fields= ['name']
		widgets={'name' :TextInput(attrs={'class':'input','placeholder':"Add City name"})}