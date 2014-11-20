# -*- coding: utf-8 -*-
import tweepy
from lxml import etree
from xml.etree.ElementTree import Element, ElementTree
from xml.dom import minidom
import xml.etree.ElementTree as ET
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import mainwindow

	#Authorization Key/Token for Twitter requests
CONSUMER_KEY ="rCL84xdkVKzEjJML1mavTV1Cz"
CONSUMER_SECRET ="0rr7VxMzwGp5zAeuNAAgNx99wIFHk7EolsD2cEeJJoLMIssX5B"
ACCESS_TOKEN ="251142396-cjjq9jzNIx7Iad93lhvigbTtsGWWzUSxYOqVGyZb"
ACCESS_TOKEN_SECRET ="ciNwHD3cV1rVtjELYcEo6Oq7cM4kBAjxCt0OtPhFOodVQ"

	#Number of posts taken
N_POSTS = 5

	#Authorization process for Twitter requests
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

	#GUI definition
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

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Twitta"))
        MainWindow.resize(793, 655)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 421, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 110, 171, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 80, 116, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 131, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 151, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 110, 151, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 20, 116, 22))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 40, 116, 22))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 60, 116, 22))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 80, 116, 22))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 110, 141, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.radioButton_9 = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 50, 116, 22))
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 60, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.handleButton)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 220, 771, 371))
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(560, 110, 120, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radioButton_10 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.radioButton_11 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 50, 116, 22))
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 30, 611, 20))
        self.label.setText(_fromUtf8("Digite o Nome do Usuário ou Palavra Chave (sem '@' ou '#'):"))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(590, 60, 60, 27))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 30, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton.setChecked)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton_2.setChecked)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton_3.setChecked)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton_4.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Twitta", "Twitta", None))
        self.groupBox.setTitle(_translate("MainWindow", "Critério de Busca", None))
        self.radioButton_3.setText(_translate("MainWindow", "Trends", None))
        self.radioButton_2.setText(_translate("MainWindow", "Palavra Chave", None))
        self.radioButton.setText(_translate("MainWindow", "Posts por Usuário", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ordenar por", None))
        self.radioButton_4.setText(_translate("MainWindow", "Nome", None))
        self.radioButton_5.setText(_translate("MainWindow", "Data", None))
        self.radioButton_6.setText(_translate("MainWindow", "Retweets", None))
        self.radioButton_7.setText(_translate("MainWindow", "Favoritos", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ordem", None))
        self.radioButton_8.setText(_translate("MainWindow", "Decrescente", None))
        self.radioButton_9.setText(_translate("MainWindow", "Crescente", None))
        self.pushButton.setText(_translate("MainWindow", "Buscar", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Trends", None))
        self.radioButton_10.setText(_translate("MainWindow", "Mundo", None))
        self.radioButton_11.setText(_translate("MainWindow", "Brasil", None))
        self.label_2.setText(_translate("MainWindow", " Qtde:", None))

    def handleButton(self):
	global N_POSTS
	N_POSTS = self.spinBox.value()
	if self.radioButton.isChecked():
		if self.radioButton_4.isChecked():
			self.radioButton_5.setChecked(True)
			self.statusbar.showMessage('Pesquisas por usuario ja sao ordenadas por nome.', msecs = 6000)
		if self.radioButton_5.isChecked():
			name = self.lineEdit.text()
			getData(str(name))
			if self.radioButton_9.isChecked():
				stringao = listPosts(cres = False)
			else: 
				stringao = listPosts()
			self.plainTextEdit.setPlainText(stringao)
		if self.radioButton_6.isChecked():
			name = self.lineEdit.text()
			getData(str(name))
			if self.radioButton_9.isChecked():
				stringao = listPostsRt(cres = False)
			else: 
				stringao = listPostsRt()
			self.plainTextEdit.setPlainText(stringao)
		if self.radioButton_7.isChecked():
			name = self.lineEdit.text()
			getData(str(name))
			if self.radioButton_9.isChecked():
				stringao = listPostsFavs(cres = False)
			else: 
				stringao = listPostsFavs()
			self.plainTextEdit.setPlainText(stringao)
	if self.radioButton_2.isChecked():
		if self.radioButton_4.isChecked():
			name = self.lineEdit.text()
			getKeywords(str(name))
			if self.radioButton_9.isChecked():
				stringao = ordena(cres = False)
			else: 
				stringao = ordena()
			self.plainTextEdit.setPlainText(stringao)
		if self.radioButton_5.isChecked():
			name = self.lineEdit.text()
			getKeywords(str(name))
			if self.radioButton_9.isChecked():
				stringao = ordenaData(cres = False)
			else: 
				stringao = ordenaData()
			self.plainTextEdit.setPlainText(stringao)
		if self.radioButton_6.isChecked():
			name = self.lineEdit.text()
			getKeywords(str(name))
			if self.radioButton_9.isChecked():
				stringao = ordenaPopularidade(cres = False)
			else: 
				stringao = ordenaPopularidade()
			self.plainTextEdit.setPlainText(stringao)
		if self.radioButton_7.isChecked():
			name = self.lineEdit.text()
			getKeywords(str(name))
			if self.radioButton_9.isChecked():
				stringao = ordenaCarisma(cres = False)
			else: 
				stringao = ordenaCarisma()
			self.plainTextEdit.setPlainText(stringao)
	if self.radioButton_3.isChecked():
		if self.radioButton_11.isChecked():
			stringao = getTrends(brazil = True)
		else: 
			self.radioButton_10.setChecked(True)
			stringao = getTrends(brazil = False)
		self.plainTextEdit.setPlainText(stringao)
	
	#End of GUI definition

tree = ElementTree()

	#Main definition
def main():
	app = QtGui.QApplication(sys.argv)
	form = Ui_MainWindow()
	form.show()
	app.exec_()

	#Takes a defined user's data
def getData(user_name):
	public_tweets = api.user_timeline(user_name, count = N_POSTS)
	root = Element(user_name)
	i = 1
	for tweet in public_tweets:
		ID = Element("id", ID = str(i))
		post = Element('post', text = tweet.text)
		date = Element('date', date = str(tweet.created_at))
		retweets = Element('retweets', retweets = str(tweet.retweet_count))
		favorites = Element('favorites', favorites = str(tweet.favorite_count))
		root.append(ID)		
		ID.append(post)
		ID.append(date)
		ID.append(retweets)
		ID.append(favorites)
		
		ElementTree(root).write('output.xhtml')
		i = i +1
	
	#Gets the string input for other functions
def getKeywords(keyword):
	public_tweets = api.search(q = keyword, lang = "pt", count = N_POSTS, show_user = True)
	root = Element(str(keyword))
	i = 1
	for tweet in public_tweets:
		ID = Element("id", ID = str(i))
		name = Element("name", name = str(tweet.user.screen_name))
		post = Element('post', text = tweet.text)
		date = Element('date', date = str(tweet.created_at))
		retweets = Element('retweets', retweets = str(tweet.retweet_count))
		favorites = Element('favorites', favorites = str(tweet.favorite_count))
		root.append(ID)
		ID.append(name)
		ID.append(post)
		ID.append(date)
		ID.append(retweets)
		ID.append(favorites)

		ElementTree(root).write('Keywords.xhtml')
		i = i +1 

	#Lists an user's posts by Date
def listPosts(cres = True):
	root = ET.parse("output.xhtml")
	ids = root.findall("id") 
	ldate = []
	stringao = ""
	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('date')
		tag_atrib = tag.attrib['date']
		ldate.append([tag_atrib, ident])
	heapsort(ldate)
	if cres == True:
		ldate = ldate[::-1]
	for cont in range(len(ldate)):
		for j in ids:
			ind = j.get("ID")
			if ldate[cont][1] == ind:
				ind_date = j.find('date')
				atr_date = ind_date.attrib['date']
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				stringao = stringao + str(atr_date) + " -> " + atr_post + "\n"
	return stringao

	#Lists an user's posts by Retweets
def listPostsRt(cres = True):
	stringao = ""
	root = ET.parse("output.xhtml")
	ids = root.findall("id")
	lrt = []
	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('retweets')
		tag_atrib = tag.attrib['retweets']
		lrt.append([(str(int(tag_atrib) + 100000)), ident])
	heapsort(lrt)
	if cres == True:
		lrt = lrt[::-1]
	for cont in range(len(lrt)):
		lrt[cont][0] = str(int(lrt[cont][0]) - 100000)
		for j in ids:
			ind = j.get("ID")
			if lrt[cont][1] == ind:
				ind_rt = j.find('retweets')
				atr_rt = str(int(ind_rt.attrib['retweets']))
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				stringao = stringao + " Rts: " + str(atr_rt) + " -> " + atr_post + "\n"
	return stringao

	#Lists an user's posts by Favorites
def listPostsFavs(cres = True):
	root = ET.parse("output.xhtml")
	ids = root.findall("id")
	lfave = []
	stringao = ""
	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('favorites')
		tag_atrib = tag.attrib['favorites']
		lfave.append([tag_atrib, ident])
	heapsort(lfave)
	if cres == True:
		lfave = lfave[::-1]
	for cont in range(len(lfave)):
		lfave[cont][0] = str(int(lfave[cont][0]) - 100000)
		for j in ids:
			ind = j.get("ID")
			if lfave[cont][1] == ind:
				ind_fave = j.find('favorites')
				atr_fave = str(int(ind_fave.attrib['favorites']))
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				stringao = stringao + " Favs: " + str(atr_fave) + " -> " + atr_post + "\n"
	return stringao

	#Gets the current Trending Topics for World/Brazil
def getTrends(brazil = True):
	if brazil != True:
		public_trends = api.trends_place(1)
	else:
		public_trends = api.trends_place(23424768)
	data = public_trends[0] 
	trends = data['trends']
	names = [trend['name'] for trend in trends]
	trendsName = '\n'.join(names)
	trendi = "trends"
	root = Element(str(trendi))
	for i in names:
		trend_word = Element('trendword', trend_word = i)
		root.append(trend_word)
		ElementTree(root).write('trends.xhtml')
	return trendsName

	#Lists the search query posts by Author name
def ordena(cres = True):
	root = ET.parse("Keywords.xhtml")
	names = root.findall("id")
	lnames = []
	stringao = ""
	for name in names:
		ident = name.get("ID")
		tag = name.find('name')
		tag_atrib = tag.attrib['name']
		lnames.append([minusculas(tag_atrib), ident]) # faz lista com os nomes do usuários todos em case low	
	heapsort(lnames)
	if cres == True:
		lnames = lnames[::-1]
	for cont in range(len(lnames)):
		ids = root.findall("id")
		for j in ids:
			ind = j.get("ID")
			if lnames[cont][1] == ind:
				ind_date = j.find('date')
				atr_date = ind_date.attrib['date']
				ind_name = j.find('name')
				atr_name = ind_name.attrib['name']
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				stringao = stringao + atr_date + " Post: " + str(atr_name) + " -> " + atr_post + "\n"
	return stringao

	#Lists the search query posts by Retweets
def ordenaPopularidade(cres = True):
	root = ET.parse("Keywords.xhtml")
	ids = root.findall("id")
	lrt = []
	stringao = ""
	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('retweets')
		tag_atrib = tag.attrib['retweets']
		lrt.append([(str(int(tag_atrib) + 100000)), ident])
	heapsort(lrt)
	if cres == True:
		lrt = lrt[::-1]
	for cont in range(len(lrt)):
		lrt[cont][0] = str(int(lrt[cont][0]) - 100000)
		for j in ids:
			ind = j.get("ID")
			if lrt[cont][1] == ind:
				ind_rt = j.find('retweets')
				atr_rt = str(int(ind_rt.attrib['retweets']))
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				ind_name = j.find('name')
				atr_name = ind_name.attrib['name']
				stringao = stringao + "Rts: " + str(atr_rt) + " - Post: " + str(atr_name) + " -> " + atr_post + "\n"
	return stringao

	#Lists the search query posts by Favorites
def ordenaCarisma(cres = True):
	root = ET.parse("Keywords.xhtml")
	ids = root.findall("id")
	lfave = []
	stringao = ""

	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('favorites')
		tag_atrib = tag.attrib['favorites']
		lfave.append([tag_atrib, ident])
	heapsort(lfave)
	if cres == True:
		lfave = lfave[::-1]	
	for cont in range(len(lfave)):
		lfave[cont][0] = str(int(lfave[cont][0]) - 100000)
		for j in ids:
			ind = j.get("ID")
			if lfave[cont][1] == ind:
				ind_fave = j.find('favorites')
				atr_fave = str(int(ind_fave.attrib['favorites']))
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				ind_name = j.find('name')
				atr_name = ind_name.attrib['name']
				stringao = stringao + "Favs: " + str(atr_fave) + " - Post: " + str(atr_name) + " -> " + atr_post + "\n"
	return stringao

	#Lists the search query posts by Date
def ordenaData(cres = True):
	root = ET.parse("Keywords.xhtml")
	ids = root.findall("id") 
	ldate = []
	stringao = ""
	for actual in ids:
		ident = actual.get("ID")
		tag = actual.find('date')
		tag_atrib = tag.attrib['date']
		ldate.append([tag_atrib, ident])
	heapsort(ldate)
	if cres == True:
		ldate = ldate[::-1]	
	for cont in range(len(ldate)):
		for j in ids:
			ind = j.get("ID")
			if ldate[cont][1] == ind:
				ind_date = j.find('date')
				atr_date = ind_date.attrib['date']
				ind_post = j.find('post')
				atr_post = ind_post.attrib['text']
				ind_name = j.find('name')
				atr_name = ind_name.attrib['name']
				stringao = stringao + str(atr_date) + " Post: " + str(atr_name) + " -> " + atr_post + "\n"
	return stringao

	#Heapsort definition
def heapsort(lst):
	for start in range((len(lst)-2)/2, -1, -1):
		siftdown(lst, start, len(lst)-1)
 	for end in range(len(lst)-1, 0, -1):
		lst[end], lst[0] = lst[0], lst[end]
		siftdown(lst, 0, end - 1)
	return lst
 
	#Auxiliar function for heapsort
def siftdown(lst, start, end):
	root = start
	while True:
		child = root * 2 + 1
		if child > end: break
		if child + 1 <= end and lst[child] < lst[child + 1]:
			child += 1
		if lst[root] < lst[child]:
			lst[root], lst[child] = lst[child], lst[root]
			root = child
		else:
			break

	#Lowcase translation for other functions
def minusculas(string):
    txt=""
    for i in string:
        order=ord(i)
        if ( order >= 65 ) and ( order <= 90 ):
                txt+=chr(order+32)
                continue
        txt+=chr(order)
    return txt
	
if __name__ == "__main__": 
    main()
