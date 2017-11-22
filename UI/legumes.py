from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Legumes(object):

    def __init__(self, uiMain):
        self.uiMain = uiMain
        
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
        self.checkBox.setObjectName("ail")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        ail = QtGui.QIcon('legumes/ail.jpg')
        self.checkBox.setIcon(ail)
        self.checkBox.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(169, 113, 103, 30))
        self.checkBox_2.setObjectName("tomate")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        tomate = QtGui.QIcon('legumes/tomate.jpg')
        self.checkBox_2.setIcon(tomate)
        self.checkBox_2.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(306, 113, 103, 30))
        self.checkBox_3.setObjectName("pomme2terre")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        pomme2terre = QtGui.QIcon('legumes/pomme2terre.jpg')
        self.checkBox_3.setIcon(pomme2terre)
        self.checkBox_3.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(443, 113, 103, 30))
        self.checkBox_4.setObjectName("oignon")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        oignon = QtGui.QIcon('legumes/oignon.jpg')
        self.checkBox_4.setIcon(oignon)
        self.checkBox_4.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(580, 113, 103, 30))
        self.checkBox_5.setObjectName("carotte")
        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)
        carotte = QtGui.QIcon('legumes/carotte.jpg')
        self.checkBox_5.setIcon(carotte)
        self.checkBox_5.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setGeometry(QtCore.QRect(31, 203, 103, 30))
        self.checkBox_6.setObjectName("salades")
        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)
        salades = QtGui.QIcon('legumes/salade.jpg')
        self.checkBox_6.setIcon(salades)
        self.checkBox_6.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setGeometry(QtCore.QRect(169, 203, 103, 30))
        self.checkBox_7.setObjectName("poivron")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        poivron = QtGui.QIcon('legumes/poivron.jpg')
        self.checkBox_7.setIcon(poivron)
        self.checkBox_7.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_8.setGeometry(QtCore.QRect(301, 203, 103, 30))
        self.checkBox_8.setObjectName("concombre")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        concombre = QtGui.QIcon('legumes/concombre.jpg')
        self.checkBox_8.setIcon(concombre)
        self.checkBox_8.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_9.setGeometry(QtCore.QRect(441, 203, 103, 30))
        self.checkBox_9.setObjectName("choufleur")
        self.gridLayout.addWidget(self.checkBox_9, 1, 3, 1, 1)
        choufleur = QtGui.QIcon('legumes/choufleur.jpg')
        self.checkBox_9.setIcon(choufleur)
        self.checkBox_9.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_10.setGeometry(QtCore.QRect(580, 203, 103, 30))
        self.checkBox_10.setObjectName("courgette")
        self.gridLayout.addWidget(self.checkBox_10, 1, 4, 1, 1)
        courgette = QtGui.QIcon('legumes/courgette.jpg')
        self.checkBox_10.setIcon(courgette)
        self.checkBox_10.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_11 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_11.setGeometry(QtCore.QRect(31, 293, 103, 30))
        self.checkBox_11.setObjectName("betterave")
        self.gridLayout.addWidget(self.checkBox_11, 2, 0, 1, 1)
        betterave = QtGui.QIcon('legumes/betterave.jpg')
        self.checkBox_11.setIcon(betterave)
        self.checkBox_11.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_12 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_12.setGeometry(QtCore.QRect(169, 293, 103, 30))
        self.checkBox_12.setObjectName("aubergine")
        self.gridLayout.addWidget(self.checkBox_12, 2, 1, 1, 1)
        aubergine = QtGui.QIcon('legumes/aubergine.jpg')
        self.checkBox_12.setIcon(aubergine)
        self.checkBox_12.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_13 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_13.setGeometry(QtCore.QRect(306, 293, 103, 30))
        self.checkBox_13.setObjectName("asperge")
        self.gridLayout.addWidget(self.checkBox_13, 2, 2, 1, 1)
        asperge = QtGui.QIcon('legumes/asperge.jpg')
        self.checkBox_13.setIcon(asperge)
        self.checkBox_13.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_14 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_14.setGeometry(QtCore.QRect(443, 293, 103, 30))
        self.checkBox_14.setObjectName("haricot")
        self.gridLayout.addWidget(self.checkBox_14, 2, 3, 1, 1)
        haricot = QtGui.QIcon('legumes/haricot.jpg')
        self.checkBox_14.setIcon(haricot)
        self.checkBox_14.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_15 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_15.setGeometry(QtCore.QRect(581, 293, 103, 30))
        self.checkBox_15.setObjectName("artichaut")
        self.gridLayout.addWidget(self.checkBox_15, 2, 4, 1, 1)
        artichaut = QtGui.QIcon('legumes/artichaut.jpg')
        self.checkBox_15.setIcon(artichaut)
        self.checkBox_15.setIconSize(QtCore.QSize(iconWidth, iconWidth))
            
        self.pushButton.clicked.connect(self.getCheckedIng)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Liste des légumes"))
        self.label.setText(_translate("Form", "Légumes"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_2.setText(_translate("Form", "Ail"))
        self.label_3.setText(_translate("Form", "Tomate"))
        self.label_4.setText(_translate("Form", "Patate"))
        self.label_5.setText(_translate("Form", "Oignon"))
        self.label_6.setText(_translate("Form", "Carotte"))
        self.label_7.setText(_translate("Form", "Salades"))
        self.label_8.setText(_translate("Form", "Poivron"))
        self.label_9.setText(_translate("Form", "Concombre"))
        self.label_10.setText(_translate("Form", "Chou-fleur"))
        self.label_11.setText(_translate("Form", "Courgette"))
        self.label_12.setText(_translate("Form", "Betterave"))
        self.label_13.setText(_translate("Form", "Aubergine"))
        self.label_14.setText(_translate("Form", "Asperge"))
        self.label_15.setText(_translate("Form", "Haricot"))
        self.label_16.setText(_translate("Form", "Artichaut"))


    def getCheckedIng(self):
        layout = self.gridLayout
        self.legumesList = []
        for index in range(layout.count()):
            widget = layout.itemAt(index).widget()
            if (widget.isChecked()):
                self.legumesList.append(widget.objectName()) 
        self.uiMain.showLegumes(self.legumesList)
        return self.legumesList


    def main(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Legumes()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    legumes = Legumes()
    legumes.main()
    

