'''
backend for apertium gui
'''
import sys
import json
from requests import get
from PyQt4 import QtCore, QtGui
from apertiumbasicuimain import Ui_MainWindow
LANG_DICT = {"eng":"english",
             "epo":"esparanto",
             "cym":"welsh",
             "kaz":"kazak",
             "tat":"tatar",
             }
INV_LANG_DICT = {v: k for k, v in LANG_DICT.items()}
class MyForm(QtGui.QMainWindow):
    '''
    main window setup
    '''
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.input,
                               QtCore.SIGNAL("textChanged(QString)"), self.translate_func)
        self.add_pairs()
    def add_pairs(self):
        '''
        extract available language pairs
        '''
        list1 = []
        urllink = 'http://127.0.0.1:2737/listPairs'
        response = json.loads(get(urllink).text)["responseData"]
        for res in response:
            langpair = ''
            srclang = res["sourceLanguage"]
            trglang = res["targetLanguage"]
            for key in LANG_DICT.keys():
                if key == srclang:
                    langpair = langpair + LANG_DICT[key]
            if langpair == '':
                langpair = langpair + res["sourceLanguage"]
            langpair = langpair + '  -->  '
            for key in LANG_DICT.keys():
                if key == trglang:
                    langpair = langpair + LANG_DICT[key]
            if langpair[-1:] == ' ':
                langpair = langpair + trglang
            list1.append(langpair)
        self.ui.select1.addItems(list1)
    def translate_func(self):
        '''
        translate text
        '''
        if self.ui.select1.currentText():
            currentpair = str(self.ui.select1.currentText())
            text1 = ''
            text2 = ''
            flag = 1
            for k in range(len(currentpair)):
                if currentpair[k] != ' ' and flag == 1:
                    text1 = text1 + currentpair[k]
                elif currentpair[k] == ' ':
                    flag = 0
                elif flag == 0:
                    text2 = text2 + currentpair[k]
            text2 = text2[3:]
            for key in INV_LANG_DICT.keys():
                if key == text1:
                    text1 = INV_LANG_DICT[text1]
            for key in INV_LANG_DICT.keys():
                if key == text2:
                    text2 = INV_LANG_DICT[text2]
            urllink = 'http://127.0.0.1:2737/translate?langpair=%s|%s&q=%s' % (text1, text2, self.ui.input.text())
            response = json.loads(get(urllink).text)["responseData"]
            translatedstring = response["translatedText"]
            self.ui.output.setText(translatedstring)
        else:
            self.ui.output.setText(self.ui.input.text())
if __name__ == '__main__':
    APP = QtGui.QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(APP.exec_())
