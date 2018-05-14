import sys,os 
from time import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
def showDialog(): 
    label = "<span style=' color:#8FBC8F;'>Me ：{} </span>".format(strftime("%Y-%m-%d %H:%M:%S", localtime())) 
    message =  chatText.toPlainText() 
    outputarea.append(label) 
    outputarea.append(' '+message) 
    chatText.clear() 
    chatText.setFocus() 
    saveMsg(message) 
def cancelMsg(): 
    chatText.clear() 
def saveMsg(txt): 
    file = open('save.txt', 'a') 
    file.write(txt + '\n') 
    file.close() 
def saveMsg(txt): 
    file = open('save.txt', 'a') 
    file.write(txt + '\n') 
    file.close() 
def getMsg(): 
    if os.path.exists('save.txt'): 
        message = '\nGet The Message:' 
        outputarea.append(message) 
        file = open('save.txt', 'r') 
        txt = file.read() + '\n' 
        outputarea.append(txt) 
        file.close() 
    else: 
        outputarea.append('No Record\n') 
chatapp = QApplication(sys.argv) 
chatwidget = QWidget() 
chatText = QTextEdit(chatwidget) 
chatText.setMaximumSize(QSize(600,100)) 
outputarea = QTextEdit(chatwidget) 
outputarea.setReadOnly(True) 
outputarea.setFont(QFont('SimSun', 12)) 
outputarea.setMaximumSize(QSize(600, 200)) 
btnSend = QPushButton('发送', chatwidget) 
btnCancel = QPushButton('取消', chatwidget) 
btnHistory = QPushButton('历史记录', chatwidget) 
btnSend.clicked.connect(showDialog) 
btnCancel.clicked.connect(cancelMsg) 
btnHistory.clicked.connect(getMsg) 
hbox = QHBoxLayout() 
hbox.addWidget(btnSend) 
hbox.addWidget(btnCancel) 
hbox.addStretch(1) 
hbox.addWidget(btnHistory) 
vbox = QVBoxLayout() 
vbox.addWidget(outputarea) 
vbox.addWidget(chatText) 
vbox.addLayout(hbox) 
chatwidget.setLayout(vbox) 
chatwidget.setGeometry(0, 0, 600, 400) 
chatwidget.setWindowTitle('与 hanwei 对话中') 
screen = QDesktopWidget().screenGeometry() 
size = chatwidget.geometry() 
chatwidget.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2) 
chatwidget.show() 
sys.exit(chatapp.exec_()) 