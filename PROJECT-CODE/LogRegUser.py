from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton 
from PyQt5 import QtGui, QtWidgets, QtCore
from CentralWindow import CentralWindowMain
from RegistrationForm import FormReg

class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle("MAIG WAREHOUSE APPLICATION v1.0.1")
        
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        layout = QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        form = QFormLayout()
        self.name_edit = QLineEdit()
        form_label = QtWidgets.QLabel("Nazwa użytkownika:")
        form_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")

        form.addRow(form_label, self.name_edit)
        
        self.password_edit = QLineEdit()
        password_label = QtWidgets.QLabel("Hasło:")
        password_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        form.addRow(password_label, self.password_edit)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.nip_form = QLineEdit()
        nip_label = QtWidgets.QLabel("NIP:")
        nip_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        form.addRow(nip_label, self.nip_form)
        layout.addLayout(form)
        
        self.log_button = QPushButton("Zaloguj się")
        self.log_button.clicked.connect(self.login_accept)
        self.reg_button = QPushButton("Zarejestruj się")
        self.reg_button.clicked.connect(self.registration_accept)
        
        layout.addWidget(self.log_button)
        layout.addWidget(self.reg_button)
        
        self.name_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        self.password_edit.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin: 10px; padding: 6px;")

        self.nip_form.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin: 10px; padding: 6px;")
        
        self.log_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")

        self.reg_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")
             
        pixmap = QtGui.QPixmap(r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\alsn20210928150320120vwuc.jpg")
        pixmap = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(palette)
        
        self.setLayout(layout)
        
    def login_accept(self):
        self.central_window = CentralWindowMain()
        self.central_window.show()
        self.close()

    def registration_accept(self):
        self.central_window_reg = FormReg()
        self.central_window_reg.show()

        


        