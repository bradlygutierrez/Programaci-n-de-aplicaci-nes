# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from Datos.dtProyecto import DT_proyect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

import iconosPrincipal
from entidades.proyecto import Proyecto


class Ui_proyectos(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet("background-color: rgb(20, 18, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(20, 18, 35);")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(62, 80, 291, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(77, 76, 76);\n"
                                    "border-top-left-radius: 10px;\n"
                                    "border-bottom-left-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 80, 89, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(77, 76, 76);\n"
                                      "image: url(:/iconos principal/lupa (1).png);\n"
                                      "border-top-right-radius: 10px;\n"
                                      "border-bottom-right-radius: 10px;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 80, 41, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("image: url(:/iconos principal/engranaje.png);\n"
                                        "background-color: transparent;\n"
                                        "border: none;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 80, 41, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("image: url(:/iconos principal/menos (1).png);\n"
                                        "background-color: transparent;\n"
                                        "border: none;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 80, 41, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("image: url(:/iconos principal/boton-agregar.png);\n"
                                        "background-color: transparent;\n"
                                        "border: none;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color: transparent;\n"
                                        "border: none;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(870, 480, 41, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "border-top-right-radius: 10px;\n"
                                 "border-bottom-right-radius: 10px;")
        self.label.setObjectName("label")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(680, 480, 191, 41))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border-top-left-radius: 10px;\n"
                                        "background-color: rgb(51, 209, 122);\n"
                                        "border-bottom-left-radius: 10px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 140, 851, 321))
        self.tableWidget.setStyleSheet("background-color: rgb(224, 224, 224);\n"
                                       "border-radius: 20px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><img src=\":/iconos principal/impresora (2).png\"/></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Imprimir presupuesto"))

    def cargar_proyectos(self):
        proyectos = DT_proyect.listarProyectos()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(len(proyectos))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Nombre del proyecto", "Descripcion", "Fecha Inicio", "Presupuesto Inicial", "Beneficiario"])
        self.tableWidget.setColumnWidth(0, 157)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 208)
        self.tableWidget.setColumnWidth(3, 217)
        self.tableWidget.setColumnWidth(4, 256)

        for i, proyecto in enumerate(proyectos):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(proyecto.nombre)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(proyecto.descripcion)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(proyecto.fecha_inicio)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(proyecto.presupuesto_inicial)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(proyecto.beneficiario_proyecto)))

        alignment = QtCore.Qt.AlignCenter

        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(j, i)
                if item is not None:
                    item.setTextAlignment(alignment)

    def eliminar_proyecto(self):
        row = self.tableWidget.currentRow()
        nombre = self.tableWidget.item(row, 0).text()
        Proyecto.nombre = nombre
        DT_proyect.eliminarProyecto(Proyecto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_proyectos()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.cargar_proyectos()
    sys.exit(app.exec_())
