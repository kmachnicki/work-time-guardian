import sys
from workingTimeDialog import WorkingTimeDialog


from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
myWindow = WorkingTimeDialog()
myWindow.show()
app.exec_()