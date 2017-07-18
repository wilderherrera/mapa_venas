# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafica.ui'
#
# Created: Fri Jun 09 12:01:49 2017
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(965, 667)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 180, 261, 221))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("unillanos.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 281, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 25pt \"Microsoft Tai Le\";"))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Control De Acceso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.inicia = QtGui.QPushButton(self.centralwidget)
        self.inicia.setGeometry(QtCore.QRect(430, 110, 141, 51))
        self.inicia.setMouseTracking(False)
        self.inicia.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.inicia.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"border:5;\n"
"\n"
""))
        self.inicia.setText(QtGui.QApplication.translate("MainWindow", "Iniciar Sistema", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../ProyectosAngular2/proyecto_angular/src/image/policia.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inicia.setIcon(icon)
        self.inicia.setIconSize(QtCore.QSize(30, 30))
        self.inicia.setObjectName(_fromUtf8("inicia"))
        self.abre_excel = QtGui.QPushButton(self.centralwidget)
        self.abre_excel.setGeometry(QtCore.QRect(400, 430, 211, 51))
        self.abre_excel.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"border:5;"))
        self.abre_excel.setText(QtGui.QApplication.translate("MainWindow", "Registro De Acceso", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("reg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abre_excel.setIcon(icon1)
        self.abre_excel.setIconSize(QtCore.QSize(40, 40))
        self.abre_excel.setObjectName(_fromUtf8("abre_excel"))
        self.salir = QtGui.QPushButton(self.centralwidget)
        self.salir.setGeometry(QtCore.QRect(760, 570, 161, 51))
        self.salir.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"border-radius:5;"))
        self.salir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Logos/salir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salir.setIcon(icon2)
        self.salir.setIconSize(QtCore.QSize(20, 20))
        self.salir.setObjectName(_fromUtf8("salir"))
        self.letras = QtGui.QLabel(self.centralwidget)
        self.letras.setGeometry(QtCore.QRect(10, 580, 341, 41))
        self.letras.setStyleSheet(_fromUtf8("font: 15pt \"MS Shell Dlg 2\";"))
        self.letras.setText(QtGui.QApplication.translate("MainWindow", "Esperando Visitantes...", None, QtGui.QApplication.UnicodeUTF8))
        self.letras.setObjectName(_fromUtf8("letras"))
        self.regis = QtGui.QPushButton(self.centralwidget)
        self.regis.setGeometry(QtCore.QRect(430, 550, 161, 51))
        self.regis.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"border:5;"))
        self.regis.setText(QtGui.QApplication.translate("MainWindow", "Registrar Visitante", None, QtGui.QApplication.UnicodeUTF8))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Logos/reg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.regis.setIcon(icon3)
        self.regis.setIconSize(QtCore.QSize(20, 20))
        self.regis.setObjectName(_fromUtf8("regis"))
        self.caja = QtGui.QTextEdit(self.centralwidget)
        self.caja.setEnabled(False)
        self.caja.setGeometry(QtCore.QRect(400, 500, 211, 31))
        self.caja.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";"))
        self.caja.setObjectName(_fromUtf8("caja"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(760, 480, 161, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Imagen1.jpg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.salir, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

