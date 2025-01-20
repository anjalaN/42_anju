#!/usr/bin/env python3
import requests

API_KEY = "9d8e100fbf99d17abae7be5486ff297f"  # Ta clé API active
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")

#construire l'url pour requete

url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang=fr"

# Effectuer la requête
response = requests.get(url)


#Verifier si la requete a reussi
if response.status_code == 200:
    data = response.json()
    print("Météo actuelle :")
    print(f"Température : {data['main']['temp']}°C")
    print(f"Humidité : {data['main']['humidity']}%")
    print(f"Description : {data['weather'][0]['description']}")
    print(f"Wind : {data['wind']['speed']} m/s")
    print(f"Cloud: {data['clouds']['all']}%")  # Affiche le pourcentage de nuages
    print(f"Direction du vent : {data['wind']['deg']}°")  # Optionnel: Affiche la direction du vent en degrés
else:
    print(f"Erreur : Impossible de récupérer les données (Code : {response.status_code}).")
    print(f"Message de l'API : {response.json()}")