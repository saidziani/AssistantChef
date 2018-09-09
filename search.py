from bs4 import BeautifulSoup
import os, nltk

class Search():

    def __init__(self, keywords = False, corpus = False, lang = 1):
        self.keywords = set(keywords)
        self.corpus = corpus
        self.lang = lang

    # get a tagged text: exemple [je suis libre] => [('je', P), ('suis', VB), ('libre', ADJ)]
    def getTagged(self, text):
        from nltk.tag import StanfordPOSTagger

        if self.lang == 1:
            jar = 'stanford-pos-tagger/stanford-postagger-3.8.0.jar'
            model = 'stanford-pos-tagger/french.tagger'
            pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
            tokenizedText = nltk.word_tokenize(text.lower())
            taggedText = pos_tagger.tag(tokenizedText)
        else:
            jar = 'stanford-pos-tagger/stanford-postagger-3.8.0.jar'
            model = 'stanford-pos-tagger/arabic.tagger'
            pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
            tokenizedText = nltk.word_tokenize(text.lower())
            taggedText = pos_tagger.tag(tokenizedText)
            print(taggedText)
        return taggedText
        

    def getStemmedText(self, text):
        stemmedText = []
        if self.lang == 1:
            stemmer = nltk.stem.snowball.FrenchStemmer()
            stemmedText = [stemmer.stem(word) for word in text if word.isalpha()]
        else:
            from tashaphyne.stemming import ArabicLightStemmer
            ArListem = ArabicLightStemmer()
            for word in text:
                if word.isalpha():
                    stem = ArListem.light_stem(word)
                    root = ArListem.get_root()
                    stemmedText.append(root)
        return stemmedText



    # transform my XML page to Beautifull soup object
    def getCorpusSoup(self):
        file = open(self.corpus, 'r')
        content = file.read()
        return BeautifulSoup(content,"lxml")


    # just to split sentence to words
    def text2list(self, text):        
        tokenizedText = nltk.word_tokenize(text.lower())
        return tokenizedText


    # check if my recipe contain a denied ingredient (porc, liqueur...)
    def isDenied(self, content, denied):
        # Content: title or recipe or category 
        # Denied: my word list to denied
        splitedContent = self.text2list(content)
        for ing in denied:
            if ing in splitedContent:
                return False
        return True


    # just to build correctly my denied word list: french stop words + colors ...etc
    def getDeniedWords(self):
        deniedList = []
        if self.lang == 1:
            colors =  ['blanc', 'noir', 'rouge', 'jaune'] # à compléter
            otherWord = ['tous', 'les', 'ingrédients', 'moitiés', 'trait', 'frais', 'ensemble', 'petits', 'grand', 'préparation', 'préparations', 'poisson', 'légumes', 'fruits', 'épices', 'service', 'plat']
            haram = ['vin', 'porc', 'liqueur', 'cochenille', 'mulet', 'jambon', 'alcool', 'bière', 'rhum', 'vodka', 'whisky', 'tequila', 'Gin', 'cognac', 'pastis', 'lardon', 'champagne']#à compléter
            from nltk.corpus import stopwords
            stopWords = stopwords.words('french')
            deniedList.extend(colors)
            deniedList.extend(otherWord)
            deniedList.extend(haram)
            deniedList.extend(stopWords)
        else:
            colors =  [] # à compléter
            otherWord = []
            from stop_words import get_stop_words
            stopWords = get_stop_words('arabic')
            deniedList.extend(colors)
            deniedList.extend(otherWord)
            deniedList.extend(stopWords)
        
        return self.getStemmedText(deniedList)

    # transform a recipe on XML format to a keywords list
    def getKeyWords(self, text):
        deniedList = set(self.getDeniedWords())
        keywords = []
        if self.lang == 1:
            for line in text:
                tline = self.getTagged(line)
                ntline = [taggedWord[0] for taggedWord in tline if taggedWord[1].startswith('N')]
                stemmedNTLine = set(self.getStemmedText(ntline))
                cleanText = stemmedNTLine - deniedList
                keywords.extend(list(cleanText))
        else:
            # from nltk.stem.isri import ISRIStemmer
            # stemmer = ISRIStemmer()
            for line in text:
                tline = self.getTagged(line)
                tline = [(item[1].split('/')[0], item[1].split('/')[1]) for item in tline]
                ntline = [taggedWord[0] for taggedWord in tline if (taggedWord[1].startswith('N') or taggedWord[1].startswith('DTN'))]
                stemmedNTLine = set(self.getStemmedText(ntline))
                cleanText = stemmedNTLine - deniedList
                keywords.extend(list(cleanText))
                # cleanText = [stemmer.stem(word) for word in ntline if stemmer.stem(word) not in deniedList and word.isalpha()]
                # keywords.extend(cleanText)
        return set(keywords)


    # search a recipe by ID
    def idSearch(self, idRecipe):
        soup = self.getCorpusSoup()
        recipe = [ balise.text for balise in soup.find_all("rec", attrs={"id" : idRecipe}) ]
        return recipe

    # get recipe ID
    def findById(self, rec):
        soup = BeautifulSoup(rec)
        idRecipe = soup.find("rec")['id']
        return idRecipe


    def existNb(self, keywords, recipeKeyWords):
        return len(set(set(keywords)).intersection(set(recipeKeyWords)))


    def compare(self, keywords, recipeKeyWords):
        nbWords = self.existNb(keywords, recipeKeyWords)
        lenRecipeKeyWords = len(set(recipeKeyWords))
        prop = round(float((nbWords / lenRecipeKeyWords) * 100), 2)
        if prop == 0:
            return -2, prop 
        elif prop < 30:
            return -1, prop
        elif prop >= 30 and prop < 60: 
            return 0, prop
        else:
            return 1, prop


    # non desirable ingredient
    def getNonDesirable(self, choice):
        if self.lang == 1:
            notBio = ['acide'] #à compléter
            notVegan = ['viandes', 'poisson', 'poulet', 'escalope', 'canard', 'chèvre', 'œuf', 'graisse'] #à compélter
            diab = ['sucres', 'miel', 'tarte', 'pâtisserie'] #à compélter
            noCrustace = ['homard', 'langoustes', 'tourteaux', 'crabes', 'araignée', 'écrevisse', 'étrille' 'crevettes','fruits de mer', 'moules', 'huîtres', 'oursin', 'saumon'] #à compélter
            noGlutin = ['blé', 'seigle','orge','avoine', 'blé','épeautre','engrain', 'farine', 'semoule', 'boulgour', 'amidon', 'muesli', 'pâtes'] #à compélter
            noArachides = ['arachide', 'arachin', 'cacahuète', 'conarachin', 'mandelonas', 'noix'] #à compélter
            noLait = ['lait', 'fromage', 'beurre', 'yaourts', 'kéfir', 'viili', 'bifidus', 'caséine', 'babeurre', 'crème'] #à compélter
            haram = ['vin', 'porc', 'liqueur', 'cochenille', 'mulet', 'jambon', 'alcool', 'bière', 'rhum', 'vodka', 'whisky', 'tequila', 'Gin', 'cognac', 'pastis', 'lardon', 'champagne']#à compléter

        else:
            notBio = ['acide'] #à compélter
            notVegan = ['viandes', 'poisson', 'poulet']#à compélter
            diab = ['sucres', 'miel'] #à compélter
            noCrustace = [''] #à compélter
            noGlutin = [''] #à compélter
            noArachides = [''] #à compélter
            noLait = [''] #à compélter
            haram = ['vin', 'porc', 'liqueur', 'cochenille', 'mulet']#à compléter

        nonDesirable = []
        if 1 in choice: 
            nonDesirable.extend(notBio)
        if 2 in choice:
            nonDesirable.extend(notVegan)
        if 3 in choice:
            nonDesirable.extend(diab)
        if 4 in choice:
            nonDesirable.extend(noCrustace)
        if 5 in choice:
            nonDesirable.extend(noGlutin)
        if 6 in choice:
            nonDesirable.extend(noArachides)
        if 7 in choice:
            nonDesirable.extend(noLait)
        nonDesirable.extend(haram)
        return self.getStemmedText(nonDesirable)


    def getBySet(self):
        frInverse = open('corpusFr/frInverse.txt', 'r')
        queryKeywords = ['croustill', 'beignet']
        for Qkeyword in queryKeywords: 
            for line in frInverse.readlines():
                lineSplited = line.split(',')
                keyword = lineSplited[0]
                if Qkeyword == keyword:
                    print(lineSplited[1:])
            print(Qkeyword)


    #lang=1 french / lang=2 arabe
    def getResult(self, queryKeywords, lang):
        lang = self.lang
        corpusKeyWords = open('corpusFr/frInverse.txt', 'r') if lang == 1 else  open('corpusAr/arKeyWords.txt', 'r')
        content = corpusKeyWords.readlines()
        content = [w[:-1] for w in content]
        idRecipes = {}
        recipesList = []
        for line in content:
            lineContent = line.split(',')
            keyWord = lineContent[0]
            if keyWord in queryKeywords:
                recipesList.append(lineContent[1:len(lineContent)])
        idRecipes = set(recipesList[0])
        for wordList in recipesList:
            idRecipes.intersection(set(wordList))
        return idRecipes


    # transform my XML page to Beautifull soup object
    def getCorpusSoupById(self, idRecipe):
        if idRecipe >= 1 and idRecipe < 1000 :
            corpus = 'corpusFr/frCorpus1.txt'
        elif idRecipe >= 1000 and idRecipe < 2000 :
            corpus = 'corpusFr/frCorpus2.txt'
        elif idRecipe >= 2000 and idRecipe < 3000 :
            corpus = 'corpusFr/frCorpus3.txt'
        elif idRecipe >= 3000 and idRecipe < 4000 :
            corpus = 'corpusFr/frCorpus4.txt'
        elif idRecipe >= 4000 and idRecipe < 5000 :
            corpus = 'corpusFr/frCorpus5.txt'
        elif idRecipe >= 5000 and idRecipe < 6000 :
            corpus = 'corpusFr/frCorpus6.txt'
        elif idRecipe >= 6000 and idRecipe < 7000 :
            corpus = 'corpusFr/frCorpus7.txt'
        elif idRecipe >= 7000 and idRecipe < 8000 :
            corpus = 'corpusFr/frCorpus8.txt'
        elif idRecipe >= 8000 and idRecipe < 9000 :
            corpus = 'corpusFr/frCorpus78.txt'
        elif idRecipe >= 9000 and idRecipe < 10000 :
            corpus = 'corpusFr/frCorpus9.txt'
        elif idRecipe >= 10000 and idRecipe < 11000 :
            corpus = 'corpusFr/frCorpus10.txt'
        elif idRecipe >= 11000 and idRecipe < 12000 :
            corpus = 'corpusFr/frCorpus11.txt'
        elif idRecipe >= 12000 and idRecipe < 13000 :
            corpus = 'corpusFr/frCorpus12.txt'
        elif idRecipe >= 13000 and idRecipe < 14000 :
            corpus = 'corpusFr/frCorpus13.txt'
        elif idRecipe >= 14000 and idRecipe < 15000 :
            corpus = 'corpusFr/frCorpus14.txt'
        elif idRecipe >= 15000 and idRecipe < 16000 :
            corpus = 'corpusFr/frCorpus15.txt'
        elif idRecipe >= 16000 and idRecipe < 17000 :
            corpus = 'corpusFr/frCorpus16.txt'
        elif idRecipe >= 17000 and idRecipe < 18000 :
            corpus = 'corpusFr/frCorpus17.txt'
        elif idRecipe >= 18000 and idRecipe < 18440 :
            corpus = 'corpusFr/frCorpus18.txt'
        else:
            corpus = 'corpusFr/newCorpus.txt'
        file = open(corpus, 'r')
        content = file.read()
        return BeautifulSoup(content,"lxml")


    # search a recipe by ID specific data
    def idSearchRecipeData(self, idRecipe, checked):
        soup = self.getCorpusSoupById(int(idRecipe))
        title, cat, ing, prep, eng, inf = [], [], [], [], [], []
        deniedList = self.getNonDesirable(checked)
        for div in soup.find_all("rec", attrs={"id" : str(idRecipe)}):

            check = False
            i = 0
            while not check and i < len(deniedList) :
                if deniedList[i] in div.text:
                    check = True
                i += 1

            if not check:
                for d in div.find_all('title'):
                    title.append(d.text)
                for d in div.find_all('cat'):
                    cat.append(d.text)
                for d in div.find_all('ing'):
                    ing.append(d.text)
                for d in div.find_all('prep'):
                    prep.append(d.text)
                for d in div.find_all('eng'):
                    eng.append(d.text)
                for d in div.find_all('inf'):
                    inf.append(d.text)
        return title, cat, ing, prep, eng, inf


    def updateCorpus(self, url):

        from urllib.request import urlopen
        from urllib.parse import quote
        import re
        from string import punctuation

        page = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(page,'html.parser')

        lastIdToSave = open('corpusFr/lastIdToSave.txt', 'r')
        lastID = lastIdToSave.read()
        lastIdToSave.close()

        newCorpus = open('corpusFr/newCorpus.txt', 'a')

        urls, i = [], int(lastID)+1
        for a in soup.find_all('a', attrs={"class", "recipe-card"}):
            urls.append(str('http://www.marmiton.org'+a['href']))
        print(urls)
        for url in urls[:5]:
            page = urlopen(url).read().decode('utf-8')
            soup = BeautifulSoup(page,'html.parser')

            titles = [ title.text for title in soup.find_all("h1", attrs={"class" : "main-title"}) ]

            ingredients = [ qt.text+ing.text for (qt,ing) in zip(soup.find_all("span", attrs={"class" : "recipe-ingredient-qt"}), soup.find_all("span", attrs={"class" : "ingredient"})) ]

            preparations = [ prep.text.split('\t\t\t')[1].split('.')[0] for prep in soup.find_all("li", attrs={"class" : "recipe-preparation__list__item"}) ]
            preparations = re.sub('\t', ' ', '. '.join(preparations))

            timePrep = ""
            for divpTime in soup.find_all("div", attrs={"class" : "recipe-infos__timmings__preparation"}):
                for pTime in divpTime.find_all("span", attrs={"class" : "recipe-infos__timmings__value"}):
                    timePrep = pTime.text.strip() 

            cookPrep = ""
            for divpTime in soup.find_all("div", attrs={"class" : "recipe-infos__timmings__cooking"}):
                for pTime in divpTime.find_all("span", attrs={"class" : "recipe-infos__timmings__value"}):
                    cookPrep = pTime.text.strip()

            info = "<inf>Auteur : www.marmiton.org \nNiveau : \nPréparation : "+timePrep+" \nCuisson :"+cookPrep+"</inf>"

            categories = []
            for tagsCat in soup.find_all("ul", attrs={"class" : "mrtn-tags-list"}):
                for tag in tagsCat.find_all("li", attrs={"class" : "mrtn-tag"}):
                    categories.append(tag.text)

            #Remove punctuation
            titles = ['<title>'+''.join(c for c in s if c not in punctuation)+'</title>' for s in titles]
            categories = ['<cat>'+''.join(c for c in s if c not in punctuation)+'</cat>' for s in categories]
            ingredients = ['<ing>'+''.join(c for c in s if c not in punctuation)+'</ing>' for s in ingredients]
            preparations = '<prep>'+preparations+'</prep>'
            calories = '<eng>0</eng>'

            #Convert to String
            strTitles = "\n".join(titles)
            strTitles = " ".join(strTitles.split())
            strCategories = "\n".join(categories)
            strCategories = " ".join(strCategories.split())
            strIngredients = "\n".join(ingredients)

            #String to write in my Corpus
            toWrite = '<rec id='+str(i)+'>\n'+strTitles+'\n'+info+'\n'+strCategories+'\n'+strIngredients+'\n'+preparations+'\n'+calories+'\n</rec>\n'
            newCorpus.write(toWrite)

            i += 1
        lastIdToSave = open('corpusFr/lastIdToSave.txt', 'w')
        lastIdToSave.write(str(i-1))
        lastIdToSave.close()

if __name__ == "__main__":
    searchObj = Search([], 'corpus/arCorpus.txt', 2)
    words = ['ﺔﻧﻭﺮﻜﻌﻤﻟا' ,'ﺎﺑﺎﻄﺒﻟا' ,'ﻞﺼﺒﻟا' ,'ﻞﻔﻠﻔﻟا']
    stemmed = searchObj.getStemmedText(words)
    query = ["ﻖﺘﺴﻔﻟاﻭ" ,"ﺓﺕﻻﻮﻛﻮﺷﻝا" ,"ﻉﺏﺎﺻا"]
    keyWords = searchObj.getKeyWords(query)
    print(keyWords)
