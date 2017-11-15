#!/usr/bin/python3

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import os, re
from string import punctuation


subUrls = os.listdir('/var/www/TALN/nestle-family.com/recipes/arRecipes/')

ar_corpus = open('ar_nestleCorpus.txt','w')
i = 0
for subUrl in subUrls:
    url = 'http://localhost/TALN/nestle-family.com/recipes/' + quote(subUrl)
    page = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')
    
    #Remove JS and CSS
    for script in soup(["script", "style"]):
        script.extract()

    #Exract usefull infos
    titles = [ title.text for title in soup.find_all("h1", attrs={"itemprop" : "name"}) ]

    for div in soup.find_all("div", attrs={"class" : "content"}): 
        categories = [ cat.text for cat in div.find_all("h5") ]

    ingredients = [ ing.text for ing in soup.find_all("span", attrs={"itemprop" : "ingredients"}) ]

    for div in soup.find_all("div", attrs={"itemprop" : "recipeInstructions"}):
        preparations = [ prep.text for prep in div.find_all("p") ]

    calories = [ eng.text for eng in soup.find_all("span", attrs={"itemprop" : "calories"}) ]

    #Exceptionnal for this webste
    punctuation = punctuation+"–"
    #Remove punctuation
    titles = ['<title>'+''.join(c for c in s if c not in punctuation)+'</title>' for s in titles]
    categories = ['<cat>'+''.join(c for c in s if c not in punctuation)+'</cat>' for s in categories]
    ingredients = ['<ing>'+''.join(c for c in s if c not in punctuation)+'</ing>' for s in ingredients]
    preparations = ['<prep>'+' '.join(s.split())+'</prep>' for s in preparations]
    calories = ['<eng>'+s+'</eng>' for s in calories]

    #Convert to String
    strTitles = "\n".join(titles)
    strTitles = " ".join(strTitles.split())
    strCategories = "\n".join(categories)
    strCategories = " ".join(strCategories.split())
    strIngredients = "\n".join(ingredients)
    strPreparations = "\n".join(preparations)
    strCalories = "\n".join(calories)

    #String to write in my Corpus
    toWrite = '<rec>\n'+strTitles+'\n'+strCategories+'\n'+strIngredients+'\n'+strPreparations+'\n'+strCalories+'\n</rec>\n'
    ar_corpus.write(toWrite)

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

