from PyQt5 import QtCore, QtGui, QtWidgets
import search, OneRecipeFr
import functools

recipes = {}

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
        print(data)
        newData = []
        for rec in data:
            if rec:
                newData.append(rec)
        print(newData)
        nbRecipes = len(data)
        self.label_3.setText(str(sizeRecipes)+' résultats de recherche')
        labels = ['self.label_'+str(i) for i in range(4, nbRecipes+4)]
        labels4Cat = ['self.label_'+str(i+nbRecipes) for i in range(4, nbRecipes+4)]

        h = 110

        i = 0
        for (info, labelCat, label) in zip(newData, labels4Cat, labels):
            idRecipe = info
            title, cat, ing, prep, eng, inf  = self.getRecipeTitle(idRecipe, checked)
            title = ', '.join(title)
            if title:
                tmpRecipe = [title, cat, ing, prep, eng, inf]
                recipes[idRecipe] = tmpRecipe

                label = QtWidgets.QLabel(Form)
                label.setGeometry(QtCore.QRect(150, h, 500, 25))
                label.setObjectName(idRecipe)
                label.setText(title)
                label.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                label.mousePressEvent = self.sendData
                label.mousePressEvent = functools.partial(self.sendData, source_object=label)

                cat = ' | '.join(cat)
                nameL = labelCat[5:]
                labelL = QtWidgets.QLabel(Form)
                labelL.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                labelL.setObjectName(nameL)
                labelL.setText(cat)
                labelL.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")

                h += 65
                i += 1
            if i == 5:
                break

        self.keywords = queryWords
        self.labelRechNoline = QtWidgets.QLabel(Form)
        self.labelRechNoline.setGeometry(QtCore.QRect(150, 450, 500, 30))
        self.labelRechNoline.setObjectName("labelRechNoline")
        self.labelRechNoline.setStyleSheet("font-size:14px;color:#bdbdbd")
        self.labelRechNoline.setText("Recherche infructueuse ? faites une recherhce en ligne.")
        self.labelRechNoline.mousePressEvent = functools.partial(self.doOnlineSearche)

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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RecipesResFr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

