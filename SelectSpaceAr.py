from PyQt5 import QtCore, QtGui, QtWidgets
import functools
import FruitSpaceAr, VegetableSpaceAr, SpiceSpaceAr

class SelectSpaceAr(object):
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


        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(175, 180, 500, 30))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(175, 300, 500, 30))
        self.label_4.setObjectName("label_4")

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(225, 220, 150, 30))
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(375, 220, 150, 30))
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(525, 220, 150, 30))
        self.checkBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(245, 340, 100, 30))
        self.checkBox_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(355, 340, 100, 30))
        self.checkBox_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(465, 340, 100, 30))
        self.checkBox_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(575, 340, 100, 30))
        self.checkBox_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_7.setObjectName("checkBox_7")        

        self.pushButton = QtWidgets.QPushButton(Form) 
        self.pushButton.setGeometry(QtCore.QRect(175, 400, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #2fd475;\n"
"border-radius: 12px;color:#fff;font-size:14px")


        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")
        self.label_4.setStyleSheet("font-weight:500;\n"
"font-size:17px")


        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(575, 100, 70, 30))
        self.label_5.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_5.setObjectName("legumes")
        self.label_5.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_5)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(455, 100, 70, 30))
        self.label_6.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_6.setObjectName("fruits")
        self.label_6.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_6)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(325, 100, 70, 30))
        self.label_7.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_7.setObjectName("viandes")
        self.label_7.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_7)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(205, 100, 70, 30))
        self.label_8.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#000;color:#fff;border-radius:15px")
        self.label_8.setObjectName("epices")
        self.label_8.mousePressEvent = functools.partial(self.openIngSpace, source_object=self.label_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "اختر المطبخ المناسب:"))
        self.label_4.setText(_translate("Form", "اختر المكونات الغير مناسبة:"))

        self.label_5.setText(_translate("Form", "    الخضر "))
        self.label_6.setText(_translate("Form", "    الفواكه "))
        self.label_7.setText(_translate("Form", "    اللحوم "))
        self.label_8.setText(_translate("Form", "    التوابل "))

        self.checkBox.setText(_translate("Form", " طبيعي"))
        self.checkBox_2.setText(_translate("Form", " نباتي"))
        self.checkBox_3.setText(_translate("Form", " مرض السكري"))
        self.checkBox_4.setText(_translate("Form", " سمك"))
        self.checkBox_5.setText(_translate("Form", " غبﻻرب"))
        self.checkBox_6.setText(_translate("Form", " بحوم"))
        self.checkBox_7.setText(_translate("Form", " حليب"))
        self.pushButton.setText(_translate("Form", "بحث"))


        

    def retour(self, event):
        print('BACK')
        Form.close()

    def openIngSpace(self, event, source_object=None):
        source_object.setStyleSheet("font-weight:500;\n"
"font-size:15px;background-color:#2a8fe9;color:#fff;border-radius:15px")

        self.window = QtWidgets.QMainWindow()
        if source_object.objectName() == "legumes":
            self.ui = VegetableSpaceAr.VegetableSpaceAr(self)
        elif source_object.objectName() == "fruits":
            self.ui = FruitSpaceAr.FruitSpaceAr(self)
        elif source_object.objectName() == "epices":
            self.ui = SpiceSpaceAr.SpiceSpaceAr(self)
        else:
            print('Hiiii')

        self.ui.setupUi(self.window)
        self.window.show()

    def getKeyWords(self, ingList):
        self.label_8.setText(ingList[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SelectSpaceAr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

