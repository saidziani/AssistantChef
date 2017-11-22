from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Epices(object):
    def setupUi(self, Form):

        iconWidth = 85

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
        self.label_2.setGeometry(QtCore.QRect(32, 70, 125, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(labelLegFont)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(169, 70, 125, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(labelLegFont)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(306, 70, 125, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(labelLegFont)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(443, 70, 125, 30))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(labelLegFont)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(580, 70, 125, 30))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(labelLegFont)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(31, 200, 125, 30))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(labelLegFont)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(169, 200, 125, 30))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(labelLegFont)

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(301, 200, 125, 30))
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(labelLegFont)



        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(32, 113, 103, 30))
        self.checkBox.setObjectName("cumin")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        cumin = QtGui.QIcon('epices/cumin.jpg')
        self.checkBox.setIcon(cumin)
        self.checkBox.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(169, 113, 103, 30))
        self.checkBox_2.setObjectName("menthe")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        menthe = QtGui.QIcon('epices/menthe.jpg')
        self.checkBox_2.setIcon(menthe)
        self.checkBox_2.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(306, 113, 103, 30))
        self.checkBox_3.setObjectName("paprika")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        paprika  = QtGui.QIcon('epices/paprika.jpg')
        self.checkBox_3.setIcon(paprika )
        self.checkBox_3.setIconSize(QtCore.QSize(iconWidth, iconWidth))

        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(443, 113, 103, 30))
        self.checkBox_4.setObjectName("piment")
        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)
        piment = QtGui.QIcon('epices/piment.jpg')
        self.checkBox_4.setIcon(piment)
        self.checkBox_4.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(580, 113, 103, 30))
        self.checkBox_5.setObjectName("poivrenoir")
        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)
        poivrenoir = QtGui.QIcon('epices/poivrenoir.jpg')
        self.checkBox_5.setIcon(poivrenoir)
        self.checkBox_5.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setGeometry(QtCore.QRect(31, 203, 103, 30))
        self.checkBox_6.setObjectName("safran")
        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)
        safran = QtGui.QIcon('epices/safran.jpg')
        self.checkBox_6.setIcon(safran)
        self.checkBox_6.setIconSize(QtCore.QSize(iconWidth, iconWidth))


        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setGeometry(QtCore.QRect(169, 203, 103, 30))
        self.checkBox_7.setObjectName("coriandre")
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)
        coriandre = QtGui.QIcon('epices/coriandre.jpg')
        self.checkBox_7.setIcon(coriandre)
        self.checkBox_7.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_8.setGeometry(QtCore.QRect(301, 203, 103, 30))
        self.checkBox_8.setObjectName("paprikarouge")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        paprikarouge = QtGui.QIcon('epices/paprikarouge.jpg')
        self.checkBox_8.setIcon(paprikarouge)
        self.checkBox_8.setIconSize(QtCore.QSize(iconWidth, iconWidth))
        
        self.pushButton.clicked.connect(self.getCheckedIng)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Liste des épices"))
        self.label.setText(_translate("Form", "epices"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_2.setText(_translate("Form", "Cumin"))
        self.label_3.setText(_translate("Form", "Menthe"))
        self.label_4.setText(_translate("Form", "Paprika"))
        self.label_5.setText(_translate("Form", "Piment"))
        self.label_6.setText(_translate("Form", "Poivre noir"))
        self.label_7.setText(_translate("Form", "safran"))
        self.label_8.setText(_translate("Form", "Coriandre"))
        self.label_9.setText(_translate("Form", "Paprika rouge"))


    def getCheckedIng(self):
        layout = self.gridLayout
        self.epicesList = []
        for index in range(layout.count()):
            widget = layout.itemAt(index).widget()
            if (widget.isChecked()):
                self.epicesList.append(widget.objectName()) 
        print(self.epicesList)
        return self.epicesList


    def main(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Epices()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    epices = Epices()
    epices.main()
    

