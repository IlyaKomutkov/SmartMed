# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FourthWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class VisualizationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        MainWindow.setToolTipDuration(4)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(450, 400, 113, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 471, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxScatter = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxScatter.setObjectName("checkBoxScatter")
        self.gridLayout.addWidget(self.checkBoxScatter, 3, 1, 1, 1)
        self.checkBoxLinear = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxLinear.setObjectName("checkBoxLinear")
        self.gridLayout.addWidget(self.checkBoxLinear, 0, 1, 1, 1)
        self.checkBoxCorr = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxCorr.setObjectName("checkBoxCorr")
        self.gridLayout.addWidget(self.checkBoxCorr, 2, 1, 1, 1)
        self.checkBoxLog = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxLog.setObjectName("checkBoxLog")
        self.gridLayout.addWidget(self.checkBoxLog, 1, 1, 1, 1)
        self.checkBoxHeatmap = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxHeatmap.setObjectName("checkBoxHeatmap")
        self.gridLayout.addWidget(self.checkBoxHeatmap, 0, 0, 1, 1)
        self.checkBoxHist = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxHist.setObjectName("checkBoxHist")
        self.gridLayout.addWidget(self.checkBoxHist, 1, 0, 1, 1)
        self.checkBoxBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxBox.setObjectName("checkBoxBox")
        self.gridLayout.addWidget(self.checkBoxBox, 2, 0, 1, 1)
        self.checkBoxBar = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxBar.setObjectName("checkBoxBar")
        self.gridLayout.addWidget(self.checkBoxBar, 3, 0, 1, 1)
        self.checkBoxDot = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxDot.setObjectName("checkBoxDot")
        self.gridLayout.addWidget(self.checkBoxDot, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Визуализация"))
        self.pushButtonDone.setText(_translate("MainWindow", "Done"))
        self.checkBoxScatter.setText(_translate(
            "MainWindow", "матрица корреляций(scatter)"))
        self.checkBoxLinear.setText(_translate(
            "MainWindow", "линейные зависимости"))
        self.checkBoxCorr.setText(_translate(
            "MainWindow", "матрица корреляций(численная)"))
        self.checkBoxLog.setText(_translate(
            "MainWindow", "логарифмические зависимости"))
        self.checkBoxHeatmap.setText(_translate("MainWindow", "хитмап"))
        self.checkBoxHist.setText(_translate("MainWindow", "гистограмма"))
        self.checkBoxBox.setText(_translate("MainWindow", "ящик усы"))
        self.checkBoxBar.setText(_translate("MainWindow", "Бар чарт"))
        self.checkBoxDot.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">Это тул тип типочек молодой цыганенок я за тобой бегал месяц мразота</p></body></html>"))
        self.checkBoxDot.setText(_translate("MainWindow", "Дот плот"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
