# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarGasto.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgregarGasto(object):
    def setupUi(self, AgregarGasto):
        AgregarGasto.setObjectName("AgregarGasto")
        AgregarGasto.resize(800, 557)
        AgregarGasto.setStyleSheet("background-color: rgb(21, 15, 48);")
        self.centralwidget = QtWidgets.QWidget(AgregarGasto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 191, 21))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 130, 191, 51))
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 341, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
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
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 50, 201, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 100, 201, 21))
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 150, 201, 21))
        self.lineEdit_5.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(110, 190, 201, 21))
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 470, 291, 61))
        self.pushButton_3.setStyleSheet("font: 75 11pt \"Ubuntu Bold\";\n"
"background-color: rgb(51, 209, 122);\n"
"border-radius: 10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.pushButton_4.setStyleSheet("font: 75 11pt \"Ubuntu Bold\";\n"
"background-color: rgb(51, 209, 122);\n"
"border-radius: 10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 60, 761, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(420, 40, 261, 25))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(420, 100, 261, 25))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(350, 70, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-image: url(:/regresar/Downloads/buscar.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(370, 260, 411, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("border-radius: 10px;color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(20, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(168, 168, 168);")
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 40, 191, 21))
        self.lineEdit_7.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 80, 191, 21))
        self.lineEdit_6.setStyleSheet("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.groupBox_4.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.groupBox_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.groupBox_5.raise_()
        self.label_9.raise_()
        AgregarGasto.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AgregarGasto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        AgregarGasto.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AgregarGasto)
        self.statusbar.setObjectName("statusbar")
        AgregarGasto.setStatusBar(self.statusbar)

        self.retranslateUi(AgregarGasto)
        QtCore.QMetaObject.connectSlotsByName(AgregarGasto)

    def retranslateUi(self, AgregarGasto):
        _translate = QtCore.QCoreApplication.translate
        AgregarGasto.setWindowTitle(_translate("AgregarGasto", "MainWindow"))
        self.label.setText(_translate("AgregarGasto", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Agregar Gasto</span></p></body></html>"))
        self.label_2.setText(_translate("AgregarGasto", "Nombre"))
        self.label_3.setText(_translate("AgregarGasto", "Descripcion"))
        self.groupBox_2.setTitle(_translate("AgregarGasto", "Factura"))
        self.label_4.setText(_translate("AgregarGasto", "Referencia"))
        self.label_5.setText(_translate("AgregarGasto", "Subtotal"))
        self.label_7.setText(_translate("AgregarGasto", "IR"))
        self.checkBox.setText(_translate("AgregarGasto", "Si"))
        self.label_8.setText(_translate("AgregarGasto", "IVA"))
        self.pushButton_3.setText(_translate("AgregarGasto", "Agregar Gasto"))
        self.pushButton_4.setText(_translate("AgregarGasto", "Volver"))
        self.groupBox_4.setTitle(_translate("AgregarGasto", "Información del Gasto"))
        self.label_6.setText(_translate("AgregarGasto", "Selecciona un rubro para el Gasto agregado"))
        self.comboBox_2.setItemText(0, _translate("AgregarGasto", "Transporte"))
        self.comboBox_2.setItemText(1, _translate("AgregarGasto", "Tecnología"))
        self.comboBox_2.setItemText(2, _translate("AgregarGasto", "Materiales"))
        self.label_12.setText(_translate("AgregarGasto", "<html><head/><body><p align=\"center\">Seleccione la etapa</p></body></html>"))
        self.groupBox_5.setTitle(_translate("AgregarGasto", "Beneficiario"))
        self.label_11.setText(_translate("AgregarGasto", "Nombre"))
        self.label_10.setText(_translate("AgregarGasto", "ID"))
import CambiarContra


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarGasto = QtWidgets.QMainWindow()
    ui = Ui_AgregarGasto()
    ui.setupUi(AgregarGasto)
    AgregarGasto.show()
    sys.exit(app.exec_())
