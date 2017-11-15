#!/usr/bin/pytho3

import re
from urllib.request import urlopen
from urllib.parse import quote
# from bs4 import BeautifulSoup

import os
directory = '/var/www/TALN/tareekaa.com/طبخ/'
# os.system('rm '+directory+'*.tmp')
subDir = os.listdir(directory)
recipes = open('corpus.txt','w')
for Dir in subDir:
    subDirectory = '/var/www/TALN/tareekaa.com/طبخ/'+Dir+'/'
    # os.system('rm '+subDirectory+'*.tmp')
    # recipes = open(Dir+'.txt','w')
    i = 0
    subUrls = os.listdir(subDirectory)
    for subUrl in subUrls:
        urlOpen =  'طبخ/'+Dir+'/'+subUrl
        url = 'http://localhost/TALN/tareekaa.com/' + quote(urlOpen)
        page = urlopen(url).read().decode('utf-8')

        # copy = open('recipes/recipe'+str(i)+'.txt','w')

        #Remove JS
        page = re.sub(r'<script(?:.|\n)+?/script>', '', page)

        #Remove Comments
        page = re.sub(r'<!--[\s\S]+?-->', '', page)

        #Remove HTML tags
        # page = re.sub('<.*?>', '', page)

        #Remove blank
        page = re.sub('\s+', '\n', page)

        rtwB = re.search(r'ERSName">((?:.|\n)*?)<', page)

        print(rtwB)
        if rtwB:
            # Recipe title
            rtB = re.sub('\n', ' ', rtwB.group(1))
            # Ingredients 
            recipe = re.findall(r'itemprop="ingredients">((?:.|\n)*?)<', page)
            recipe = re.sub('\n', ' ', '**'.join(recipe))
            #Write into Corpus
            recipes.write(rtB+": "+recipe+"\n=======\n")

        # copy.write(page)
        i += 1
