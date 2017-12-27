from PyQt5 import QtCore, QtGui, QtWidgets
import search, OneRecipeFr
import functools

recipes = {}
nbClick = 0
nonEmpty = 0
class RecipesResFr(object):

    def setupUi(self, Form, data, checked, queryWords):

        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #424242;")
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.closeWindow = Form.close


        self.labelNext = QtWidgets.QLabel(Form)
        self.labelNext.setGeometry(QtCore.QRect(150, 430, 500, 30))
        self.labelNext.setObjectName("labelRechNoline")
        self.labelNext.setStyleSheet("font-size:16px;color:#bdbdbd")
        self.labelNext.setText('Suivant >>')


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('MonChef-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 70, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-size:15px;color:#bdbdbd")

        sizeRecipes = len(data)
        print("I'm from RecipesFr:", data)
        newData = []
        for rec in data:
            if rec:
                newData.append(rec)

        self.newData = newData
        # nbRecipes = len(data)
        self.label_3.setText(str(sizeRecipes)+' résultats de recherche')
        # labels = ['self.label_'+str(i) for i in range(4, nbRecipes+4)]
        # labels4Cat = ['self.label_'+str(i+nbRecipes) for i in range(4, nbRecipes+4)]


        global nonEmpty
        h = 110
        i = 0
        for info in newData:
            idRecipe = info
            title, cat, ing, prep, eng, inf  = self.getRecipeTitle(idRecipe, checked)
            title = ', '.join(title)
            nonEmpty += 1
            if title:
                if i == 0:
                    self.label_4 = QtWidgets.QLabel(Form)
                    self.label_4.setGeometry(QtCore.QRect(150, h, 500, 25))
                    self.label_4.setObjectName(idRecipe)
                    self.label_4.setText(title)
                    self.label_4.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_4.mousePressEvent = self.sendData
                    self.label_4.mousePressEvent = functools.partial(self.sendData, source_object=self.label_4)

                    cat = ' | '.join(cat)
                    self.labelL_4 = QtWidgets.QLabel(Form)
                    self.labelL_4.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_4.setObjectName("self.labelL_4")
                    self.labelL_4.setText(cat)
                    self.labelL_4.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 1:
                    self.label_5 = QtWidgets.QLabel(Form)
                    self.label_5.setGeometry(QtCore.QRect(150, h, 500, 25))
                    self.label_5.setObjectName(idRecipe)
                    self.label_5.setText(title)
                    self.label_5.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_5.mousePressEvent = self.sendData
                    self.label_5.mousePressEvent = functools.partial(self.sendData, source_object=self.label_5)

                    cat = ' | '.join(cat)
                    self.labelL_5 = QtWidgets.QLabel(Form)
                    self.labelL_5.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_5.setObjectName("self.labelL_5")
                    self.labelL_5.setText(cat)
                    self.labelL_5.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 2:
                    self.label_6 = QtWidgets.QLabel(Form)
                    self.label_6.setGeometry(QtCore.QRect(150, h, 500, 25))
                    self.label_6.setObjectName(idRecipe)
                    self.label_6.setText(title)
                    self.label_6.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_6.mousePressEvent = self.sendData
                    self.label_6.mousePressEvent = functools.partial(self.sendData, source_object=self.label_6)

                    cat = ' | '.join(cat)
                    self.labelL_6 = QtWidgets.QLabel(Form)
                    self.labelL_6.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_6.setObjectName("self.labelL_6")
                    self.labelL_6.setText(cat)
                    self.labelL_6.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 3:
                    self.label_7 = QtWidgets.QLabel(Form)
                    self.label_7.setGeometry(QtCore.QRect(150, h, 500, 25))
                    self.label_7.setObjectName(idRecipe)
                    self.label_7.setText(title)
                    self.label_7.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_7.mousePressEvent = self.sendData
                    self.label_7.mousePressEvent = functools.partial(self.sendData, source_object=self.label_7)

                    cat = ' | '.join(cat)
                    self.labelL_7 = QtWidgets.QLabel(Form)
                    self.labelL_7.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_7.setObjectName("self.labelL_7")
                    self.labelL_7.setText(cat)
                    self.labelL_7.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 4:
                    self.label_8 = QtWidgets.QLabel(Form)
                    self.label_8.setGeometry(QtCore.QRect(150, h, 500, 25))
                    self.label_8.setObjectName(idRecipe)
                    self.label_8.setText(title)
                    self.label_8.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_8.mousePressEvent = self.sendData
                    self.label_8.mousePressEvent = functools.partial(self.sendData, source_object=self.label_8)

                    cat = ' | '.join(cat)
                    self.labelL_8 = QtWidgets.QLabel(Form)
                    self.labelL_8.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_8.setObjectName("self.labelL_8")
                    self.labelL_8.setText(cat)
                    self.labelL_8.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")

                h += 65
                i += 1
            if i == 5:
                break


        self.keywords = queryWords
        self.labelRechNoline = QtWidgets.QLabel(Form)
        self.labelRechNoline.setGeometry(QtCore.QRect(150, 460, 500, 30))
        self.labelRechNoline.setObjectName("labelRechNoline")
        self.labelRechNoline.setStyleSheet("font-size:14px;color:#bdbdbd")
        self.labelRechNoline.setText("Recherche infructueuse ? faites une recherhce en ligne.")
        self.labelRechNoline.mousePressEvent = functools.partial(self.doOnlineSearche)

        self.labelNext.mousePressEvent = self.display


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))


    def retour(self, event):
        self.closeWindow()

    def getRecipeTitle(self, idRecipe, checked):
        searchObj = search.Search([], 'corpusFr/frCorpus.txt', 1)
        title, cat, ing, prep, eng, inf = searchObj.idSearchRecipeData(idRecipe, checked)
        print("From getRecipe:", title)
        return title, cat, ing, prep, eng, inf


    def doOnlineSearche(self, event):
        queryKeyWords = '-'.join(self.keywords)
        import webbrowser 
        new = 2
        url = "http://www.marmiton.org/recettes/recherche.aspx?type=all&aqt="+queryKeyWords
        webbrowser.get(using='chromium-browser').open(url,new=new)
        searchObj = search.Search([], 'corpusFr/frCorpus.txt', 1)
        searchObj.updateCorpus(url)


    def sendData(self, event, source_object=None):
        source_object.setStyleSheet("font-size:19px;color:#2a8fe9;font-weight:500")
        recipeChoosed = recipes.get(source_object.objectName()) 
        self.window = QtWidgets.QMainWindow()
        self.ui = OneRecipeFr.OneRecipeFr()
        self.ui.setupUi(self.window, recipeChoosed)
        self.window.show()


    def display(self, position):
        global nbClick
        global nonEmpty
        nonEmptyNb = nonEmpty
        i = 0
        nbClick += 5
        for info in self.newData[nonEmptyNb:]:
            idRecipe = info
            title, cat, ing, prep, eng, inf  = self.getRecipeTitle(idRecipe, [])
            title = ', '.join(title)
            nonEmpty += 1
            if title:
                if i == 0:
                    self.label_4.setText(title)
                    cat = ' | '.join(cat)
                    self.labelL_4.setText(cat)
                if i == 1:
                    self.label_5.setText(title)
                    cat = ' | '.join(cat)
                    self.labelL_5.setText(cat)
                if i == 2:
                    self.label_6.setText(title)
                    cat = ' | '.join(cat)
                    self.labelL_6.setText(cat)
                if i == 3:
                    self.label_7.setText(title)
                    cat = ' | '.join(cat)
                    self.labelL_7.setText(cat)
                if i == 4:
                    self.label_8.setText(title)
                    cat = ' | '.join(cat)
                    self.labelL_8.setText(cat)
                i += 1
            if i == 5:
                break
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RecipesResFr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

