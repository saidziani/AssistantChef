#!/usr/bin/python3

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import os
from string import punctuation


subUrls = os.listdir('/var/www/TALN/altabkh.net/recipes-copy')

ar_corpus = open('ar_altabkhCorpus.txt','w')
i = 1011
for subUrl in subUrls:
    url = 'http://localhost/TALN/altabkh.net/' + quote(subUrl)
    page = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')
    
    #Remove JS and CSS
    for script in soup(["script", "style"]):
        script.extract()

    #Exract usefull infos
    titles = [ title.text for title in soup.find_all("span", attrs={"class" : "item ERName"}) ]

    categories = [ cat.text for cat in soup.find_all("a", attrs={"rel" : "category tag"}) ]

    ingredients = [ ing.text for ing in soup.find_all("li", attrs={"itemprop" : "ingredients"}) ]

    preparations = [ prep.text for prep in soup.find_all("li", attrs={"itemprop" : "recipeInstructions"}) ]

    #Exceptionnal for this webste
    punctuation = punctuation+"–"
    #Remove punctuation
    titles = ['<title>'+''.join(c for c in s if c not in punctuation)+'</title>' for s in titles]
    categories = ['<cat>'+''.join(c for c in s if c not in punctuation)+'</cat>' for s in categories]
    ingredients = ['<ing>'+''.join(c for c in s if c not in punctuation)+'</ing>' for s in ingredients]
    preparations = ['<prep>'+''.join(c for c in s if c not in punctuation)+'</prep>' for s in preparations]

    #Convert to String
    strTitles = "\n".join(titles)
    strCategories = "\n".join(categories)
    strIngredients = "\n".join(ingredients)
    strPreparations = "\n".join(preparations)

    #String to write in my Corpus
    toWrite = '<rec id='+str(i)+'>\n'+strTitles+'\n'+strCategories+'\n'+strIngredients+'\n'+strPreparations+'\n</rec>\n'
    ar_corpus.write(toWrite)
    i += 1

    #Recipe architecture
    # <rec>
    #     <title></title>
    #     <cat></cat>
    #     <cat></cat>
    #     <ing></ing>
    #     <ing></ing>
    #     <ing></ing>
    #     <prep></prep>
    #     <prep></prep>
    #     <prep></prep>
    #     <prep></prep>
    # </rec>

