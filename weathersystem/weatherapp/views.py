from django.shortcuts import render
import requests
import time
import locale

# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'pravets'

    appid = '92847c220d324804d0a797bca465503e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric', 'lang':'bg'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    name = res['name']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']

    locale.setlocale(locale.LC_TIME, 'bg_BG')
    day = time.strftime(f"%a, %d %b %Y")

    return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon, 'temp':int(temp), 'day':day, 'name':name, 'humidity':humidity, 'wind':int(wind)})