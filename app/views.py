from django.shortcuts import render
import json
import requests

import pytz
from django.utils import timezone

# Create your views here.
def home(request):
    if request.method == "POST":
        city = request.POST.get('city')
        source = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={api_key}"
        list_of_data = requests.get(source.format(city)).json()

        temp_kelvin = list_of_data['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2) 

        data = {
            "country_code" : str(list_of_data['sys']['country']),
            
            "coordinate" : str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp" : temp_celsius,
            "humidity" : str((list_of_data['main']['humidity'])),
            "timezone": str(list_of_data['timezone']),
        }

    else:
        data = {}

    return render(request,"home.html",{"data":data})


