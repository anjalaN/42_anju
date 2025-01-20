#!/usr/bin/env python3
import requests
city = input("Location? :")
print(city)
print("dispayweather report" +city)

url = 'https://wttr.in/{}' .format(city)
res = requests.get(url)
print(res.text)