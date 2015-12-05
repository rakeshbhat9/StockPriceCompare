# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScripCompare.ui'
#
# Created: Mon Nov 23 09:34:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(266, 268)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../home/rakeshbhat9/Downloads/rb1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(10.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setDate(QtCore.QDate(2015, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setDate(QtCore.QDate(2015, 1, 1))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.verticalLayout.addWidget(self.dateEdit_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "StockCompare", None))
        self.label.setText(_translate("MainWindow", "First Symbol:", None))
        self.lineEdit.setText(_translate("MainWindow", "Enter symbol", None))
        self.label_2.setText(_translate("MainWindow", "Second Symbol:", None))
        self.lineEdit_2.setText(_translate("MainWindow", "Enter symbol", None))
        self.label_3.setText(_translate("MainWindow", "Select Start & End Date:", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))

