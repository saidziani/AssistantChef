#!/usr/bin/pytho3

import re
from urllib.request import urlopen
from urllib.parse import quote
# from bs4 import BeautifulSoup

import os
subUrls = os.listdir('/var/www/TALN/altabkh.net/recipes-copy')

recipeTitles = open('corpus.txt','w')
i = 0
for subUrl in subUrls:

    url = 'http://localhost/TALN/altabkh.net/' + quote(subUrl)
    page = urlopen(url).read().decode('utf-8')
    # copy = open('recipes/recipe'+str(i)+'.txt','w')

    #Remove JS
    page = re.sub(r'<script(?:.|\n)+?/script>', '', page)

    #Remove Comments
    page = re.sub(r'<!--[\s\S]+?-->', '', page)

    #Remove HTML tags
    page = re.sub('<.*?>', '', page)

    #Remove blank
    page = re.sub('\s+', '\n', page)

    
    rtwB = re.search(r'ERName">((?:.|\n)*?)<', page)
    if rtwB:
        # Recipe title
        rtB = re.sub('\n', ' ', rtwB.group(1))
        # Ingredients 
        recipe = re.findall(r'ingredients">((?:.|\n)*?)<', page)
        recipe = re.sub('\n', ' ', '**'.join(recipe))
        #Write into Corpus
        recipeTitles.write(rtB+": "+recipe+"\n=======\n")


    #copy.write(page)
    i += 1
