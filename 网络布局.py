from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWidgets import QPushButton, QGridLayout 
import sys 
app = QApplication(sys.argv) 
screen = QWidget() 
bodyLayout = QGridLayout() 
for i in range(1,10): 
    button = QPushButton(str(i)) 
    bodyLayout.addWidget(button,(i-1)//3,(i-1)%3) 
screen.setLayout(bodyLayout) 
screen.setWindowTitle("网格布局") 
screen.show() 
sys.exit(app.exec_()) 