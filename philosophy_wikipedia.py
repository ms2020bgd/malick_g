# -*- coding: utf-8 -*-
"""
Exercise - Lesson 2
"""

import urllib
import bs4
import requests


input_url = "https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Thal%C3%A8s"

# Fonction testant les validités des requetes
def crawl(historyList, target_url, limit=25):
    # matching
    if historyList[-1] == target_url:
        print("L'article a été trouvé")
        return False
        # Absence de convergence
    elif len(historyList) > limit:
        print("Délai de réponse trop long")
        return False
        # Cas où l'on a parcouru l'univers sans succès
    elif historyList[-1] in historyList[:-1]:
        print("l'ensemble des liens ont étés checkés sans succès")
        return False
    else:
        return True


# Fonction permettant d'extraire le premier lien pour la direction
def get_redirecting_link(url):
    resp = requests.get(url) 
    html = resp.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    body_html = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for tag in body_html.find_all("p", recursive=False):        
        if tag.find("a", recursive=False):
            recSearchLink = tag.find("a", recursive=False).get('href')
            break
    if not recSearchLink:
        return None
    masterLink = urllib.parse.urljoin(
        'https://fr.wikipedia.org/', recSearchLink)
    return masterLink




# Fonction servant à collecter tout les liens menant à l'url target
def philosophy_way(input_url): 
    way = [input_url]
    target_url = "https://fr.wikipedia.org/wiki/Philosophie"
    while crawl(way, target_url):
        print(way[-1])
        masterLink = get_redirecting_link(way[-1])
        if not masterLink:
            break
        way.append(masterLink)
    print('Distance =  ' + str(len(way)-3))

 # Lancement       
def main():
  philosophy_way(input_url)

if __name__ == '__main__':
    main()
