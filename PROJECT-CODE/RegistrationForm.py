from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QDesktopWidget, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore

class FormReg(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle("MAIG WAREHOUSE APPLICATION v1.0.1")
        self.setGeometry(300, 300, 500, 500)

        self.nip_label = QtWidgets.QLabel("NIP")
        self.nip_input = QtWidgets.QLineEdit()
        self.nip_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.nip_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.company_label = QtWidgets.QLabel("Nazwa Firmy")
        self.company_input = QtWidgets.QLineEdit()
        self.company_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.company_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.first_name_label = QtWidgets.QLabel("Imię")
        self.first_name_input = QtWidgets.QLineEdit()
        self.first_name_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.first_name_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.last_name_label = QtWidgets.QLabel("Nazwisko")
        self.last_name_input = QtWidgets.QLineEdit()
        self.last_name_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.last_name_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.phone_label = QtWidgets.QLabel("Telefon")
        self.phone_input = QtWidgets.QLineEdit()
        self.phone_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.phone_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.email_label = QtWidgets.QLabel("Email")
        self.email_input = QtWidgets.QLineEdit()
        self.email_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.email_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")
        
        self.password_label = QtWidgets.QLabel("Hasło")
        self.password_input = QtWidgets.QLineEdit()
        self.password_label.setStyleSheet("color: red; font-weight: bold; font-size: 18px; padding: 6px;")
        self.password_input.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: lightyellow; border: 2px solid green; border-radius: 3px; font-family: Arial; margin:10px; padding: 6px;")

        self.register_button = QtWidgets.QPushButton("Zarejestruj")
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.login_button = QtWidgets.QPushButton("Powrót do logowania")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("color: white; font-weight: bold; font-size: 20px; background-color: red; border-radius: 3px; font-family: Arial; margin: 5px; padding: 5px;")
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.nip_label, self.nip_input)
        form_layout.addRow(self.company_label, self.company_input)
        form_layout.addRow(self.first_name_label, self.first_name_input)
        form_layout.addRow(self.last_name_label, self.last_name_input)
        form_layout.addRow(self.phone_label, self.phone_input)
        form_layout.addRow(self.email_label, self.email_input)
        form_layout.addRow(self.password_label, self.password_input)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.register_button)
        buttons_layout.addWidget(self.login_button)

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
    
        try:
           if self.nip_input.text() == "" or self.company_input.text() == "" or self.first_name_input.text() == "" or self.last_name_input.text() == "" or self.phone_input.text() == "" or self.email_input.text() == "" or self.password_input.text() == "":
             QMessageBox.warning(self, "Uwaga", "Uzupełnij wszystkie pola!")
           else:
             QMessageBox.information(self, "Sukces", "Formularz został pomyślnie zapisany!")
             self.close()
        except Exception as e:
           QMessageBox.warning(self, "Błąd", str(e))
        
    def login(self):
        self.close()