#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:38:15 2019

@author: malick
"""

import requests
from bs4 import BeautifulSoup
from github import Github


url="https://gist.github.com/paulmillr/2657075"
response= requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

contributors = []

contributors_table =soup.find('tbody')
for row in contributors_table.find_all('tr'):
        if (row.find('th', {'scope': 'row'}) != None):
            contributors.append(row.find('a').text)

g = Github("7e61d6a3a45b7e470d4aef0d0aa4d3344c4491e7")

rank= dict()

for contributor in contributors:
    number_stars= 0
    repos_count=0
    for repo in g.get_user(contributor).get_repos():
        repos_count+=1
        number_stars+= repo.stargazers_count
    rank[contributor]=number_stars/repos_count
    
final_ranking = sorted(rank.items(), key=lambda x: x[1], reverse=True)

print(final_ranking)       
        