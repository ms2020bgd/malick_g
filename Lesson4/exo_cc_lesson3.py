#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:52:42 2019

@author: malick
"""

import itertools
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://fr.wikipedia.org/wiki/Liste_des_communes_de_France_les_plus_peuplées"


def get_soup_from_url(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')


def get_biggest_cities(limit=10):
    cities = []
    soup = get_soup_from_url(URL)
    rows = soup.find('table').find_all('tr')[1:]
    for r in rows:
        cells = r.find_all('td')
        city = cells[1].find('a').text.strip()
        cities.append(city)
    return cities[:limit]


def get_distance_between(origin, destination):
    url = f"https://fr.distance24.org/route.json?stops={origin}|{destination}"
    data = requests.get(url).json()
    return data['distance']


cities = get_biggest_cities()
combinations = list(itertools.combinations(cities, 2))

distances = []
for origin, dest in combinations:
    distance = get_distance_between(origin, dest)
    distances.append(distance)
    
df = pd.DataFrame(combinations, columns=['origin', 'dest'])

df['distance'] = distances

print(df)
    
    
    
    
    
    
    
