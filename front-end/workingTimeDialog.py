from PyQt5.QtWidgets import QMainWindow
from ui_WorkingTime import Ui_WorkingTime
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
import psycopg2

class WorkingTimeDialog(QMainWindow, Ui_WorkingTime):

    def __init__(self):
        super(WorkingTimeDialog, self).__init__()
        self.setupUi(self)
        self.conn = psycopg2.connect("dbname=wbudowane user=wbudowane password=alamakota")
        self._refreshTimer = QtCore.QTimer(self)
        self._refreshTimer.start(500)
        self._refreshTimer.timeout.connect(self.RefreshPresentTable)
        self._refreshTimer.timeout.connect(self.RefreshWorkedTimeTable)
        self._fromTimeEdit.setDateTime(datetime.now())
        self._toTimeEdit.setDateTime(datetime.now())
        self._toTimeEdit.dateTimeChanged.connect(self.RefreshWorkedTimeTable)
        self._fromTimeEdit.dateTimeChanged.connect(self.RefreshWorkedTimeTable)
        self._addUserButton.clicked.connect(self.AddUser)
        self._tableTimeWorked.setColumnCount(3)
        self._tableTimeWorked.setColumnWidth(2, 166)
        self._tableTimeWorked.setHorizontalHeaderLabels(["First Name", "Last Name", "Worked Time"])
        self._tablePresentEmployee.setColumnCount(3)
        self._tablePresentEmployee.setColumnWidth(2, 154)
        self._tablePresentEmployee.setHorizontalHeaderLabels(["First Name", "Last Name", "Arrival Time"])

#        cur = self.conn.cursor()
#        cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
#                    "VALUES (5, TIMESTAMP '2013-06-01 08:00:00');")
#        self.conn.commit()

    def GetPresentEmployees(self):
        cur = self.conn.cursor()
        cur.execute("SELECT Employee_ID, First_Name, Last_Name FROM Employee;")
        rows = cur.fetchall()
        result = []
        for row in rows:
            id = row[0]
            cur.execute("SELECT * FROM Passage WHERE EmployeeEmployee_ID = %s ;", [id] )
            passages = cur.fetchall()
            count = len(passages)
            if count > 0 and count % 2 == 1:
                result.append([row[1], row[2], passages[count - 1][2]])
        return result

    def RefreshPresentTable(self):
        present_employees = self.GetPresentEmployees()

        self._tablePresentEmployee.setRowCount(len(present_employees))
        i = int(0)
        for employee in present_employees:
            self._tablePresentEmployee.setItem(i, 0, QtWidgets.QTableWidgetItem(str(employee[0])))
            self._tablePresentEmployee.setItem(i, 1, QtWidgets.QTableWidgetItem(str(employee[1])))
            self._tablePresentEmployee.setItem(i, 2, QtWidgets.QTableWidgetItem(str(employee[2])))
            i += 1

    def GetWorkedTime(self):
        from_time = self._fromTimeEdit.dateTime().toPyDateTime()
        to_time = self._toTimeEdit.dateTime().toPyDateTime()
        cur = self.conn.cursor()
        cur.execute("SELECT Employee_ID, First_Name, Last_Name FROM Employee;")
        rows = cur.fetchall()
        result = []
        for row in rows:
            id = row[0]
            cur.execute("SELECT timestamp FROM Passage WHERE EmployeeEmployee_ID = %s AND timestamp > %s AND timestamp < %s;", [id, from_time, to_time])
            passages = cur.fetchall()
            count = len(passages)
            i = int(0)
            time_elapsed = 0
            while i < count - 1:
                a = passages[i][0]
                b = passages[i + 1][0]
                if i == 0:
                    time_elapsed = b - a
                else:
                    time_elapsed = time_elapsed + b - a
                i += 2
            if count > 0:
                result.append([row[1], row[2], time_elapsed])
        return result

    def RefreshWorkedTimeTable(self):
        worked_time = self.GetWorkedTime()

        self._tableTimeWorked.setRowCount(len(worked_time))
        i = int(0)
        for employee in worked_time:
            self._tableTimeWorked.setItem(i, 0, QtWidgets.QTableWidgetItem(str(employee[0])))
            self._tableTimeWorked.setItem(i, 1, QtWidgets.QTableWidgetItem(str(employee[1])))
            self._tableTimeWorked.setItem(i, 2, QtWidgets.QTableWidgetItem(str(employee[2])))
            i += 1

    def AddUser(self):
        cur = self.conn.cursor()
        name = self._firstNameEdit.text()
        cur.execute("INSERT INTO Employee(First_Name, Last_Name, Email, Password, Tag_ID) "
                    "VALUES (%s,%s,%s,%s,%s);", [self._firstNameEdit.text(), self._lastNameEdit.text(),
                                              self._emailEdit.text(), self._passwordEdit.text(), self._tagIdEdit.text()])
        self.conn.commit()

        #cur = self.conn.cursor()
 #       cur.execute("INSERT INTO Employee(First_Name, Last_Name, Email, Password) "
  #                  "VALUES ('aa', 'bb', 'cc', 'dd');")
        #cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
        #            "VALUES (3, TIMESTAMP '2011-05-16 15:36:38');")
 #       cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
 #                   "VALUES (1, TIMESTAMP '2011-05-16 15:39:38');")
#        cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
#                    "VALUES (2, TIMESTAMP '2011-05-16 15:37:38');")

        #self.conn.commit()
 #       cur = self.conn.cursor()
 #       cur.execute("SELECT * FROM Employee;")
 #       rows = cur.fetchall()
