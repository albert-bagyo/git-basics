'''
import pyowm


API_KEY = 'af741857faad262ab41a90507fbc95a5'
owm = pyowm.OWM(f"{API_KEY}")
m = owm.weather_manager()

def get_weather_at(place):
    observation = m.weather_at_place(place)
    return observation.weather


def print_weather_at(place):
    w = get_weather_at(place)
    wind = w.wind()
    humidity = w.humidity
    print(f"Location: ({place})\tWind speed: {wind['speed']}\tHumidity: {humidity}")

print_weather_at('Hong Kong,China')
print_weather_at('Tokyo, Japan')
print_weather_at('Koforidua,Ghana')

'''
from pprint import pprint
import requests

APIKEY = 'af741857faad262ab41a90507fbc95a5'

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
pprint(r.json())

