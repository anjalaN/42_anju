#!/usr/bin/env python3
import requests
#from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim

# Replace with your actual OpenWeatherMap API key
API_KEY = "50f2d4f0f4c194842ed69e0673908e81"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Fonction pour obtenir la latitude et la longitude d'une ville
def get_location(city_name):
    geolocator = Nominatim(user_agent="weatherApp")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude

    else:
        print("Ville introuvable")
        return None, None

# Demander à l'utilisateur une ville
city_name = input("Location?: ")

# Obtenir la latitude et la longitude de la ville
latitude, longitude = get_location(city_name)

if latitude and longitude:
    # Construire l'URL de la requête avec les coordonnées
    url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang=fr"
    
    # Effectuer la requête
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Afficher les données météorologiques
        print(f"The current weather in {city_name} is:")
        print(f"- Temperature (C): {data['main']['temp']}")
        print(f"- Humidity: {data['main']['humidity']}%")
        print(f"- Cloud: {data['clouds']['all']}%")
        print(f"- Wind: {data['wind']['speed'] * 3.6:.2f} km/h")  # Conversion de m/s en km/h
    else:
        print(f"Error: Unable to fetch data (Code: {response.status_code})")
        print(f"Message: {response.json()['message']}")
else:
    print("Invalid city, please try again.")