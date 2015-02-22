import sys
import urllib
import re
from PyQt4 import QtCore, QtGui
from apertiumbasicuimain import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MyForm, self).__init__(parent)
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.ctimer = QtCore.QTimer()
		#QtCore.QObject.connect(self.ui.convert,QtCore.SIGNAL("clicked()"),self.constantUpdate)
		QtCore.QObject.connect(self.ui.input, QtCore.SIGNAL("textChanged(QString)"), self.constantUpdate)
		#QtCore.QObject.connect(self.ui.st, QtCore.SIGNAL("clicked()"), self.stp)

	# def dosomework(self):
	# 	#self.ctimer.start(2.000)
	# 	#self.ui.output.setText(self.ui.input.text())
	def constantUpdate(self):
		if(str(self.ui.select1.currentText())=='English' and str(self.ui.select2.currentText())=='Esparanto'):
			b='http://127.0.0.1:2737/translate?langpair=en|eo&q=%s' % (self.ui.input.text())
			response = urllib.urlopen(b)
			html = response.read()
			nestr = re.sub(r'[^a-zA-Z ]',r'',html)
			length=len(nestr.split())
			i=5
			a=''
			while(i<length):
			    a=a+nestr.split()[i]+' '
			    i+=1
			response.close() 
			self.ui.output.setText(a)
	# def stp(self):
	# 	self.ctimer.stop()
if __name__=='__main__':	
    app=QtGui.QApplication(sys.argv)
    ex=MyForm()
    ex.show()
    sys.exit(app.exec_())
