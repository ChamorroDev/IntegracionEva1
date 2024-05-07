from django.shortcuts import render
from tienda.models import Disco 
import requests

def home(request):
    all_discos=Disco.objects.filter(oferta=True)[:9]
 
    return render(request,"home.html",{"discos":all_discos})





def weather(request):
    api_key="oW3o4geoIFyojrJ6HAF6TPnkfSVqG7PE"
    root_url = 'http://dataservice.accuweather.com/currentconditions/v1/60449?'
    city = 'Santiago'
    ##url=f"{root_url}apikey={api_key}&q={city}"
    ## http://dataservice.accuweather.com/currentconditions/v1/60449?apikey=oW3o4geoIFyojrJ6HAF6TPnkfSVqG7PE&language=es
    url=f"{root_url}apikey={api_key}&language=es"

    city_weather = requests.get(url.format(city)).json() 
    city_weather=city_weather[0]
    print(city_weather)

    weather_icon = city_weather['WeatherIcon']
    if len(str(weather_icon)) < 2:
        weather_icon = '0' + str(weather_icon)
    
    url_iconweather = f'https://developer.accuweather.com/sites/default/files/{weather_icon}-s.png'


    
    contexto = {
            'ciudad':city,
            'temperatura': city_weather['Temperature']['Metric']['Value'],
            'WeatherText': city_weather['WeatherText'],
            'iconweather':url_iconweather

        }
    return render(request, 'weather.html',contexto)
