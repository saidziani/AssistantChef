#!/usr/bin/python3

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import os
from string import punctuation


directory = '/var/www/TALN/tareekaa.com/طبخ/'
subDir = os.listdir(directory)
ar_trkCorpus = open('ar_trkCorpus.txt','w')

for Dir in subDir:
    subDirectory = '/var/www/TALN/tareekaa.com/طبخ/'+Dir+'/'
    subUrls = os.listdir(subDirectory)

    for subUrl in subUrls:
        urlOpen =  'طبخ/'+Dir+'/'+subUrl
        url = 'http://localhost/TALN/tareekaa.com/' + quote(urlOpen)
        page = urlopen(url).read().decode('utf-8')

        soup = BeautifulSoup(page,'html.parser')
        
        #Remove JS and CSS
        for script in soup(["script", "style"]):
            script.extract()

        #Exract usefull infos
        titles = [ title.text for title in soup.find_all("h1", attrs={"class" : "ERSName"}) ]
        # print(titles)
        # categories = [ cat.text for cat in soup.find_all("a", attrs={"rel" : "category tag"}) ]

        ingredients = [ ing.text for ing in soup.find_all("li", attrs={"itemprop" : "ingredients"}) ]

        preparations = [ prep.text for prep in soup.find_all("li", attrs={"itemprop" : "recipeInstructions"}) ]

        #Exceptionnal for this webste
        # punctuation = punctuation+"–"
        #Remove punctuation
        titles = ['<title>'+''.join(c for c in s if c not in punctuation)+'</title>' for s in titles]
        # categories = ['<cat>'+''.join(c for c in s if c not in punctuation)+'</cat>' for s in categories]
        categories = '<cat>'+Dir+'</cat>'

        ingredients = ['<ing>'+''.join(c for c in s if c not in punctuation)+'</ing>' for s in ingredients]
        preparations = ['<prep>'+''.join(c for c in s if c not in punctuation)+'</prep>' for s in preparations]

        #Convert to String
        strTitles = "\n".join(titles)
        # strCategories = "\n".join(categories)
        strIngredients = "\n".join(ingredients)
        strPreparations = "\n".join(preparations)

        # #String to write in my Corpus
        toWrite = '<rec>\n'+strTitles+'\n'+categories+'\n'+strIngredients+'\n'+strPreparations+'\n</rec>\n'
        ar_trkCorpus.write(toWrite)



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

