import sys
import urllib
import re
from PyQt4 import QtCore, QtGui
from apertiumbasicuimain import Ui_MainWindow

class errorform(QtGui.QDialog):
    def __init__(self, parent=None):
        super(errorform, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
   
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("This language pair is not available or the localhost server is not running, please refer to docs, http://wiki.apertium.org/wiki/Apertium-apy or http://wiki.apertium.org/wiki/List_of_language_pairs")
        
        
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
       
class MyForm(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MyForm, self).__init__(parent)
		
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.dialogTextBrowser = errorform(self)
		QtCore.QObject.connect(self.ui.input, QtCore.SIGNAL("textChanged(QString)"), self.constantUpdate)
		QtCore.QObject.connect(self.ui.showerror, QtCore.SIGNAL("clicked()"), self.posterror)

		
	def constantUpdate(self):

		if(str(self.ui.select1.currentText())=='English' and str(self.ui.select2.currentText())=='Esparanto'):
			self.ui.showerror.setStyleSheet("background-color: white")
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
		elif(str(self.ui.select1.currentText())=='Welsh' and str(self.ui.select2.currentText())=='English'):
			self.ui.showerror.setStyleSheet("background-color: white")
			b='http://127.0.0.1:2737/translate?langpair=cym|eng&q=%s' % (self.ui.input.text())
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
		else:
			self.ui.showerror.setStyleSheet("background-color: red")
			self.posterror()
	def posterror(self):

		self.dialogTextBrowser.exec_()

if __name__=='__main__':	
    app=QtGui.QApplication(sys.argv)

    app.setApplicationName('Apertium Translator Tool')
    ex=MyForm()
    ex.show()
    sys.exit(app.exec_())
