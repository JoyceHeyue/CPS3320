from PyQt5 import QtCore, QtWidgets

class Ui_Package(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 222)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 109, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 109, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 79, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 79, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 49, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 49, 111, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 109, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Add"))
        self.label.setText(_translate("Form", "Money 1"))
        self.label_2.setText(_translate("Form", "Money 2"))
        self.label_3.setText(_translate("Form", "Vegetable Combo"))
        self.label_4.setText(_translate("Form", "Fruit Combo"))
        self.pushButton_3.setText(_translate("Form", "Return"))
