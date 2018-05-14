import sys,os 
from time import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
def show_name(name): 
    name = nameLine.text() 
    if name == "": 
        QMessageBox.information(nameLine,"输入为空","请输入姓名") 
        return 
    else: 
        QMessageBox.information(nameLine,"Well Done!","Hello {}!".format(name)) 
		
app = QApplication(sys.argv) 
Enter = QWidget() 
nameLabel = QLabel("姓名:") 
nameLine = QLineEdit(Enter) 
EnterButton = QPushButton("Enter", Enter) 
subLayout = QHBoxLayout() 
subLayout.addStretch(1) 
subLayout.addWidget(EnterButton) 
bodyLayout = QVBoxLayout() 
bodyLayout.addWidget(nameLabel) 
bodyLayout.addWidget(nameLine) 
bodyLayout.addLayout(subLayout) 
EnterButton.clicked.connect(show_name) 
Enter.setLayout(bodyLayout) 
Enter.setWindowTitle("Hello Qt") 
Enter.show() 
sys.exit(app.exec_()) 