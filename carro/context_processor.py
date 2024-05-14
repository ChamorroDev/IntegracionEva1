import requests
from .carro import Carro


def importe_total_carro(request):
    carro = Carro(request)

    total=0
    if request.user.is_authenticated:
   
        for key,value in request.session["carro"].items():
            total=total+(float(value["precio"]))      
            
    else:
       total="Debes hacer login"
    return {"importe_total_carro":total}


def obtener_clima(request):
    api_key = "oW3o4geoIFyojrJ6HAF6TPnkfSVqG7PE"
    root_url = "http://dataservice.accuweather.com/currentconditions/v1/60449?"
    city = "Santiago"
    url = f"{root_url}apikey={api_key}&language=es"

    #city_weather = requests.get(url.format(city)).json() 



    ##city_weather = city_weather[0]
    city_weather = 1


    ##weather_icon = city_weather['WeatherIcon']
    ##if len(str(weather_icon)) < 2:
     ##   weather_icon = '0' + str(weather_icon)

    ##url_iconweather = f'https://developer.accuweather.com/sites/default/files/{weather_icon}-s.png'
    url_iconweather = f'https://developer.accuweather.com/sites/default/files/09-s.png'

    return {
        'clima': {
            """
            'ciudad': city,
            'temperatura': city_weather['Temperature']['Metric']['Value'],
            'WeatherText': city_weather['WeatherText'],
            'iconweather': url_iconweather,
            """
            'ciudad': 'Santiago',
            'temperatura': 3,
            'WeatherText': 'Nublado',
            'iconweather': url_iconweather
            
        }
    }
