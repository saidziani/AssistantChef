from PyQt5 import QtCore, QtGui, QtWidgets
import functools
import search, RecipesResFr
import FruitSpaceFr, VegetableSpaceFr, SpiceSpaceFr

ingredient = []
class SelectSpaceFr(object):
    def setupUi(self, Form):
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
        self.label_3.setGeometry(QtCore.QRect(150, 180, 500, 30))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 300, 500, 30))
        self.label_4.setObjectName("label_4")

        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setGeometry(QtCore.QRect(150, 220, 100, 30))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 220, 100, 30))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(450, 220, 100, 30))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(150, 340, 100, 30))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(280, 340, 100, 30))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(390, 340, 100, 30))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(500, 340, 100, 30))
        self.checkBox_7.setObjectName("checkBox_7")        

        self.pushButton = QtWidgets.QPushButton(Form) 
        self.pushButton.setGeometry(QtCore.QRect(550, 400, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #2fd475;\n"
"border-radius: 12px;color:#fff;font-size:14px")


        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")
        self.label_4.setStyleSheet("font-weight:500;\n"
"font-size:17px")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 80, 30))
        self.label_5.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_5.setObjectName("legumes")
        self.label_5.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_5)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(270, 100, 80, 30))
        self.label_6.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_6.setObjectName("fruits")
        self.label_6.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_6)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(390, 100, 80, 30))
        self.label_7.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_7.setObjectName("viandes")
        self.label_7.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_7)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(510, 100, 80, 30))
        self.label_8.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_8.setObjectName("epices")
        self.label_8.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_8)

        self.pushButton.clicked.connect(self.recherche)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Choisissez le type de cuisine qui vous convient:"))
        self.label_4.setText(_translate("Form", "Sélectionner les allergènes à éviter:"))
        self.label_5.setText(_translate("Form", "  Légumes "))
        self.label_6.setText(_translate("Form", "     Fruits "))
        self.label_7.setText(_translate("Form", "   Viandes "))
        self.label_8.setText(_translate("Form", "     Épices "))
        self.checkBox_1.setText(_translate("Form", " Cuisine Bio"))
        self.checkBox_2.setText(_translate("Form", " Végan"))
        self.checkBox_3.setText(_translate("Form", " Diabétique"))
        self.checkBox_4.setText(_translate("Form", " Crustacés"))
        self.checkBox_5.setText(_translate("Form", " Gluten"))
        self.checkBox_6.setText(_translate("Form", " Arachides"))
        self.checkBox_7.setText(_translate("Form", " Lait"))
        self.pushButton.setText(_translate("Form", " Rechercher"))


        

    def retour(self, event):
        self.closeWindow()

    def openIngSpace(self, event, source_object=None):
        source_object.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#2a8fe9;color:#fff;border-radius:15px")

        self.window = QtWidgets.QMainWindow()
        if source_object.objectName() == "legumes":
            self.ui = VegetableSpaceFr.VegetableSpaceFr(self)
        elif source_object.objectName() == "fruits":
            self.ui = FruitSpaceFr.FruitSpaceFr(self)
        elif source_object.objectName() == "epices":
            self.ui = SpiceSpaceFr.SpiceSpaceFr(self)
        else:
            print('Hiiii')

        self.ui.setupUi(self.window)
        self.window.show()

    def getKeyWords(self, ingList):
        ingredient.extend(ingList)
        print(ingredient)


    def recherche(self):
        checked = []
        if self.checkBox_1.isChecked():
            checked.append(1)
        if self.checkBox_2.isChecked():
            checked.append(2)
        if self.checkBox_3.isChecked():
            checked.append(3)
        if self.checkBox_4.isChecked():
            checked.append(4)
        if self.checkBox_5.isChecked():
            checked.append(5)
        if self.checkBox_6.isChecked():
            checked.append(6)
        if self.checkBox_7.isChecked():
            checked.append(7)

        searchObj = search.Search([], 'corpus/frCorpus.txt', 1)

        queryToken = ingredient
        print(queryToken)

        queryKeyWords = searchObj.getKeyWords(queryToken)
        print(queryKeyWords)
        checked, result  = searchObj.getResult(queryKeyWords , 1, checked)

        self.sendData(result)

    def sendData(self,  data):
        self.window = QtWidgets.QMainWindow()
        self.ui = RecipesResFr.RecipesResFr()
        self.ui.setupUi(self.window, data)
        self.window.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SelectSpaceFr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

