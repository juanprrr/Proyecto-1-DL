import sys
import OctalConverter
import hamming
import testmatplot
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.hammingCurrent = None
        self.table2.setColumnWidth(17,170)
        self.table2.setColumnWidth(18,170)
        self.convertButton.clicked.connect(self.convert)
        self.hammingButton.clicked.connect(self.hamBut)
        self.compararButton.clicked.connect(self.comparar)
        self.hammingButton.setEnabled(False)
        self.compararButton.setEnabled(False)
        self.show()

    def comparar(self):
        conthr = 0
        for j in str(self.compararInput.text()):
            self.table2.setItem(0, conthr, QtWidgets.QTableWidgetItem(j))
            conthr += 1
        
        if self.parButton.isChecked():
            self.hammingCurrent.comprobar(str(self.compararInput.text()),"par")
            n = 0
            while n < len(self.hammingCurrent.tabla_hamming):
                m = (2**n)-1
                cont = 0
                for i in range(len(self.hammingCurrent.tabla_hamming[n])):
                  self.table2.setItem(n+1, m, QtWidgets.QTableWidgetItem(self.hammingCurrent.tabla_hamming[n][cont]))
                  cont += 1
                  m += 1
                n+=1

        else:
            self.hammingCurrent.comprobar(str(self.compararInput.text()),"impar")
            n = 0
            while n < len(self.hammingCurrent.tabla_hamming):
                m = (2**n)-1
                cont = 0
                for i in range(len(self.hammingCurrent.tabla_hamming[n])):
                  self.table2.setItem(n+1, m, QtWidgets.QTableWidgetItem(self.hammingCurrent.tabla_hamming[n][cont]))
                  cont += 1
                  m += 1
                n+=1
                
        contPar = 1
        for j in self.hammingCurrent.paridades:        
            self.table2.setItem(contPar, 18, QtWidgets.QTableWidgetItem(j))
            if j == "1":
                self.table2.setItem(contPar, 17, QtWidgets.QTableWidgetItem("Error"))
            else:
                self.table2.setItem(contPar, 17, QtWidgets.QTableWidgetItem("Correcto"))
            contPar+=1
        
        if "1" in self.hammingCurrent.paridades:
            QMessageBox.about(self, "Warning", "Error en bit: " + self.hammingCurrent.toDec())
        

                


    def convert(self):
        conv = OctalConverter.OctalConverter(int(self.octalInput.text()))
        if conv.isValid(conv.data) == False:
            QMessageBox.about(self, "Warning", "Ingrese un valor de base octal válido")
            
        else:
            self.conversionTable.setItem(0,0,QtWidgets.QTableWidgetItem(conv.toBinary()))
            self.conversionTable.setItem(0,1,QtWidgets.QTableWidgetItem(conv.toDec()))
            self.conversionTable.setItem(0,2,QtWidgets.QTableWidgetItem(conv.toHex()))
            nzri = testmatplot.NZRI([int(i) for i in conv.toBinary()])
            self.hammingButton.setEnabled(True)
    
    def hamBut(self):
        a = hamming.Hamming()
        
        if self.parButton.isChecked():
            
            a.calcParidad(a.hileraHamming(self.conversionTable.item(0,0).text()), "par")
            a.comprobar(a.hileraParidad,"par")
            n = 0
            while n < len(a.tabla_hamming):
                m = (2**n)-1
                cont = 0
                for i in range(len(a.tabla_hamming[n])):
                  self.table1.setItem(n+1, m, QtWidgets.QTableWidgetItem(a.tabla_hamming[n][cont]))
                  cont += 1
                  m += 1
                n+=1
            
            conthm = 0
            for j in a.hilerahamming:
                self.table1.setItem(0, conthm, QtWidgets.QTableWidgetItem(j))
                conthm += 1
            
            conthp = 0
            for k in a.hileraParidad:
                self.table1.setItem(6, conthp, QtWidgets.QTableWidgetItem(k))
                conthp += 1

        else:
            a.calcParidad(a.hileraHamming(self.conversionTable.item(0,0).text()), "impar")
            a.comprobar(a.hileraParidad,"impar")
            n = 0
            while n < len(a.tabla_hamming):
                m = (2**n)-1
                cont = 0
                for i in range(len(a.tabla_hamming[n])):
                  self.table1.setItem(n+1, m, QtWidgets.QTableWidgetItem(a.tabla_hamming[n][cont]))
                  cont += 1
                  m += 1
                n+=1

            conthm = 0
            for j in a.hilerahamming:
                self.table1.setItem(0, conthm, QtWidgets.QTableWidgetItem(j))
                conthm += 1

            conthp = 0
            for k in a.hileraParidad:
                self.table1.setItem(6, conthp, QtWidgets.QTableWidgetItem(k))
                conthp += 1

        self.hammingCurrent = a
        self.compararButton.setEnabled(True)

            

            
            


    


app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
app.exec_()
        

