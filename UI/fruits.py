from PyQt5 import QtCore, QtGui, QtWidgets
import main
class Fruits(object):
    def setupUi(self, Form):

        iconWidth = 65

        Form.setObjectName("Form")
        Form.resize(741, 432)
        Form.setStyleSheet('background-color: white;')

        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(12)
        Form.setFont(font)

        labelFont = QtGui.QFont()
        labelFont.setPointSize(20)
        self.label = QtWidgets.QLabel(Form)
        self.label.setFont(labelFont)
        self.label.setGeometry(QtCore.QRect(30, 10, 131, 41))
        self.label.setObjectName("label")


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 390, 97, 26))
        self.pushButton.setObjectName("pushButton")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 60, 681, 301))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        labelLegFont = QtGui.QFont()
        labelLegFont.setPointSize(15)
        # self.label = QtWidgets.QLabel(Form)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(32, 55, 120, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(labelLegFont)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(169, 55, 120, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(labelLegFont)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(306, 55, 120, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(labelLegFont)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(443, 55, 120, 30))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(labelLegFont)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(580, 55, 120, 30))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(labelLegFont)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(31, 150, 120, 30))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(labelLegFont)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(169, 150, 120, 30))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(labelLegFont)

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(301, 150, 120, 30))
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(labelLegFont)

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(441, 150, 120, 30))
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(labelLegFont)

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(580, 150, 120, 30))
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(labelLegFont)

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(31, 245, 120, 30))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(labelLegFont)

        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(169, 245, 120, 30))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(labelLegFont)

        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(306, 245, 120, 30))
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(labelLegFont)

        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(443, 245, 120, 30))
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(labelLegFont)

        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(581, 245, 120, 30))
        self.label_16.setObjectName("label_16")
        self.label_16.setFont(labelLegFont)



        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(32, 113, 103, 30))
        self.checkBox.setObjectName("abricot")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        abricot = QtGui.QIcon('fruits/abricot.jpg')
        self.checkBox.setIcon(abricot)
        self.checkBox.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(169, 113, 103, 30))
        self.checkBox_2.setObjectName("banane")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        banane = QtGui.QIcon('fruits/banane.jpg')
        self.checkBox_2.setIcon(banane)
        self.checkBox_2.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(306, 113, 103, 30))
        self.checkBox_3.setObjectName("citron")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        citron  = QtGui.QIcon('fruits/citron.jpg')
        self.checkBox_3.setIcon(citron )
        self.checkBox_3.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(443, 113, 103, 30))
        self.checkBox_4.setObjectName("peche")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        peche = QtGui.QIcon('fruits/peche.jpg')
        self.checkBox_4.setIcon(peche)
        self.checkBox_4.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(580, 113, 103, 30))
        self.checkBox_5.setObjectName("pomme")
        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)
        pomme = QtGui.QIcon('fruits/pomme.jpg')
        self.checkBox_5.setIcon(pomme)
        self.checkBox_5.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setGeometry(QtCore.QRect(31, 203, 103, 30))
        self.checkBox_6.setObjectName("poire")
        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)
        poire = QtGui.QIcon('fruits/poire.jpg')
        self.checkBox_6.setIcon(poire)
        self.checkBox_6.setIconSize(QtCore.QSize(iconWidth, iconWidth))


        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setGeometry(QtCore.QRect(169, 203, 103, 30))
        self.checkBox_7.setObjectName("orange")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        orange = QtGui.QIcon('fruits/orange.jpg')
        self.checkBox_7.setIcon(orange)
        self.checkBox_7.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_8.setGeometry(QtCore.QRect(301, 203, 103, 30))
        self.checkBox_8.setObjectName("coco")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        coco = QtGui.QIcon('fruits/coco.jpg')
        self.checkBox_8.setIcon(coco)
        self.checkBox_8.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_9.setGeometry(QtCore.QRect(441, 203, 103, 30))
        self.checkBox_9.setObjectName("raisin")
        self.gridLayout.addWidget(self.checkBox_9, 1, 3, 1, 1)
        raisin = QtGui.QIcon('fruits/raisin.jpg')
        self.checkBox_9.setIcon(raisin)
        self.checkBox_9.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_10.setGeometry(QtCore.QRect(580, 203, 103, 30))
        self.checkBox_10.setObjectName("prune")
        self.gridLayout.addWidget(self.checkBox_10, 1, 4, 1, 1)
        prune = QtGui.QIcon('fruits/prune.jpg')
        self.checkBox_10.setIcon(prune)
        self.checkBox_10.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_11 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_11.setGeometry(QtCore.QRect(31, 293, 103, 30))
        self.checkBox_11.setObjectName("mandarine")
        self.gridLayout.addWidget(self.checkBox_11, 2, 0, 1, 1)
        mandarine = QtGui.QIcon('fruits/mandarine.jpg')
        self.checkBox_11.setIcon(mandarine)
        self.checkBox_11.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_12 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_12.setGeometry(QtCore.QRect(169, 293, 103, 30))
        self.checkBox_12.setObjectName("ananas")
        self.gridLayout.addWidget(self.checkBox_12, 2, 1, 1, 1)
        ananas = QtGui.QIcon('fruits/ananas.jpg')
        self.checkBox_12.setIcon(ananas)
        self.checkBox_12.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_13 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_13.setGeometry(QtCore.QRect(306, 293, 103, 30))
        self.checkBox_13.setObjectName("amande")
        self.gridLayout.addWidget(self.checkBox_13, 2, 2, 1, 1)
        amande = QtGui.QIcon('fruits/amande.jpg')
        self.checkBox_13.setIcon(amande)
        self.checkBox_13.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_14 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_14.setGeometry(QtCore.QRect(443, 293, 103, 30))
        self.checkBox_14.setObjectName("cerise")
        self.gridLayout.addWidget(self.checkBox_14, 2, 3, 1, 1)
        cerise = QtGui.QIcon('fruits/cerise.jpg')
        self.checkBox_14.setIcon(cerise)
        self.checkBox_14.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_15 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_15.setGeometry(QtCore.QRect(581, 293, 103, 30))
        self.checkBox_15.setObjectName("kiwi")
        self.gridLayout.addWidget(self.checkBox_15, 2, 4, 1, 1)
        kiwi = QtGui.QIcon('fruits/kiwi.jpg')
        self.checkBox_15.setIcon(kiwi)
        self.checkBox_15.setIconSize(QtCore.QSize(iconWidth, iconWidth))
            
        self.pushButton.clicked.connect(self.getCheckedIng)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Liste des fruits"))
        self.label.setText(_translate("Form", "Fruits"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_2.setText(_translate("Form", "Abricot"))
        self.label_3.setText(_translate("Form", "Banane"))
        self.label_4.setText(_translate("Form", "Citron"))
        self.label_5.setText(_translate("Form", "Pêche"))
        self.label_6.setText(_translate("Form", "Pomme"))
        self.label_7.setText(_translate("Form", "Poire"))
        self.label_8.setText(_translate("Form", "Orange"))
        self.label_9.setText(_translate("Form", "Noix de coco"))
        self.label_10.setText(_translate("Form", "Raisin"))
        self.label_11.setText(_translate("Form", "Prune"))
        self.label_12.setText(_translate("Form", "Mandarine"))
        self.label_13.setText(_translate("Form", "Ananas"))
        self.label_14.setText(_translate("Form", "Amande"))
        self.label_15.setText(_translate("Form", "Cerise"))
        self.label_16.setText(_translate("Form", "Kiwi"))


    def getCheckedIng(self):
        layout = self.gridLayout
        self.fruitsList = []
        for index in range(layout.count()):
            widget = layout.itemAt(index).widget()
            if (widget.isChecked()):
                self.fruitsList.append(widget.objectName()) 
        # print(self.fruitsList)
        return self.fruitsList


    def main(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Fruits()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    fruits = Fruits()
    fruits.main()
    

