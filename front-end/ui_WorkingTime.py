# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkingTime.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WorkingTime(object):
    def setupUi(self, WorkingTime):
        WorkingTime.setObjectName("WorkingTime")
        WorkingTime.resize(836, 759)
        self.centralwidget = QtWidgets.QWidget(WorkingTime)
        self.centralwidget.setObjectName("centralwidget")
        self._buttonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self._buttonRefresh.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self._buttonRefresh.setObjectName("_buttonRefresh")
        self._tablePresentEmployee = QtWidgets.QTableWidget(self.centralwidget)
        self._tablePresentEmployee.setGeometry(QtCore.QRect(20, 60, 371, 521))
        self._tablePresentEmployee.setObjectName("_tablePresentEmployee")
        self._tablePresentEmployee.setColumnCount(0)
        self._tablePresentEmployee.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self._tableTimeWorked = QtWidgets.QTableWidget(self.centralwidget)
        self._tableTimeWorked.setGeometry(QtCore.QRect(410, 90, 401, 491))
        self._tableTimeWorked.setObjectName("_tableTimeWorked")
        self._tableTimeWorked.setColumnCount(0)
        self._tableTimeWorked.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self._fromTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self._fromTimeEdit.setGeometry(QtCore.QRect(460, 50, 131, 22))
        self._fromTimeEdit.setObjectName("_fromTimeEdit")
        self._toTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self._toTimeEdit.setGeometry(QtCore.QRect(650, 50, 131, 22))
        self._toTimeEdit.setObjectName("_toTimeEdit")
        WorkingTime.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkingTime)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        WorkingTime.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkingTime)
        self.statusbar.setObjectName("statusbar")
        WorkingTime.setStatusBar(self.statusbar)

        self.retranslateUi(WorkingTime)
        QtCore.QMetaObject.connectSlotsByName(WorkingTime)

    def retranslateUi(self, WorkingTime):
        _translate = QtCore.QCoreApplication.translate
        WorkingTime.setWindowTitle(_translate("WorkingTime", "WorkingTime"))
        self._buttonRefresh.setText(_translate("WorkingTime", "Refresh"))
        self.label.setText(_translate("WorkingTime", "Present Employees"))
        self.label_2.setText(_translate("WorkingTime", "Time Worked"))

