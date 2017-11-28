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

        return taggedText



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
        from nltk.corpus import stopwords
        deniedList = []
        if self.lang == 1:
            colors =  ['blanc', 'noir', 'rouge', 'jaune'] # à compléter
            otherWord = ['tous', 'les', 'ingrédients', 'moitiés', 'trait', 'frais', 'ensemble', 'petits', 'grand', 'préparation', 'préparations', 'poisson', 'légumes', 'fruits', 'épices', 'service', 'plat']
            haram = ['vin', 'porc', 'liqueur', 'cochenille', 'mulet']#à compléter
            stopWords = stopwords.words('french')
            stemmer = nltk.stem.snowball.FrenchStemmer()
        else:
            colors =  [] # à compléter
            otherWord = []
            haram = []#à compléter
            from stop_words import get_stop_words
            stopWords = get_stop_words('arabic')
            from nltk.stem.isri import ISRIStemmer
            stemmer = ISRIStemmer()

        deniedList.extend(colors)
        deniedList.extend(otherWord)
        deniedList.extend(haram)
        deniedList.extend(stopWords)
        deniedList = [stemmer.stem(word) for word in deniedList]
        return deniedList


    # transform a recipe on XML format to a keywords list
    def getKeyWords(self, text):
        if self.lang == 1:
            stemmer = nltk.stem.snowball.FrenchStemmer()
        else:
            from nltk.stem.isri import ISRIStemmer
            stemmer = ISRIStemmer()
        deniedList = self.getDeniedWords()
        keywords = []
        for line in text:
            tline = self.getTagged(line)
            if self.lang != 1 :
                tline = [(item[1].split('/')[0], item[1].split('/')[1]) for item in tline]
            ntline = [taggedWord[0] for taggedWord in tline if taggedWord[1].startswith('N')]
            cleanText = [stemmer.stem(word) for word in ntline if stemmer.stem(word) not in deniedList and word.isalpha()]
            keywords.extend(cleanText)
        return set(keywords)


    # search recipe by diffrent mode
    def getRecipe(self, mode):
        #mode=[1 => all the recipe, 2 => title, 3 => category, 4 => ingredient]
        soup = self.getCorpusSoup()
        if mode == 1:
            output = []
            for div in soup.find_all("rec"):
                output.append(div.text)
            return output

        elif mode == 2:
            balise = "title"
        elif mode == 3:
            balise = "cat"
        else:
            balise = "ing"

        output = []
        for div in soup.find_all("rec"):
            for d in div.find_all(balise):
                output.append(d.text)
        return output


    # search a recipe by ID
    def idSearch(self, idRecipe):
        soup = self.getCorpusSoup()
        recipe = [ balise.text for balise in soup.find_all("rec", attrs={"id" : idRecipe}) ]
        return recipe

    # search a recipe by ID specific data
    def idSearchData(self, idRecipe, mode):
        #mode=[1 => title, 2 => category, 3 => ingredient]
        soup = self.getCorpusSoup()
        if mode == 1:
            balise = "title"
        elif mode == 2:
            balise = "cat"
        elif mode == 3:
            balise = "ing"
        elif mode == 4:
            balise = "prep"
        elif mode == 5:
            balise = "eng"
        else:
            balise = "inf"

        data = []

        for div in soup.find_all("rec", attrs={"id" : str(idRecipe)}):
            for d in div.find_all(balise):
                data.append(d.text)
        return data

    # get recipe ID
    def findById(self, rec):
        soup = BeautifulSoup(rec)
        idRecipe = soup.find("rec")['id']
        return idRecipe


    # check if a recipe is healthy (callories <= 300)
    def isHealthy(self, idRecipe):
        soup = self.getCorpusSoup()
        for balise in soup.find_all("rec", attrs={"id" : idRecipe}):
            for eng in balise.find_all("eng"):
                return eng.text


    def isVegetarian(self, idRecipe):
        meat = ['viande', 'poisson', 'poulet','poivron', 'dinde']
        recipe = self.idSearch(idRecipe)
        keywords = self.getKeyWords(recipe)
        cpt, length = self.existNb(meat, keywords)
        if cpt == 0:
            print(keywords)


    def existNb(self, keywords, recipeKeyWords):
        cpt = 0
        for keyword in keywords:
            if keyword.lower() in recipeKeyWords:
                cpt += 1
        return cpt, len(recipeKeyWords)


    def compare(self, keywords, recipeKeyWords):

        nbWords, lenRecipeKeyWords = self.existNb(keywords, recipeKeyWords)
        prop = round(float((nbWords / lenRecipeKeyWords) * 100), 2)
        # print(prop)
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
            notBio = ['acide'] #à compélter
            notVegan = ['viandes', 'poisson', 'poulet'] #à compélter
            diab = ['sucres', 'miel'] #à compélter
            noCrustace = [''] #à compélter
            noGlutin = [''] #à compélter
            noArachides = [''] #à compélter
            noLait = [''] #à compélter
            stemmer = nltk.stem.snowball.FrenchStemmer()
        else:
            notBio = ['acide'] #à compélter
            notVegan = ['viandes', 'poisson', 'poulet'] #à compélter
            diab = ['sucres', 'miel'] #à compélter
            noCrustace = [''] #à compélter
            noGlutin = [''] #à compélter
            noArachides = [''] #à compélter
            noLait = [''] #à compélter
            from nltk.stem.isri import ISRIStemmer
            stemmer = ISRIStemmer()

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
        
        nonDesirable = [stemmer.stem(word) for word in nonDesirable]
        return nonDesirable


    #lang=1 french / lang=2 arabe
    def getResult(self, queryKeywords, lang, checked):

        import re
        from operator import itemgetter
        lang = self.lang
        corpusKeyWords = open('corpus/frKeyWords.txt', 'r') if lang == 1 else  open('corpus/arKeyWords.txt', 'r')
        idRecipes = {}
        recipesTocheck = {}
        for line in corpusKeyWords.readlines():
            splitedLine = line.split(',')
            idRecipe = splitedLine[0]
            recipeKeywords = splitedLine[1:len(splitedLine)-1]
            last = re.sub('\n', '', splitedLine[len(splitedLine)-1])
            recipeKeywords.append(last)
            decision, prop = self.compare(list(queryKeywords), recipeKeywords)
            if prop != 0 :
                idRecipes[idRecipe] = prop
                recipesTocheck[idRecipe] = (recipeKeywords, prop)
        sortedIdRecipes = sorted(idRecipes.items(), key=itemgetter(1), reverse=True)

        deniedList = self.getNonDesirable(checked)
        checkedRecipes = {}
        for recipeKey in recipesTocheck.keys():
            recipe = recipesTocheck.get(recipeKey)
            exist, i = False, 0
            while i < len(deniedList) and not exist:
                if  deniedList[i] in recipe[0]:
                    exist = True
                i += 1
            if not exist:
                checkedRecipes[recipeKey] =  recipe[1]

        sortedCheckedRecipes = sorted(checkedRecipes.items(), key=lambda x: x[1], reverse=True)

        return sortedIdRecipes, sortedCheckedRecipes






if __name__ == "__main__":
    search = Search(['france'], 'corpus/frCorpus.txt')
    print(search.idSearchData(12, 1))
    # text = search.getRecipe(1)
    # recipeKeyWords = search.getKeyWords(text)
    # print(recipeKeyWords)
    # recipe = search.idSearch(52)
    # print(recipe)

    # print(search.isVegetarian(52))
    # search.getTagged()
    # print(search.idSearch(52))


