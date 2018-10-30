# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gridLayout_1(object):
    def setupUi(self, gridLayout_1):
        gridLayout_1.setObjectName("gridLayout_1")
        gridLayout_1.resize(333, 373)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gridLayout_1.setWindowIcon(icon)
        self.grid = QtWidgets.QGridLayout(gridLayout_1)
        self.grid.setObjectName("0")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.message = QtWidgets.QLabel(gridLayout_1)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 7, 1, 1, 1)
        self.hostLine = QtWidgets.QLineEdit(gridLayout_1)
        self.hostLine.setObjectName("hostLine")
        self.gridLayout.addWidget(self.hostLine, 1, 1, 1, 2)
        self.portLine = QtWidgets.QLineEdit(gridLayout_1)
        self.portLine.setObjectName("portLine")
        self.gridLayout.addWidget(self.portLine, 2, 1, 1, 2)
        self.connectButton = QtWidgets.QPushButton(gridLayout_1)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.testButton = QtWidgets.QPushButton(gridLayout_1)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 7, 2, 1, 1)
        self.userLine = QtWidgets.QLineEdit(gridLayout_1)
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 3, 1, 1, 2)
        self.passwordLine = QtWidgets.QLineEdit(gridLayout_1)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 4, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(gridLayout_1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(gridLayout_1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.serviceLine = QtWidgets.QLineEdit(gridLayout_1)
        self.serviceLine.setObjectName("serviceLine")
        self.gridLayout.addWidget(self.serviceLine, 5, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(gridLayout_1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(gridLayout_1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(gridLayout_1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.grid.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(gridLayout_1)
        QtCore.QMetaObject.connectSlotsByName(gridLayout_1)

    def retranslateUi(self, gridLayout_1):
        _translate = QtCore.QCoreApplication.translate
        gridLayout_1.setWindowTitle(_translate("gridLayout_1", "Connect Settings"))
        self.message.setText(_translate("gridLayout_1", "message"))
        self.connectButton.setText(_translate("gridLayout_1", "Connect"))
        self.testButton.setText(_translate("gridLayout_1", "Test connection"))
        self.label_2.setText(_translate("gridLayout_1", "Port"))
        self.label.setText(_translate("gridLayout_1", "Host IP"))
        self.label_3.setText(_translate("gridLayout_1", "User"))
        self.label_4.setText(_translate("gridLayout_1", "Password"))
        self.label_5.setText(_translate("gridLayout_1", "Service"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gridLayout_1 = QtWidgets.QDialog()
    ui = Ui_gridLayout_1()
    ui.setupUi(gridLayout_1)
    gridLayout_1.show()
    sys.exit(app.exec_())

