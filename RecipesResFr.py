from PyQt5 import QtCore, QtGui, QtWidgets
import search, OneRecipeFr
import functools

recipes = {}
actualRecipeNb = 0
actualNoneEmptyRecipeNb = 0
precedentFive = []
class RecipesResFr(object):

    def setupUi(self, Form):

        ['12846', '5323', '5', '5613', '11614', '3129', '10151', '5874', '12081', '16022', '5048', '3993', '4828', '13840']

        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #424242;")
        
        data = ['12846', '5323', '5', '5613', '11614', '3129', '10151', '5874', '12081', '16022', '5048', '3993', '4828', '13840', '9590', '5590', '1248', '3074', '15699', '4135', '15775', '16274', '3555', '7957', '10877', '16272', '2235', '7265', '13496', '15791', '13363', '13829', '6521', '15765', '15701', '1302', '12085', '668', '6153', '16478', '682', '14229', '1219', '15704', '8922', '2', '5977', '13511', '16031', '1642', '16024', '2453', '5553', '770', '11065', '6418', '13603', '9466', '3384', '16025', '8675', '5592', '16271', '4361', '8018', '13520', '3069', '3208', '1291', '4853', '5146', '15559', '3', '11229', '4464', '3010', '15838', '10661', '12386', '6024', '553', '1518', '16275', '8344', '6557', '3340', '4268', '14108', '1236', '3499', '2805', '15751', '15714', '13415', '2413', '9471', '2824', '11270', '5920', '15766', '10076', '6256', '1252', '5180', '16023', '4659', '16082', '16270', '2889', '2786', '12054', '4581', '6574', '8600', '15767', '16273', '2790', '1627', '13515', '3070', '4', '3009', '3754']

        checked = []

        queryWords = ['citron']

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
        print("I'm from RecipesFr:", data)
        noneEmptyRecipes = []
        for rec in data:
            if rec:
                noneEmptyRecipes.append(rec)

        self.noneEmptyRecipes = noneEmptyRecipes
        self.label_3.setText(str(sizeRecipes)+' résultats de recherche')

        global actualNoneEmptyRecipeNb
        h = 110
        i = 0
        for info in noneEmptyRecipes:
            idRecipe = info
            title, cat, ing, prep, eng, inf  = self.getRecipeTitle(idRecipe, checked)
            title = ', '.join(title)
            actualNoneEmptyRecipeNb += 1
            if title:
                tmpRecipe = [title, cat, ing, prep, eng, inf]
                recipes[idRecipe] = tmpRecipe
                precedentFive.append(idRecipe)
                if i == 0:
                    self.label_4 = QtWidgets.QLabel(Form)
                    self.label_4.setGeometry(QtCore.QRect(150, h, 600, 25))
                    self.label_4.setObjectName(idRecipe)
                    self.label_4.setText(title)
                    self.label_4.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_4.mousePressEvent = functools.partial(self.sendData, source_object=self.label_4)

                    cat = ' | '.join(cat)
                    self.labelL_4 = QtWidgets.QLabel(Form)
                    self.labelL_4.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_4.setObjectName("self.labelL_4")
                    self.labelL_4.setText(cat)
                    self.labelL_4.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 1:
                    self.label_5 = QtWidgets.QLabel(Form)
                    self.label_5.setGeometry(QtCore.QRect(150, h, 600, 25))
                    self.label_5.setObjectName(idRecipe)
                    self.label_5.setText(title)
                    self.label_5.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_5.mousePressEvent = functools.partial(self.sendData, source_object=self.label_5)

                    cat = ' | '.join(cat)
                    self.labelL_5 = QtWidgets.QLabel(Form)
                    self.labelL_5.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_5.setObjectName("self.labelL_5")
                    self.labelL_5.setText(cat)
                    self.labelL_5.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 2:
                    self.label_6 = QtWidgets.QLabel(Form)
                    self.label_6.setGeometry(QtCore.QRect(150, h, 600, 25))
                    self.label_6.setObjectName(idRecipe)
                    self.label_6.setText(title)
                    self.label_6.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_6.mousePressEvent = functools.partial(self.sendData, source_object=self.label_6)

                    cat = ' | '.join(cat)
                    self.labelL_6 = QtWidgets.QLabel(Form)
                    self.labelL_6.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_6.setObjectName("self.labelL_6")
                    self.labelL_6.setText(cat)
                    self.labelL_6.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 3:
                    self.label_7 = QtWidgets.QLabel(Form)
                    self.label_7.setGeometry(QtCore.QRect(150, h, 600, 25))
                    self.label_7.setObjectName(idRecipe)
                    self.label_7.setText(title)
                    self.label_7.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_7.mousePressEvent = functools.partial(self.sendData, source_object=self.label_7)

                    cat = ' | '.join(cat)
                    self.labelL_7 = QtWidgets.QLabel(Form)
                    self.labelL_7.setGeometry(QtCore.QRect(150, h+25, 500, 20))
                    self.labelL_7.setObjectName("self.labelL_7")
                    self.labelL_7.setText(cat)
                    self.labelL_7.setStyleSheet("font-size:14px;color:#7d7d7d;font-weight:200")


                if i == 4:
                    self.label_8 = QtWidgets.QLabel(Form)
                    self.label_8.setGeometry(QtCore.QRect(150, h, 600, 25))
                    self.label_8.setObjectName(idRecipe)
                    self.label_8.setText(title)
                    self.label_8.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
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

        if len(noneEmptyRecipes) > 5:
            self.labelNext = QtWidgets.QLabel(Form)
            self.labelNext.setGeometry(QtCore.QRect(260, 430, 100, 30))
            self.labelNext.setObjectName("labelNext")
            self.labelNext.setStyleSheet("font-size:16px;color:#424242;opacity:0.6")
            self.labelNext.setText('Suivant >>')
            self.labelNext.mousePressEvent = functools.partial(self.nextORprecDisplay, source_object=self.labelNext)

        self.labelPreced = QtWidgets.QLabel(Form)
        self.labelPreced.setGeometry(QtCore.QRect(150, 430, 110, 30))
        self.labelPreced.setObjectName("labelPreced")
        self.labelPreced.setStyleSheet("font-size:16px;color:#424242;opacity:0.6")
        self.labelPreced.setText('<< Précédent |')
        self.labelPreced.mousePressEvent = functools.partial(self.nextORprecDisplay, source_object=self.labelPreced)


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


    def nextORprecDisplay(self, event, source_object=None):

        global actualNoneEmptyRecipeNb
        global precedentFive

        i = 0
        startPoint = actualNoneEmptyRecipeNb

        myList = self.noneEmptyRecipes[startPoint:]
        if source_object.objectName()=="labelPreced":
            myList = precedentFive

        for info in myList:
            idRecipe = info
            title, cat, ing, prep, eng, inf  = self.getRecipeTitle(idRecipe, [])
            title = ', '.join(title)
            if source_object.objectName()=="labelNext":
                actualNoneEmptyRecipeNb += 1
            if title:
                tmpRecipe = [title, cat, ing, prep, eng, inf]
                recipes[idRecipe] = tmpRecipe

                if i == 0:
                    self.label_4.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_4.setText(title)
                    self.label_4.setObjectName(idRecipe)
                    cat = ' | '.join(cat)
                    self.labelL_4.setText(cat)
                    self.label_4.mousePressEvent = functools.partial(self.sendData, source_object=self.label_4)
                    if source_object.objectName()=="labelNext":
                        precedentFive[0] = idRecipe

                if i == 1:
                    self.label_5.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_5.setText(title)
                    self.label_5.setObjectName(idRecipe)
                    cat = ' | '.join(cat)
                    self.labelL_5.setText(cat)
                    self.label_5.mousePressEvent = functools.partial(self.sendData, source_object=self.label_5)
                    if source_object.objectName()=="labelNext":
                        precedentFive[1] = idRecipe

                if i == 2:
                    self.label_6.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_6.setText(title)
                    self.label_6.setObjectName(idRecipe)
                    cat = ' | '.join(cat)
                    self.labelL_6.setText(cat)
                    self.label_6.mousePressEvent = functools.partial(self.sendData, source_object=self.label_6)
                    if source_object.objectName()=="labelNext":
                        precedentFive[2] = idRecipe

                if i == 3:
                    self.label_7.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_7.setText(title)
                    self.label_7.setObjectName(idRecipe)
                    cat = ' | '.join(cat)
                    self.labelL_7.setText(cat)
                    self.label_7.mousePressEvent = functools.partial(self.sendData, source_object=self.label_7)
                    if source_object.objectName()=="labelNext":
                        precedentFive[3] = idRecipe

                if i == 4:
                    self.label_8.setStyleSheet("font-size:19px;color:#424242;font-weight:500")
                    self.label_8.setText(title)
                    self.label_8.setObjectName(idRecipe)
                    cat = ' | '.join(cat)
                    self.labelL_8.setText(cat)
                    self.label_8.mousePressEvent = functools.partial(self.sendData, source_object=self.label_8)
                    if source_object.objectName()=="labelNext":
                        precedentFive[4] = idRecipe
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

