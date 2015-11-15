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
        WorkingTime.resize(745, 600)
        self.centralwidget = QtWidgets.QWidget(WorkingTime)
        self.centralwidget.setObjectName("centralwidget")
        self._buttonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self._buttonRefresh.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self._buttonRefresh.setObjectName("_buttonRefresh")
        self._tablePresentEmployee = QtWidgets.QTableWidget(self.centralwidget)
        self._tablePresentEmployee.setGeometry(QtCore.QRect(90, 20, 631, 521))
        self._tablePresentEmployee.setObjectName("_tablePresentEmployee")
        self._tablePresentEmployee.setColumnCount(0)
        self._tablePresentEmployee.setRowCount(0)
        WorkingTime.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkingTime)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
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

