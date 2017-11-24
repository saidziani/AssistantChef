from bs4 import BeautifulSoup
import os
from nltk.tokenize import TweetTokenizer

#Tokenisation
tweet = "Hi! i'm Farid i have 1520$ #mony :-) :) <3 !"

class Search():


    def __init__(self, keywords = False, corpus = False):
        self.keywords = set(keywords)
        self.corpus = corpus

    # get a tagged text: exemple [je suis libre] => [('je', P), ('suis', VB), ('libre', ADJ)]
    def getTagged(self, text):
        from nltk.tag import StanfordPOSTagger
        jar = 'stanford-french-pos-tagger/stanford-postagger-3.8.0.jar'
        model = 'stanford-french-pos-tagger/french.tagger'
        pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8' )
        tokenizer = TweetTokenizer()
        tokenizedText = tokenizer.tokenize(text.lower())
        taggedText = pos_tagger.tag(tokenizedText)
        return taggedText

    # transform my XML page to Beautifull soup object
    def getCorpusSoup(self):
        file = open(self.corpus, 'r')
        content = file.read()
        return BeautifulSoup(content,"lxml")

    # just to split sentence to words
    def text2list(self, text):
        tokenizer = TweetTokenizer()
        tokenizedText = tokenizer.tokenize(text.lower())
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
        colors = ['blanc', 'noir', 'rouge', 'jaune'] # à compléter
        otherWord = ['tous', 'les', 'ingrédients', 'moitiés', 'trait', 'frais', 'ensemble', 'petits', 'grand', 'préparation', 'préparations']
        deniedList = []
        deniedList.extend(stopwords.words('french')) 
        deniedList.extend(colors)
        deniedList.extend(otherWord)
        return deniedList

    # transform a recipe on XML format to a keywords list
    def getKeyWords(self, text):
        deniedList = self.getDeniedWords() 
        keywords = []
        for line in text:
            line = self.getTagged(line)
            line = [taggedWord[0] for taggedWord in line if taggedWord[1].startswith('N')]
            cleanText = [word for word in line if word not in deniedList and word.isalpha()]
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


    def existNb(self,keywords, recipeKeyWords):
        cpt = 0
        for keyword in keywords:
            if keyword.lower() in recipeKeyWords:
                cpt += 1
        return cpt, len(recipeKeyWords)


    def compare(self,keywords, recipeKeyWords):
        nbWords, lenRecipeKeyWords = self.existNb(keywords, recipeKeyWords)
        prop = (nbWords / lenRecipeKeyWords) * 100
        print(prop)
        if prop == 0:
            return 0 
        elif prop < 30:
            return -1
        elif prop >= 30 and prop < 60: 
            return 0
        else:
            return 1




if __name__ == "__main__":
    search = Search(['abricots', 'soUpe', 'balsamique', 'feuilles', 'concombre', 'vinaigre','vinaigre','vinaigre','vinaigre',  'أكواب', 'chèvre', 'الجيلي'], 'French_corpus.txt')
    text = search.getRecipe(1)
    recipeKeyWords = search.getKeyWords(text)
    print(recipeKeyWords)
    # recipe = search.idSearch(52)
    # print(recipe)

    # print(search.isVegetarian(52))
    # search.getTagged()
    # print(search.idSearch(52))





#Recherche Minceur
#nombre de calories 

#KCAL='300'
#def recherche_nutritioniste(soup,KCAL):
#     for div in soup.find_all("rec"):
#            for d in div.find_all("title"):
#                if (d in HallalFood(soup)):
#                    for(d1 in d.find_all("eng")):
#                        print(d1.text)
#recherche_nutritioniste(soup,KCAL) 




#online 




########################################""#recette de la semaine####################################################
#online : 1st step


# import locale
# import datetime

# locale.setlocale(locale.LC_ALL, locale="French")
# now = datetime.datetime.now()

# jour=now.strftime("%A")
# url="http://www.cuisineaz.com/idees-repas/?jour="+jour

# page=urlopen(url).read().decode('utf-8')
    
# soup1 = BeautifulSoup(page,'html.parser')

# for div in soup1.find_all("article", attrs={'id':'ContentPlaceHolder_rptMenuElementRecette_elemListItem_0','class':'tile entree'}):
#         dj=re.sub('[\n]+','',div.text)        
#         print(dj)
#         recherche_recette(soup,dj)
# for div in soup1.find_all("article", attrs={'id':'ContentPlaceHolder_rptMenuElementRecette_elemListItem_1','class':'tile plat'}):
#         dj=re.sub('[\n]+','',div.text)        
#         print(dj)
#         recherche_recette(soup,dj)
# for div in soup1.find_all("article", attrs={'id':'ContentPlaceHolder_rptMenuElementRecette_elemListItem_2','class':'tile dessert'}):
#         dj=re.sub('[\n]+','',div.text)        
#         print(dj)
#         recherche_recette(soup,dj)
## Maj recette




#Rapporter les noms des plats du jour 



#offline : 2nd step
#recherche_recette(soup,recette)   




#######################################contrainte sur les ingredients##################################################### 









##########################################Recherche video################################################################
# supposons qu'on a un lien extrait avec chaque recette
# on ouvre le lien on aura a le telechager 
#TESTvIDEOS
#lecteur video sur l'interface.



########################################################################################################################

# <rec>
# <title>AbraCadaBra Gâteau Magique version salé ..</title>
# <inf>Auteur : 
# Niveau : Facile
# Préparation : 15 min
# Cuisson :35 min</inf>
# <cat>Légumes</cat>
# <cat>Poivron</cat>
# <ing>2 œufs</ing>
# <ing>25 cl de lait             </ing>
# <ing>65 g de beurre </ing>
# <ing>30 g d'emmental râpé</ing>
# <ing>50 gr de Parmesan</ing>
# <ing>70 gr de Grogonzola</ing>
# <ing>100 g de lardons</ing>
# <ing>½ poivron long en petits dés</ing>
# <ing>55 gr de farine </ing>
# <ing>¼ cc noix de muscade râpée </ing>
# <ing>Sel, poivre du moulin </ing>
# <prep>1°- Faites fondre le beurre, puis laissez-le tiédir. Dans une casserole, faites chauffer le lait et réservez.     2°- Séparez les blancs des jaunes d'oeufs dans deux saladiers. Blanchissez les jaunes avec le beurre fondu. 3°- Incorporez la farine en deux fois et versez le lait en deux ou trois fois aussi . 4°- Ajoutez l'emmental râpé et le parmesan , la noix de muscade, salez, poivrez et mélangez. 5°- Montez les blancs en neige** très ferme  puis, à l'aide d'une spatule, incorporez-les à la préparation précédente **  Pour incorporer les blancs en neige à la préparation très liquide, il est conseillé d’utiliser un fouet en travaillant la masse doucement,afin de ne pas la dissoudre dans la pâte : il doit rester de gros grumeaux. Il est en effet difficile d’incorporer des blancs à une préparation liquide avec une cuillère en bois.6°- Répartissez les lardons et le poivron coupez en petits dés au fond du moule, puis versez le mélange aux oeufs par-dessus. 07°- Mettre au four chaud 160 ° pour 35 mn. Le dessus du gâteau doit être doré et l'intérieur légèrement tremblotant.</prep>
# <eng></eng>
# </rec>
#HallalFood
# NHI='bacon,gélatine,jambon,porc,liqueur,biere,vin'