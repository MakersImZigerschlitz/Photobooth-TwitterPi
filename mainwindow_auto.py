# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setBaseSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lblOK = QtWidgets.QLabel(self.centralWidget)
        self.lblOK.setGeometry(QtCore.QRect(350, 330, 250, 16))
        self.lblOK.setObjectName("lblOK")
        self.btnPicYes = QtWidgets.QPushButton(self.centralWidget)
        self.btnPicYes.setGeometry(QtCore.QRect(180, 360, 111, 51))
        self.btnPicYes.setObjectName("btnPicYes")
        self.btnPicNo = QtWidgets.QPushButton(self.centralWidget)
        self.btnPicNo.setGeometry(QtCore.QRect(530, 360, 111, 51))
        self.btnPicNo.setObjectName("btnPicNo")
        self.lblPicture = QtWidgets.QLabel(self.centralWidget)
        self.lblPicture.setGeometry(QtCore.QRect(0, 0, 801, 281))
        self.lblPicture.setObjectName("lblPicture")
        self.lblPicture.setAlignment(QtCore.Qt.AlignCenter);
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)	
        pixmap = QtGui.QPixmap('/home/pi/image.jpg')
        pixmap = pixmap.scaledToWidth(430)
        self.lblPicture.setPixmap(pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblOK.setText(_translate("MainWindow", "Sind Sie mit dem Bild zufrieden?"))
        self.btnPicYes.setText(_translate("MainWindow", "Ja"))
        self.btnPicNo.setText(_translate("MainWindow", "Nein"))
        self.lblPicture.setText(_translate("MainWindow", "Image"))

