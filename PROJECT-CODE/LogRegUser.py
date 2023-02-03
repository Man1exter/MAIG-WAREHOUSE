from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton 
from PyQt5 import QtGui, QtWidgets, QtCore
class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        layout = QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        form = QFormLayout()
        self.name_edit = QLineEdit()
        form_label = QtWidgets.QLabel("Nazwa użytkownika:")
        form_label.setStyleSheet("color: green; font-weight: bold; font-size: 18px;")

        form.addRow(form_label, self.name_edit)
        
        self.password_edit = QLineEdit()
        password_label = QtWidgets.QLabel("Hasło:")
        password_label.setStyleSheet("color: green; font-weight: bold; font-size: 18px;")
        form.addRow(password_label, self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.nip_form = QLineEdit()
        nip_label = QtWidgets.QLabel("NIP:")
        nip_label.setStyleSheet("color: green; font-weight: bold; font-size: 18px;")
        form.addRow(nip_label, self.nip_form)
        layout.addLayout(form)
        
        self.log_button = QPushButton("Zaloguj się")
        self.reg_button = QPushButton("Zarejestruj się")
        layout.addWidget(self.log_button)
        layout.addWidget(self.reg_button)
        
        self.name_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial;")
        self.password_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial;")
        self.nip_form.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial;")
        self.log_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial;")
        self.reg_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial;")
        
        palette = self.palette()
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.Window, QtGui.QBrush(QtGui.QPixmap(r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\alsn20210928150320120vwuc.jpg")))
        self.setPalette(palette)
        
        self.setLayout(layout)

        