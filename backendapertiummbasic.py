import sys
import urllib
import re
from PyQt4 import QtCore, QtGui
from apertiumbasicmainui import Ui_MainWindow


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

	def constantUpdate(self):
		if(str(self.ui.select1.currentText())=='English' and str(self.ui.select2.currentText())=='Esparanto'):
			b='http://127.0.0.1:2737/translate?langpair=en|eo&q=%s' % (self.ui.input.text())
			response = urllib.urlopen(b)
			html = response.read()
			nestr = re.sub(r'[^a-zA-Z{}?! ]',r'',html)
			#print nestr
			translatedString=''
			i=0
			flag=0
			opening_brak=0
			while(opening_brak!=2):
			    if(nestr[i]=='{'):
			        opening_brak+=1
			        #print nestr[i]
			    i+=1
			i=i+15
			while(nestr[i]!='}'):
			    translatedString=translatedString+nestr[i]
			    i+=1
			#print a
			response.close()
			self.ui.output.setText(translatedString)
if __name__=='__main__':	
    app=QtGui.QApplication(sys.argv)
    ex=MyForm()
    ex.show()
    sys.exit(app.exec_())
