from PyQt5 import QtCore, QtGui, QtWidgets
import re, functools
class OneRecipeFr(object):
    def setupUi(self, Form, recipe):
        Form.setObjectName("Form")
        Form.setFixedSize(1000, 700)
        Form.setGeometry(190, 50, 1000, 700)
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
        self.label_2.setGeometry(QtCore.QRect(865, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour


        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 70, 800, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:#2a8fe9;font-size:25px;font-family:lato;font-weight:500")
        self.label_3.setText(recipe[0])

        self.labelCat = QtWidgets.QLabel(Form)
        self.labelCat.setGeometry(QtCore.QRect(110, 100, 800, 15))
        self.labelCat.setObjectName("labelCat")
        self.labelCat.setStyleSheet("color:#424242;font-size:13px;font-family:lato;font-weight:400")
        cat = ' | '.join(recipe[1])
        self.labelCat.setText(cat)

        infos = recipe[5]
        inf = re.sub(r'(Niveau : |Préparation : |Cuisson :)', '', ' '.join(infos)).split('\n')

        level, prepTime, cookTime = inf[1], inf[2], inf[3]
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 150, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color:#bdbdbd;font-size:15px;font-family:lato;font-weight:500")
        self.label_4.setText('Niveau: '+level)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(260, 120, 150, 30))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color:#bdbdbd;font-size:15px;font-family:lato;font-weight:500")
        self.label_5.setText('Préparation: '+prepTime)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(450, 120, 150, 30))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color:#bdbdbd;font-size:15px;font-family:lato;font-weight:500")
        self.label_6.setText('Cuisson: '+cookTime)


        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(110, 155, 200, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color:#424242;font-size:20px;font-family:lato;font-weight:700")


        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(110, 180, 800, 350))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color:#424242;font-size:18px;font-family:lato;font-weight:400")
        ing = ', '.join(recipe[2])
        self.label_9.setText(ing)
        self.label_9.setAlignment(QtCore.Qt.AlignTop)
        self.label_9.setWordWrap(True)


        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(110, 310, 200, 30))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("color:#424242;font-size:20px;font-family:lato;font-weight:700")


        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(110, 340, 800, 450))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color:#424242;font-size:18px;font-family:lato;font-weight:400")
        prep = ', '.join(recipe[3])
        self.label_10.setText(prep)
        self.label_10.setAlignment(QtCore.Qt.AlignTop)
        self.label_10.setWordWrap(True)

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(620, 120, 150, 30))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color:red;font-size:15px;font-family:lato;font-weight:500")
        self.label_11.mousePressEvent = functools.partial(self.youtubeOpen, recipeTitle=recipe[0])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_7.setText(_translate("Form", "Ingrédients:"))
        self.label_8.setText(_translate("Form", "Préparation:"))
        self.label_11.setText(_translate("Form", "Similaire sur youtube"))


    def youtubeOpen(self, event, recipeTitle):
        queryKeyWords = '+'.join(recipeTitle.split())
        import webbrowser 
        new = 2
        url = "https://www.youtube.com/results?search_query="+queryKeyWords
        webbrowser.get(using='chromium-browser').open(url,new=new)
        
        


    def retour(self, event):
        print('BACK')
        self.closeWindow()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

