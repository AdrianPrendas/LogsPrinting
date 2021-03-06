# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patterns.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os, sys
import connection as window_conect
import analisis as analisis

class Ui_MainWindow(object):
    
    def loadTable(self):
        self.tableWidget.setRowCount(0)
        for a in analisis.loadTable().head():
            for row_number, row_data in enumerate (a):
                self.tableWidget.insertRow(row_number)
                for col_number, data in enumerate (row_data):     
                    self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(a)) )
    def about(self):            
         msg = QMessageBox(self.centralwidget)
         msg.setText("Welcome to DB_Patterns")
         msg.setInformativeText("This is a educational project created by Roger Amador and Adrian Prendas")
         msg.setWindowTitle("DB_Patterns")
         msg.exec_() 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.filter = QtWidgets.QLineEdit(self.groupBox)
        self.filter.setObjectName("filter")
        self.gridLayout_2.addWidget(self.filter, 0, 0, 1, 1)
        self.search = QtWidgets.QPushButton(self.groupBox)
        self.search.setObjectName("search")
        self.gridLayout_2.addWidget(self.search, 0, 2, 1, 1)
        self.chooser = QtWidgets.QComboBox(self.groupBox)
        self.chooser.setObjectName("chooser")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.gridLayout_2.addWidget(self.chooser, 0, 1, 1, 1)
        self.graphics = QtWidgets.QTabWidget(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.graphics.setFont(font)
        self.graphics.setObjectName("graphics")
        self.tab_user = QtWidgets.QWidget()
        self.tab_user.setObjectName("tab_user")
        self.graphics.addTab(self.tab_user, "")
        self.tab_tbs_name = QtWidgets.QWidget()
        self.tab_tbs_name.setObjectName("tab_tbs_name")
        self.graphics.addTab(self.tab_tbs_name, "")
        self.tab_tb_name = QtWidgets.QWidget()
        self.tab_tb_name.setObjectName("tab_tb_name")
        self.graphics.addTab(self.tab_tb_name, "")
        self.tab_owner = QtWidgets.QWidget()
        self.tab_owner.setObjectName("tab_owner")
        self.graphics.addTab(self.tab_owner, "")
        self.tab_operation = QtWidgets.QWidget()
        self.tab_operation.setObjectName("tab_operation")
        self.graphics.addTab(self.tab_operation, "")
        self.tab_date = QtWidgets.QWidget()
        self.tab_date.setObjectName("tab_date")
        self.graphics.addTab(self.tab_date, "")
        self.tab_time = QtWidgets.QWidget()
        self.tab_time.setObjectName("tab_time")
        self.graphics.addTab(self.tab_time, "")
        self.gridLayout_2.addWidget(self.graphics, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 2, 3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1023, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew_tab = QtWidgets.QAction(MainWindow)
        self.actionNew_tab.setObjectName("actionNew_tab")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionSelect_all = QtWidgets.QAction(MainWindow)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.actionToolbar = QtWidgets.QAction(MainWindow)
        self.actionToolbar.setObjectName("actionToolbar")
        self.actionSteps = QtWidgets.QAction(MainWindow)
        self.actionSteps.setObjectName("actionSteps")
        self.menuFile.addAction(self.actionNew_tab)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.graphics.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB_Patterns"))
        self.groupBox.setTitle(_translate("MainWindow", "DBPatterns"))
        self.search.setText(_translate("MainWindow", "SEARCH"))
        self.chooser.setItemText(0, _translate("MainWindow", "GENERAL"))
        self.chooser.setItemText(1, _translate("MainWindow", "USER_NAME"))
        self.chooser.setItemText(2, _translate("MainWindow", "TABLESPACE_NAME"))
        self.chooser.setItemText(3, _translate("MainWindow", "TABLE_NAME"))
        self.chooser.setItemText(4, _translate("MainWindow", "SEG_OWNER"))
        self.chooser.setItemText(5, _translate("MainWindow", "OPERATION"))
        self.chooser.setItemText(6, _translate("MainWindow", "DATE"))
        self.chooser.setItemText(7, _translate("MainWindow", "TIME"))
        self.chooser.setItemText(8, _translate("MainWindow", "COMMIT"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_user), _translate("MainWindow", "USER"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_tbs_name), _translate("MainWindow", "TABLESPACE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_tb_name), _translate("MainWindow", "TABLE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_owner), _translate("MainWindow", "SEG_OWNER"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_operation), _translate("MainWindow", "OPERATION"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_date), _translate("MainWindow", "DATE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_time), _translate("MainWindow", "TIME"))
        self.label.setText(_translate("MainWindow", "    Graphics"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "USER_NAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TABLESPACE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TABLE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SEG_OWNER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OPERATION"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SQL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SQL_-1"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "TIME"))
       
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionRecent.setText(_translate("MainWindow", "Open Recent"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionNew_tab.setText(_translate("MainWindow", "New tab"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionSelect_all.setText(_translate("MainWindow", "Select all"))
        self.actionToolbar.setText(_translate("MainWindow", "Toolbar"))
        self.actionSteps.setText(_translate("MainWindow", "StepByStep"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.loadTable()
    sys.exit(app.exec_())

