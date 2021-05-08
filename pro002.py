from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("fuck you bitch")
        self.initUI()
    def initUI(self):
        self.label= QtWidgets.QLabel(self)
        self.label.setText("How you doing")
        self.label.move(50,50)
        self.b= QtWidgets.QPushButton(self)
        self.b.setText("fuck")
        self.b.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("Your mom Sucks cock in hell")
        self.update()
    def update (self):
        self.label.adjustSize()
def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())
window()