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
        self.input = QtGui.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 60, 231, 281))
        self.input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input.setObjectName(_fromUtf8("input"))
        self.output = QtGui.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(300, 60, 211, 271))
        self.output.setText(_fromUtf8(""))
        self.output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output.setObjectName(_fromUtf8("output"))
        self.convert = QtGui.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(120, 350, 98, 27))
        self.convert.setObjectName(_fromUtf8("convert"))
        self.clr = QtGui.QPushButton(self.centralwidget)
        self.clr.setGeometry(QtCore.QRect(310, 350, 98, 27))
        self.clr.setObjectName(_fromUtf8("clr"))
        self.st = QtGui.QPushButton(self.centralwidget)
        self.st.setGeometry(QtCore.QRect(220, 380, 98, 27))
        self.st.setObjectName(_fromUtf8("st"))
        self.select1 = QtGui.QComboBox(self.centralwidget)
        self.select1.setGeometry(QtCore.QRect(40, 20, 78, 27))
        self.select1.setObjectName(_fromUtf8("select1"))
        self.select1.addItem(_fromUtf8(""))
        self.select1.addItem(_fromUtf8(""))
        self.select1.addItem(_fromUtf8(""))
        self.select1.addItem(_fromUtf8(""))
        self.select2 = QtGui.QComboBox(self.centralwidget)
        self.select2.setGeometry(QtCore.QRect(380, 20, 78, 27))
        self.select2.setObjectName(_fromUtf8("select2"))
        self.select2.addItem(_fromUtf8(""))
        self.select2.addItem(_fromUtf8(""))
        self.select2.addItem(_fromUtf8(""))
        self.select2.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.clr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.output.clear)
        QtCore.QObject.connect(self.clr, QtCore.SIGNAL(_fromUtf8("clicked()")), self.input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.convert.setText(_translate("MainWindow", "Start", None))
        self.clr.setText(_translate("MainWindow", "Clear ", None))
        self.st.setText(_translate("MainWindow", "Stop", None))
        self.select1.setItemText(0, _translate("MainWindow", "English", None))
        self.select1.setItemText(1, _translate("MainWindow", "French", None))
        self.select1.setItemText(2, _translate("MainWindow", "russian", None))
        self.select1.setItemText(3, _translate("MainWindow", "Malay", None))
        self.select2.setItemText(0, _translate("MainWindow", "English", None))
        self.select2.setItemText(1, _translate("MainWindow", "French", None))
        self.select2.setItemText(2, _translate("MainWindow", "Malay", None))
        self.select2.setItemText(3, _translate("MainWindow", "Russian", None))

