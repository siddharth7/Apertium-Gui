import sys

from PyQt4 import QtCore, QtGui
from apertiumbasicuimain import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MyForm, self).__init__(parent)
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.ctimer = QtCore.QTimer()
		QtCore.QObject.connect(self.ui.convert,QtCore.SIGNAL("clicked()"), self.dosomework)
		QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.constantUpdate)
		QtCore.QObject.connect(self.ui.st, QtCore.SIGNAL("clicked"), self.stp)

	def dosomework(self):
		self.ctimer.start(0.1000)
		#self.ui.output.setText(self.ui.input.text())
	def constantUpdate(self):
		self.ui.output.setText(self.ui.input.text())
	def stp(self):
		self.ctimer.stop()
if __name__=='__main__':	
    app=QtGui.QApplication(sys.argv)
    ex=MyForm()
    ex.show()
    #timer.singleShot(60000, self.convert_func)
    sys.exit(app.exec_())
