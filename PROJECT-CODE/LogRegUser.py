from PyQt5.QtWidgets import * 
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        form = QFormLayout()
        self.name_edit = QLineEdit()
        form.addRow("Nazwa użytkownika:", self.name_edit)
        
        self.password_edit = QLineEdit()
        form.addRow("Hasło:", self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.nip_form = QLineEdit()
        form.addRow("NIP:", self.nip_form)

        self.log_button = QPushButton("Zaloguj się")
        self.reg_button = QPushButton("Zarejestruj się")
        
        self.name_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px;")
        self.password_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px;")
        self.nip_form.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px;")
        self.log_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px;")
        self.reg_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px;")
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.log_button)
        layout.addWidget(self.reg_button)
        self.setLayout(layout)
        