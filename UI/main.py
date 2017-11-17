# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talntest.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 375)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 200, 571, 24))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_9.setEnabled(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_4.addWidget(self.checkBox_9, 0, 3, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_4.addWidget(self.checkBox_10, 0, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_11.setEnabled(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_4.addWidget(self.checkBox_11, 0, 2, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_12.setEnabled(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_4.addWidget(self.checkBox_12, 0, 1, 1, 1)

        
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(70, 80, 631, 24))
        self.widget.setObjectName("widget")


        


        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(Form)

        #Second CheckBox list
        self.widget1.setEnabled(True)
        self.widget1.setGeometry(QtCore.QRect(90, 200, 571, 24))
        self.widget1.setObjectName("widget1")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.checkBox_4 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 3, 1, 1)

        self.checkBox_1 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setObjectName("fruit")
        self.gridLayout_2.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_3 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 300, 97, 26))
        self.pushButton.setObjectName("pushButton")

        self.widget1.setHidden(True)
        self.layoutWidget.setHidden(True)

        self.radioButton.clicked.connect(self.widget1.show)
        self.radioButton.clicked.connect(self.layoutWidget.hide)

        self.radioButton_2.clicked.connect(self.layoutWidget.show)
        self.radioButton_2.clicked.connect(self.widget1.hide)
        self.pushButton.clicked.connect(self.getCheckedIng)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.radioButton_2.setText(_translate("Form", "Viandes"))
        self.checkBox_9.setText(_translate("Form", ""))
        self.checkBox_10.setText(_translate("Form", "CheckBox2"))
        self.checkBox_11.setText(_translate("Form", "CheckBox3"))
        self.checkBox_12.setText(_translate("Form", "CheckBox4"))

        self.radioButton.setText(_translate("Form", "Légumes"))
        self.checkBox_4.setText(_translate("Form", "CheckBox5"))
        self.checkBox_1.setText(_translate("Form", "CheckBox6"))
        self.checkBox_3.setText(_translate("Form", "CheckBox7"))
        self.checkBox_2.setText(_translate("Form", "CheckBox8"))

        self.pushButton.setText(_translate("Form", "PushButton"))


        icon = QtGui.QIcon('avatar.png')
        self.checkBox_9.setIcon(icon)



    def getCheckedIng(self):
        if self.radioButton.isChecked():
            layout = self.gridLayout_2
            legumes = []
            for index in range(layout.count()):
                widget = layout.itemAt(index).widget()
                if (widget.isChecked()):
                    legumes.append(widget.objectName()) 
            print(legumes)

        
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

