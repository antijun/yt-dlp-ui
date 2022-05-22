import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.clickme)

    def clickme(self):
        print("pressed")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
