import requests
from django.shortcuts import render ,redirect
from .models import CITY
from .forms import CityForm


# API format : By city name =api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def index(request):

	mesg=""
	mesg_class=""
	err=""


	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=Your_API_Key'

	

	if request.method=='POST':
		form=CityForm(request.POST)

		if form.is_valid():
			new_city=form.cleaned_data['name']
			count=CITY.objects.filter(name=new_city).count()

			if count==0:
				req=requests.get(url.format(new_city)).json()

				if(req['cod']==200):
					form.save()
				else:
					err="City do not Exist"
				
			else:
				err='City already Added! '
	if err:
		mesg=err
		mesg_class='is-danger'
	else:
		mesg ="City added successfully"
		mesg_class='is-success'

	form=CityForm()
	cities=CITY.objects.all()
	city_data=[]
	

	for city_name in cities:

		req=requests.get(url.format(city_name)).json()
		

		city_weather={
		'city':city_name.name,
    	'temperature': req['main']['temp'],
    	'description' : req['weather'][0]['description'],
    	'icon' : req['weather'][0]['icon'],
		}

		city_data.append(city_weather)




	#Convert to json 
	#req=requests.get(url.format(city)).json()

	#Create a dictionery to be displayed on the App
	# Lets refer what the req gives =
	#{"coord":{"lon":72.97,"lat":19.2},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50d"}],
	#"base":"stations","main":{"temp":29,"feels_like":33.59,"temp_min":29,"temp_max":29,"pressure":1009,"humidity":79},
	#"visibility":2200,"wind":{"speed":2.6,"deg":270},"clouds":{"all":75},"dt":1601801197,
	#"sys":{"type":1,"id":9052,"country":"IN","sunrise":1601773162,"sunset":1601816040},"timezone":19800,"id":1254661,"name":"Thāne","cod":200}
	
    # To get all the cities added in database
    
   

	#Pass the dictionery we made in city_weather
	content = {
	'city_data':city_data[::-1],
	'form':form,
	'message':mesg,
	'mesg_class' :mesg_class
	}
	return render(request,'get_weather/Base.html',content)

def delete_city(request,CityName):
	CITY.objects.get(name=CityName).delete()
	return redirect('home')
