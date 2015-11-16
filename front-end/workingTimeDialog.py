from PyQt5.QtWidgets import QMainWindow
from ui_WorkingTime import Ui_WorkingTime
from PyQt5 import QtWidgets
import psycopg2

class WorkingTimeDialog(QMainWindow, Ui_WorkingTime):

    def __init__(self):
        super(WorkingTimeDialog, self).__init__()
        self.setupUi(self)
        self.conn = psycopg2.connect("dbname=wbudowane user=wbudowane password=alamakota")
        #cur = self.conn.cursor()
 #       cur.execute("INSERT INTO Employee(First_Name, Last_Name, Email, Password) "
  #                  "VALUES ('aa', 'bb', 'cc', 'dd');")
        #cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
 #                   "VALUES (3, TIMESTAMP '2011-05-16 15:36:38');")
 #       cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
 #                   "VALUES (1, TIMESTAMP '2011-05-16 15:39:38');")
#        cur.execute("INSERT INTO Passage(EmployeeEmployee_ID, timestamp) "
#                    "VALUES (2, TIMESTAMP '2011-05-16 15:37:38');")

        #self.conn.commit()
 #       cur = self.conn.cursor()
 #       cur.execute("SELECT * FROM Employee;")
 #       rows = cur.fetchall()
        self._buttonRefresh.clicked.connect(self.RefreshPresentTable)

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
        self._tablePresentEmployee.setColumnCount(3)
        present_employees[0]
        self._tablePresentEmployee.setRowCount(len(present_employees))
        i = int(0)
        for employee in present_employees:
            self._tablePresentEmployee.setItem(i, 0, QtWidgets.QTableWidgetItem(str(employee[0])))
            self._tablePresentEmployee.setItem(i, 1, QtWidgets.QTableWidgetItem(str(employee[1])))
            self._tablePresentEmployee.setItem(i, 2, QtWidgets.QTableWidgetItem(str(employee[2])))
            i += 1




