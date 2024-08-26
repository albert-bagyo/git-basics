from geopy.distance import great_circle
from geopy.geocoders import Nominatim


def get_cordinates_of(city):
    geolocator = Nominatim(user_agent="pyLocator")
    location = geolocator.geocode(city)
    
    return location.latitude, location.longitude

def get_distance(city_1, city_2):
    city_1_coord = get_cordinates_of(city_1)
    city_2_coord = get_cordinates_of(city_2)
    distance = great_circle(city_1_coord,city_2_coord)
    return distance

def get_cities():
    print("Enter two cities with a space in-between to find the distance between them.")
    city1, city2 = input(":: ").split()
    return city1, city2

def run():
    city1, city2 = get_cities()
    distance = get_distance(city1, city2)
    print(f"The distance between {city1} and {city2} is {round(distance.km,2)} km.")
    
run()