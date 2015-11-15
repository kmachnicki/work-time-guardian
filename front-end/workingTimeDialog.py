from PyQt5.QtWidgets import QMainWindow
from ui_WorkingTime import Ui_WorkingTime
import psycopg2

class WorkingTimeDialog(QMainWindow, Ui_WorkingTime):
    def __init__(self):
        super(WorkingTimeDialog, self).__init__()
        self.setupUi(self)
        conn = psycopg2.connect("dbname=wbudowane user=wbudowane password=alamakota")
        cur = conn.cursor()
        cur.execute("INSERT INTO Employee(Employee_ID, First_Name, Last_Name, Email, Password) "
                    "VALUES (7, 'aa', 'bb', 'cc', 'dd');")
        cur.execute("SELECT * FROM Employee;")
        rows = cur.fetchall()
        print(rows)
