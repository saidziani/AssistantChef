#!/usr/bin/pytho3

import re
# from urllib.request import urlopen
# from urllib.parse import quote
# from bs4 import BeautifulSoup

# import os
# subUrls = os.listdir('/var/www/TALN/altabkh.net')

file = open('copy.txt')
page = file.read()
copy = open('copy22.txt','w')

#Extract Recip name
 # = re.search(r'<span itemprop="name" class="item ERName">(.+)</span>', page)
 # class="ingredient" itemprop="ingredients">200 جرام شوفان</li><li

print(re.findall(r'ingredients">((?:.|\n)*?)<', page))


    #With bs4
    # soup = BeautifulSoup(page, "lxml")
    # for script in soup.find_all('script'):
    #     script.decompose()
    # page = soup.get_text()

# copy.write(' '.join(page))

