# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarGasto.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 557)
        MainWindow.setStyleSheet("background-color: rgb(20, 18, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 191, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 191, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 90, 391, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 40, 131, 21))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: Black")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(30, 70, 171, 21))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 50, 141, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(145, 65, 172);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 361, 101))
        self.tableWidget.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 311, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 50, 201, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 100, 211, 21))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 150, 211, 21))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 200, 211, 21))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 460, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(35, 134, 54);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 350, 391, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 211, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.pushButton.setStyleSheet("border-image: url(:/iconosalida/cerrar-sesion.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Agregar Gasto"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "Descripcion"))
        self.groupBox.setTitle(_translate("MainWindow", "Beneficiario"))
        self.label_8.setText(_translate("MainWindow", "Nombre"))
        self.label_9.setText(_translate("MainWindow", "ID"))
        self.pushButton_4.setText(_translate("MainWindow", "Agregar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Factura"))
        self.label_4.setText(_translate("MainWindow", "Referencia"))
        self.label_5.setText(_translate("MainWindow", "Subtotal"))
        self.label_6.setText(_translate("MainWindow", "IVA"))
        self.label_7.setText(_translate("MainWindow", "IR"))
        self.pushButton_3.setText(_translate("MainWindow", "Agregar Gasto"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Rubro"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Transporte"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tecnologia"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Materiales"))
import salida_rc