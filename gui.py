import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.table2.setColumnWidth(11,170)
        self.table2.setColumnWidth(12,170)
        self.show()
    


app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
app.exec_()
        

