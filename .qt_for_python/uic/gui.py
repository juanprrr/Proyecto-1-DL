# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1550, 839)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table1 = QTableWidget(self.centralwidget)
        if (self.table1.columnCount() < 11):
            self.table1.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.table1.rowCount() < 6):
            self.table1.setRowCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table1.setVerticalHeaderItem(5, __qtablewidgetitem16)
        self.table1.setObjectName(u"table1")
        self.table1.setEnabled(True)
        self.table1.setGeometry(QRect(20, 510, 571, 251))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table1.sizePolicy().hasHeightForWidth())
        self.table1.setSizePolicy(sizePolicy)
        self.table1.horizontalHeader().setMinimumSectionSize(8)
        self.table1.horizontalHeader().setDefaultSectionSize(30)
        self.table1.horizontalHeader().setHighlightSections(False)
        self.table1.verticalHeader().setMinimumSectionSize(20)
        self.table1.verticalHeader().setDefaultSectionSize(30)
        self.table2 = QTableWidget(self.centralwidget)
        if (self.table2.columnCount() < 13):
            self.table2.setColumnCount(13)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(9, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(10, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(11, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(12, __qtablewidgetitem29)
        if (self.table2.rowCount() < 5):
            self.table2.setRowCount(5)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table2.setVerticalHeaderItem(4, __qtablewidgetitem34)
        self.table2.setObjectName(u"table2")
        self.table2.setEnabled(True)
        self.table2.setGeometry(QRect(620, 530, 831, 231))
        sizePolicy.setHeightForWidth(self.table2.sizePolicy().hasHeightForWidth())
        self.table2.setSizePolicy(sizePolicy)
        self.table2.setMaximumSize(QSize(1000, 1000))
        self.table2.horizontalHeader().setMinimumSectionSize(8)
        self.table2.horizontalHeader().setDefaultSectionSize(30)
        self.table2.horizontalHeader().setHighlightSections(False)
        self.table2.verticalHeader().setMinimumSectionSize(20)
        self.table2.verticalHeader().setDefaultSectionSize(30)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 30, 1091, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(10, 66, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.octalInput = QLineEdit(self.horizontalLayoutWidget)
        self.octalInput.setObjectName(u"octalInput")

        self.horizontalLayout.addWidget(self.octalInput)

        self.conversionTable = QTableWidget(self.centralwidget)
        if (self.conversionTable.columnCount() < 3):
            self.conversionTable.setColumnCount(3)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.conversionTable.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.conversionTable.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.conversionTable.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        if (self.conversionTable.rowCount() < 1):
            self.conversionTable.setRowCount(1)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.conversionTable.setVerticalHeaderItem(0, __qtablewidgetitem38)
        self.conversionTable.setObjectName(u"conversionTable")
        self.conversionTable.setGeometry(QRect(250, 110, 841, 111))
        self.conversionTable.horizontalHeader().setMinimumSectionSize(75)
        self.conversionTable.horizontalHeader().setDefaultSectionSize(250)
        self.conversionTable.verticalHeader().setDefaultSectionSize(75)
        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setGeometry(QRect(1190, 50, 151, 31))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(430, 240, 501, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.parButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.parButton.setObjectName(u"parButton")

        self.verticalLayout.addWidget(self.parButton)

        self.imparButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.imparButton.setObjectName(u"imparButton")

        self.verticalLayout.addWidget(self.imparButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.hammingButton = QPushButton(self.horizontalLayoutWidget_2)
        self.hammingButton.setObjectName(u"hammingButton")

        self.horizontalLayout_2.addWidget(self.hammingButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"p1", None));
        ___qtablewidgetitem1 = self.table1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"p2", None));
        ___qtablewidgetitem2 = self.table1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"d1", None));
        ___qtablewidgetitem3 = self.table1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"p3", None));
        ___qtablewidgetitem4 = self.table1.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"d2", None));
        ___qtablewidgetitem5 = self.table1.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"d3", None));
        ___qtablewidgetitem6 = self.table1.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"d3", None));
        ___qtablewidgetitem7 = self.table1.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"d4", None));
        ___qtablewidgetitem8 = self.table1.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"p4", None));
        ___qtablewidgetitem9 = self.table1.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"d5", None));
        ___qtablewidgetitem10 = self.table1.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"d7", None));
        ___qtablewidgetitem11 = self.table1.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Palabra de datos (sin paridad)", None));
        ___qtablewidgetitem12 = self.table1.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"P1", None));
        ___qtablewidgetitem13 = self.table1.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.table1.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"P2", None));
        ___qtablewidgetitem15 = self.table1.verticalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"P4", None));
        ___qtablewidgetitem16 = self.table1.verticalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Palabra de datos (con paridad)", None));
        ___qtablewidgetitem17 = self.table2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"p1", None));
        ___qtablewidgetitem18 = self.table2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"p2", None));
        ___qtablewidgetitem19 = self.table2.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"d1", None));
        ___qtablewidgetitem20 = self.table2.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"p3", None));
        ___qtablewidgetitem21 = self.table2.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"d2", None));
        ___qtablewidgetitem22 = self.table2.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"d3", None));
        ___qtablewidgetitem23 = self.table2.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"d3", None));
        ___qtablewidgetitem24 = self.table2.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"d4", None));
        ___qtablewidgetitem25 = self.table2.horizontalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"p4", None));
        ___qtablewidgetitem26 = self.table2.horizontalHeaderItem(9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"d5", None));
        ___qtablewidgetitem27 = self.table2.horizontalHeaderItem(10)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"d7", None));
        ___qtablewidgetitem28 = self.table2.horizontalHeaderItem(11)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Prueba de paridad", None));
        ___qtablewidgetitem29 = self.table2.horizontalHeaderItem(12)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Bit de paridad", None));
        ___qtablewidgetitem30 = self.table2.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Palabra de datos recibada", None));
        ___qtablewidgetitem31 = self.table2.verticalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"P1", None));
        ___qtablewidgetitem32 = self.table2.verticalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"P2", None));
        ___qtablewidgetitem33 = self.table2.verticalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"P3", None));
        ___qtablewidgetitem34 = self.table2.verticalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"P4", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese n\u00famero octal:", None))
        ___qtablewidgetitem35 = self.conversionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Binario", None));
        ___qtablewidgetitem36 = self.conversionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Decimal", None));
        ___qtablewidgetitem37 = self.conversionTable.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None));
        ___qtablewidgetitem38 = self.conversionTable.verticalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Conversi\u00f3n", None));
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convertir", None))
        self.parButton.setText(QCoreApplication.translate("MainWindow", u"Paridad Par", None))
        self.imparButton.setText(QCoreApplication.translate("MainWindow", u"Paridad Impar", None))
        self.hammingButton.setText(QCoreApplication.translate("MainWindow", u"Hamming", None))
    # retranslateUi

