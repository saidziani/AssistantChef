from PyQt5 import QtCore, QtGui, QtWidgets
import Application, SearchSpaceAr, SelectSpaceAr

class ArabicApp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #424242;")
        self.closeWindow = Form.close

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 330, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 310, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(720, 20, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 200, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(520, 200, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")



        pixmap = QtGui.QPixmap('MonChef-logo.png').scaledToWidth(90)
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label_3.setPixmap(pixmap1)
        self.label_3.setGeometry(QtCore.QRect(25, 15, 20, 20))

        pixmap2 = QtGui.QPixmap('chef-ingredient.png').scaledToWidth(185)
        self.label_5.setPixmap(pixmap2)
        self.label_5.setGeometry(QtCore.QRect(460, 100, 210, 210))

        pixmap3 = QtGui.QPixmap('chef-recette.png').scaledToWidth(160)
        self.label_6.setPixmap(pixmap3)
        self.label_6.setGeometry(QtCore.QRect(160, 100, 210, 210))

        self.label.setGeometry(QtCore.QRect(100, 250, 210, 210))
        self.label_2.setGeometry(QtCore.QRect(400, 250, 210, 210))

        self.label.setStyleSheet("font-weight:600")
        self.label_2.setStyleSheet("font-weight:600")

        self.label.mousePressEvent = self.openRec
        self.label_2.mousePressEvent = self.openIng

        self.label_6.mousePressEvent = self.openRec
        self.label_5.mousePressEvent = self.openIng

        self.label_3.mousePressEvent = self.retour



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", "البحث عن وصفة"))
        self.label_2.setText(_translate("Form", "البحث عن وصفة\n     بمكوناتها  "))
        self.label_3.setText(_translate("Form", ""))
        self.label_4.setText(_translate("Form", ""))
        self.label_5.setText(_translate("Form", ""))
        self.label_6.setText(_translate("Form", ""))

    def openRec(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = SearchSpaceAr.SearchSpaceAr()
        self.ui.setupUi(self.window)
        self.window.show()

    def openIng(self, event):
        self.window = QtWidgets.QMainWindow()
        self.ui = SelectSpaceAr.SelectSpaceAr()
        self.ui.setupUi(self.window)
        self.window.show()

    def retour(self, event):
        print('BACK')
        self.closeWindow()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ArabicApp()
    ui.setupUi(Form)
    # Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

