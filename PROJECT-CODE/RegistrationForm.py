from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QDesktopWidget
from PyQt5 import QtGui, QtWidgets, QtCore

class FormReg(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle("MAIG WAREHOUSE APPLICATION v1.0.1")
        self.setGeometry(300, 300, 500, 500)

        nip_label = QtWidgets.QLabel("NIP")
        nip_input = QtWidgets.QLineEdit()
        nip_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        nip_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        company_label = QtWidgets.QLabel("Nazwa Firmy")
        company_input = QtWidgets.QLineEdit()
        company_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        company_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        first_name_label = QtWidgets.QLabel("Imię")
        first_name_input = QtWidgets.QLineEdit()
        first_name_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        first_name_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        last_name_label = QtWidgets.QLabel("Nazwisko")
        last_name_input = QtWidgets.QLineEdit()
        last_name_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        last_name_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        phone_label = QtWidgets.QLabel("Telefon")
        phone_input = QtWidgets.QLineEdit()
        phone_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        phone_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        email_label = QtWidgets.QLabel("Email")
        email_input = QtWidgets.QLineEdit()
        email_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        email_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        password_label = QtWidgets.QLabel("Hasło")
        password_input = QtWidgets.QLineEdit()
        password_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        password_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")

        register_button = QtWidgets.QPushButton("Zarejestruj")
        register_button.clicked.connect(self.register)
        register_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")
        register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        login_button = QtWidgets.QPushButton("Powrót do logowania")
        login_button.clicked.connect(self.login)
        login_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")
        login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(nip_label, nip_input)
        form_layout.addRow(company_label, company_input)
        form_layout.addRow(first_name_label, first_name_input)
        form_layout.addRow(last_name_label, last_name_input)
        form_layout.addRow(phone_label, phone_input)
        form_layout.addRow(email_label, email_input)
        form_layout.addRow(password_label, password_input)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(register_button)
        buttons_layout.addWidget(login_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        
        pixmap = QtGui.QPixmap(r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\alsn20210928150320120vwuc.jpg")
        pixmap = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(palette)

        self.setLayout(main_layout)
        self.center()
        
    def center(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def register(self):
        pass
        
    def login(self):
        self.close()