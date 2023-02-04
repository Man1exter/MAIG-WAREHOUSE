from LogRegUser import MainWindow 
from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(580,480)
    main_window.setWindowTitle("MAIG WAREHOUSE APPLICATION v1.0.1")
    main_window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec())