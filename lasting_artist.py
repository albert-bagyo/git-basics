import requests
from pprint import pprint
from keys import LAST_FM
API_KEY = LAST_FM['API_KEY']



    print("Who is your favorite Artist?")
    artist = input(":: ")
    res = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist}&api_key={API_KEY}&format=json')
    print(res.json()['artist']['bio']['content'])

