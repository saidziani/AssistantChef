from PyQt5 import QtCore, QtGui, QtWidgets
import functools, SelectSpaceFr

legumes = []
class VegetableSpaceFr(object):
    def __init__(self, uiMain):
        self.uiMain = uiMain

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #424242;")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

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

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 450, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #2fd475;\n"
"border-radius: 15px;color:#fff;font-size:14px")
        self.pushButton.clicked.connect(self.valider)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 50, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")

        ####################################################################

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("tomate")
        pixmap = QtGui.QPixmap('ing/legumes/tomate.jpg').scaledToWidth(80)
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(100, 80, 100, 100))
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 170, 65, 20))
        self.label_5.setObjectName("tomate")
        self.label_5.mousePressEvent = functools.partial(self.stack, source_object=self.label_5)
        self.label_4.mousePressEvent = functools.partial(self.stack, source_object=self.label_5)


        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("concombre")
        pixmap = QtGui.QPixmap('ing/legumes/concombre.jpg').scaledToWidth(80)
        self.label_6.setPixmap(pixmap)
        self.label_6.setGeometry(QtCore.QRect(220, 80, 100, 100))
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(220, 170, 85, 20))
        self.label_7.setObjectName("concombre")
        self.label_7.mousePressEvent = functools.partial(self.stack, source_object=self.label_7)
        self.label_6.mousePressEvent = functools.partial(self.stack, source_object=self.label_7)


        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("carotte")
        pixmap = QtGui.QPixmap('ing/legumes/carotte.jpg').scaledToWidth(80)
        self.label_8.setPixmap(pixmap)
        self.label_8.setGeometry(QtCore.QRect(340, 80, 100, 100))
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(350, 170, 60, 20))
        self.label_9.setObjectName("carotte")
        self.label_9.mousePressEvent = functools.partial(self.stack, source_object=self.label_9)
        self.label_8.mousePressEvent = functools.partial(self.stack, source_object=self.label_9)


        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("ail")
        pixmap = QtGui.QPixmap('ing/legumes/ail.jpg').scaledToWidth(80)
        self.label_10.setPixmap(pixmap)
        self.label_10.setGeometry(QtCore.QRect(460, 80, 100, 100))
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(490, 170, 32, 20))
        self.label_11.setObjectName("ail")
        self.label_11.mousePressEvent = functools.partial(self.stack, source_object=self.label_11)
        self.label_10.mousePressEvent = functools.partial(self.stack, source_object=self.label_11)


        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("pomme2terre")
        pixmap = QtGui.QPixmap('ing/legumes/pomme2terre.jpg').scaledToWidth(80)
        self.label_12.setPixmap(pixmap)
        self.label_12.setGeometry(QtCore.QRect(580, 80, 100, 100))
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(570, 170, 120, 20))
        self.label_13.setObjectName("pomme2terre")
        self.label_13.mousePressEvent = functools.partial(self.stack, source_object=self.label_13)
        self.label_12.mousePressEvent = functools.partial(self.stack, source_object=self.label_13)



        ####################################################################
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("poivron")
        pixmap = QtGui.QPixmap('ing/legumes/poivron.jpg').scaledToWidth(80)
        self.label_14.setPixmap(pixmap)
        self.label_14.setGeometry(QtCore.QRect(100, 200, 100, 100))
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(110, 290, 60, 20))
        self.label_15.setObjectName("poivron")
        self.label_15.mousePressEvent = functools.partial(self.stack, source_object=self.label_15)
        self.label_14.mousePressEvent = functools.partial(self.stack, source_object=self.label_15)


        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("oignon")
        pixmap = QtGui.QPixmap('ing/legumes/oignon.jpg').scaledToWidth(80)
        self.label_16.setPixmap(pixmap)
        self.label_16.setGeometry(QtCore.QRect(220, 200, 100, 100))
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(235, 290, 60, 20))
        self.label_17.setObjectName("oignon")
        self.label_17.mousePressEvent = functools.partial(self.stack, source_object=self.label_17)
        self.label_16.mousePressEvent = functools.partial(self.stack, source_object=self.label_17)


        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setObjectName("choufleur")
        pixmap = QtGui.QPixmap('ing/legumes/choufleur.jpg').scaledToWidth(80)
        self.label_18.setPixmap(pixmap)
        self.label_18.setGeometry(QtCore.QRect(340, 200, 100, 100))
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(350, 290, 80, 20))
        self.label_19.setObjectName("choufleur")
        self.label_19.mousePressEvent = functools.partial(self.stack, source_object=self.label_19)
        self.label_18.mousePressEvent = functools.partial(self.stack, source_object=self.label_19)


        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setObjectName("aubergine")
        pixmap = QtGui.QPixmap('ing/legumes/aubergine.jpg').scaledToWidth(80)
        self.label_20.setPixmap(pixmap)
        self.label_20.setGeometry(QtCore.QRect(460, 200, 100, 100))
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(465, 290, 80, 20))
        self.label_21.setObjectName("aubergine")
        self.label_21.mousePressEvent = functools.partial(self.stack, source_object=self.label_21)
        self.label_20.mousePressEvent = functools.partial(self.stack, source_object=self.label_21)


        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setObjectName("salade")
        pixmap = QtGui.QPixmap('ing/legumes/salade.jpg').scaledToWidth(80)
        self.label_22.setPixmap(pixmap)
        self.label_22.setGeometry(QtCore.QRect(580, 200, 100, 100))
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(590, 290, 58, 20))
        self.label_23.setObjectName("salade")
        self.label_23.mousePressEvent = functools.partial(self.stack, source_object=self.label_23)
        self.label_22.mousePressEvent = functools.partial(self.stack, source_object=self.label_23)


        ####################################################################
        
        ####################################################################
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setObjectName("betterave")
        pixmap = QtGui.QPixmap('ing/legumes/betterave.jpg').scaledToWidth(80)
        self.label_24.setPixmap(pixmap)
        self.label_24.setGeometry(QtCore.QRect(100, 320, 100, 100))
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(110, 410, 75, 20))
        self.label_25.setObjectName("betterave")
        self.label_25.mousePressEvent = functools.partial(self.stack, source_object=self.label_25)
        self.label_24.mousePressEvent = functools.partial(self.stack, source_object=self.label_25)


        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setObjectName("epinard")
        pixmap = QtGui.QPixmap('ing/legumes/epinard.jpg').scaledToWidth(80)
        self.label_26.setPixmap(pixmap)
        self.label_26.setGeometry(QtCore.QRect(220, 320, 100, 100))
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(220, 410, 70, 20))
        self.label_27.setObjectName("epinard")
        self.label_27.mousePressEvent = functools.partial(self.stack, source_object=self.label_27)
        self.label_26.mousePressEvent = functools.partial(self.stack, source_object=self.label_27)


        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setObjectName("citron")
        pixmap = QtGui.QPixmap('ing/legumes/citron.jpg').scaledToWidth(80)
        self.label_28.setPixmap(pixmap)
        self.label_28.setGeometry(QtCore.QRect(340, 320, 100, 100))
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(360, 410, 50, 20))
        self.label_29.setObjectName("citron")
        self.label_29.mousePressEvent = functools.partial(self.stack, source_object=self.label_29)
        self.label_28.mousePressEvent = functools.partial(self.stack, source_object=self.label_29)


        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setObjectName("courgette")
        pixmap = QtGui.QPixmap('ing/legumes/courgette.jpg').scaledToWidth(80)
        self.label_30.setPixmap(pixmap)
        self.label_30.setGeometry(QtCore.QRect(460, 320, 100, 100))
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(470, 410, 75, 20))
        self.label_31.setObjectName("courgette")
        self.label_31.mousePressEvent = functools.partial(self.stack, source_object=self.label_31)
        self.label_30.mousePressEvent = functools.partial(self.stack, source_object=self.label_31)


        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setObjectName("haricot")
        pixmap = QtGui.QPixmap('ing/legumes/haricot.jpg').scaledToWidth(80)
        self.label_32.setPixmap(pixmap)
        self.label_32.setGeometry(QtCore.QRect(580, 320, 100, 100))
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(600, 410, 65, 20))
        self.label_33.setObjectName("haricot")
        self.label_33.mousePressEvent = functools.partial(self.stack, source_object=self.label_33)
        self.label_32.mousePressEvent = functools.partial(self.stack, source_object=self.label_33)


        ####################################################################


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_3.setText(_translate("Form", "Sélectionner les légumes que vous avez pour votre recette :"))
        self.label_4.setText(_translate("Form", ""))
        self.label_5.setText(_translate("Form", " Tomates "))
        self.label_6.setText(_translate("Form", ""))
        self.label_7.setText(_translate("Form", " Concombre "))
        self.label_8.setText(_translate("Form", ""))
        self.label_9.setText(_translate("Form", " Carotte "))
        self.label_10.setText(_translate("Form", ""))
        self.label_11.setText(_translate("Form", "  Ail  "))
        self.label_12.setText(_translate("Form", ""))
        self.label_13.setText(_translate("Form", " Pomme de terre "))
        self.label_14.setText(_translate("Form", ""))
        self.label_15.setText(_translate("Form", " Poivron "))
        self.label_16.setText(_translate("Form", ""))
        self.label_17.setText(_translate("Form", " Oignon "))
        self.label_18.setText(_translate("Form", ""))
        self.label_19.setText(_translate("Form", " Chou-fleur "))
        self.label_20.setText(_translate("Form", ""))
        self.label_21.setText(_translate("Form", " Aubergine "))
        self.label_22.setText(_translate("Form", ""))
        self.label_23.setText(_translate("Form", " Salades "))
        self.label_24.setText(_translate("Form", ""))
        self.label_25.setText(_translate("Form", " Betterave "))
        self.label_26.setText(_translate("Form", ""))
        self.label_27.setText(_translate("Form", " Épindard "))
        self.label_28.setText(_translate("Form", ""))
        self.label_29.setText(_translate("Form", " Citron "))
        self.label_30.setText(_translate("Form", ""))
        self.label_31.setText(_translate("Form", " Courgette "))
        self.label_32.setText(_translate("Form", ""))
        self.label_33.setText(_translate("Form", " Haricots "))


    def retour(self, event):
        print('BACK')
        # Form.close()

    def stack(self, event, source_object=None):
        if source_object.objectName() in legumes:
            source_object.setStyleSheet("")
            legumes.remove(source_object.objectName())
        else:
            source_object.setStyleSheet("color:#2a8fe9;font-weight:600")
            legumes.append(source_object.objectName())

    
    def valider(self):
        print(legumes)
        self.ingList = legumes
        self.uiMain.getKeyWords(self.ingList)
        # Form.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = VegetableSpaceFr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

