from LogRegUser import MainWindow 
from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    program = QApplication([])
    window = MainWindow()
    
    #window.resize(500,400)
    window.setWindowTitle("MAIG WAREHOUSE v1.0.1")
    window.setStyleSheet("background-color: lightgray;")
    
    window.show()
    program.exec()