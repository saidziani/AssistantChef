from PyQt5 import QtCore, QtGui, QtWidgets
import functools, SelectSpaceAr

epices = []
class SpiceSpaceAr(object):
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
        self.label_3.setGeometry(QtCore.QRect(100, 70, 500, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")

        ####################################################################

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("حار")
        pixmap = QtGui.QPixmap('ing/epices/paprikarouge.jpg').scaledToWidth(90)
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(130, 115, 100, 100))
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 215, 95, 20))
        self.label_5.setObjectName("حار")
        self.label_5.mousePressEvent = functools.partial(self.stack, source_object=self.label_5)
        self.label_4.mousePressEvent = functools.partial(self.stack, source_object=self.label_5)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("كمون")
        pixmap = QtGui.QPixmap('ing/epices/cumin.jpg').scaledToWidth(90)
        self.label_6.setPixmap(pixmap)
        self.label_6.setGeometry(QtCore.QRect(270, 115, 100, 100))
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(285, 215, 58, 20))
        self.label_7.setObjectName("كمون")
        self.label_7.mousePressEvent = functools.partial(self.stack, source_object=self.label_7)
        self.label_6.mousePressEvent = functools.partial(self.stack, source_object=self.label_7)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("فلفل")
        pixmap = QtGui.QPixmap('ing/epices/piment.jpg').scaledToWidth(90)
        self.label_8.setPixmap(pixmap)
        self.label_8.setGeometry(QtCore.QRect(410, 115, 100, 100))
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(430, 215, 55, 20))
        self.label_9.setObjectName("فلفل")
        self.label_9.mousePressEvent = functools.partial(self.stack, source_object=self.label_9)
        self.label_8.mousePressEvent = functools.partial(self.stack, source_object=self.label_9)

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("زعفران")
        pixmap = QtGui.QPixmap('ing/epices/safran.jpg').scaledToWidth(90)
        self.label_10.setPixmap(pixmap)
        self.label_10.setGeometry(QtCore.QRect(550, 115, 100, 100))
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(570, 215, 70, 20))
        self.label_11.setObjectName("زعفران")
        self.label_11.mousePressEvent = functools.partial(self.stack, source_object=self.label_11)
        self.label_10.mousePressEvent = functools.partial(self.stack, source_object=self.label_11)

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("اسود")
        pixmap = QtGui.QPixmap('ing/epices/poivrenoir.jpg').scaledToWidth(90)
        self.label_12.setPixmap(pixmap)
        self.label_12.setGeometry(QtCore.QRect(130, 255, 100, 100))
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(130, 355, 105, 20))
        self.label_13.setObjectName("اسود")
        self.label_13.mousePressEvent = functools.partial(self.stack, source_object=self.label_13)
        self.label_12.mousePressEvent = functools.partial(self.stack, source_object=self.label_13)

        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setObjectName("كزبرة")
        pixmap = QtGui.QPixmap('ing/epices/coriandre.jpg').scaledToWidth(90)
        self.label_14.setPixmap(pixmap)
        self.label_14.setGeometry(QtCore.QRect(270, 255, 100, 100))
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(284, 355, 60, 20))
        self.label_15.setObjectName("كزبرة")
        self.label_15.mousePressEvent = functools.partial(self.stack, source_object=self.label_15)
        self.label_14.mousePressEvent = functools.partial(self.stack, source_object=self.label_15)

        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("نعناع")
        pixmap = QtGui.QPixmap('ing/epices/menthe.jpg').scaledToWidth(90)
        self.label_16.setPixmap(pixmap)
        self.label_16.setGeometry(QtCore.QRect(410, 255, 100, 100))
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(425, 355, 55, 20))
        self.label_17.setObjectName("نعناع")
        self.label_17.mousePressEvent = functools.partial(self.stack, source_object=self.label_17)
        self.label_16.mousePressEvent = functools.partial(self.stack, source_object=self.label_17)

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setObjectName("احمر")
        pixmap = QtGui.QPixmap('ing/epices/paprika.jpg').scaledToWidth(90)
        self.label_18.setPixmap(pixmap)
        self.label_18.setGeometry(QtCore.QRect(550, 255, 100, 100))
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(550, 355, 105, 20))
        self.label_19.setObjectName("احمر")
        self.label_19.mousePressEvent = functools.partial(self.stack, source_object=self.label_19)
        self.label_18.mousePressEvent = functools.partial(self.stack, source_object=self.label_19)
      

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_3.setText(_translate("Form", "Sélectionner les épices que vous avez pour votre recette :"))
        self.label_4.setText(_translate("Form", ""))
        self.label_5.setText(_translate("Form", " الفلفل الحار "))
        self.label_6.setText(_translate("Form", ""))
        self.label_7.setText(_translate("Form", " الكمون "))
        self.label_8.setText(_translate("Form", ""))
        self.label_9.setText(_translate("Form", " الفلفل "))
        self.label_10.setText(_translate("Form", ""))
        self.label_11.setText(_translate("Form", " الزعفران "))
        self.label_12.setText(_translate("Form", ""))
        self.label_13.setText(_translate("Form", " الفلفل الاسود "))
        self.label_14.setText(_translate("Form", ""))
        self.label_15.setText(_translate("Form", " الكزبرة "))
        self.label_16.setText(_translate("Form", ""))
        self.label_17.setText(_translate("Form", " النعناع "))
        self.label_18.setText(_translate("Form", ""))
        self.label_19.setText(_translate("Form", " الفلفل الاحمر "))


    def retour(self, event):
        print('BACK')
        Form.close()

    def stack(self, event, source_object=None):
        if source_object.objectName() in epices:
            source_object.setStyleSheet("")
            epices.remove(source_object.objectName())
        else:
            source_object.setStyleSheet("color:#2a8fe9;font-weight:600")
            epices.append(source_object.objectName())

    def valider(self):
        print(epices)
        self.ingList = epices
        self.uiMain.getKeyWords(self.ingList)
        # Form.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SpiceSpaceAr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

