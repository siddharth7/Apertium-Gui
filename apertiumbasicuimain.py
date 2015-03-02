# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apertiumbasicuimain.ui'
#
# Created: Sun Mar  1 13:01:47 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(538, 458)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.clr = QtGui.QPushButton(self.centralwidget)
        self.clr.setGeometry(QtCore.QRect(220, 370, 98, 27))
        self.clr.setObjectName(_fromUtf8("clr"))
        self.select1 = QtGui.QComboBox(self.centralwidget)
        self.select1.setGeometry(QtCore.QRect(140, 10, 78, 27))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.select1.setFont(font)
        self.select1.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.select1.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.select1.setObjectName(_fromUtf8("select1"))
        self.output = QtGui.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(280, 60, 241, 281))
        self.output.setObjectName(_fromUtf8("output"))
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 60, 221, 281))
        self.input.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.input.setObjectName(_fromUtf8("input"))
        self.exitbtn = QtGui.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(430, 370, 98, 27))
        self.exitbtn.setObjectName(_fromUtf8("exitbtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuHelp.addAction(self.actionOpen)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.clr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.output.clear)
        QtCore.QObject.connect(self.clr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.clr.setText(_translate("MainWindow", "Clear ", None))
        self.exitbtn.setText(_translate("MainWindow", "Exit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))

