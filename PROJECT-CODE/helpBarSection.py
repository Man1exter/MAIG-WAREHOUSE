from PyQt5 import QtWidgets, QtGui, QtCore

class HelpWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setWindowTitle("Pomoc")
        self.setGeometry(100, 100, 800, 600)

        self.center_on_screen()

        self.init_ui()

    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        self.background_label = QtWidgets.QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setScaledContents(True)  
        self.update_background()  

        
        label = QtWidgets.QLabel("Kontakt:")
        label.setStyleSheet("font-size: 29px; font-weight: bold; color: green; margin-top: 20px;")  # Pogrubienie, rozmiar i czerwony kolor tekstu
        label.setAlignment(QtCore.Qt.AlignCenter)  # Wyśrodkowanie etykiety
        main_layout.addWidget(label)

       
        contact_info_layout = QtWidgets.QVBoxLayout()

        email_label = QtWidgets.QLabel("E-mail:      maigoffice@warehouse.com.pl")
        phone_label = QtWidgets.QLabel("Telefon:    +48 (733) 466 111 / +48 (609) 701 211")
        address_label = QtWidgets.QLabel("Adres:       23-333 Poznańska 36b/f, Gdańsk, Poland")

        email_label.setStyleSheet("font-size: 19px; color: red; font-weight: bold;")
        phone_label.setStyleSheet("font-size: 19px; color: red; font-weight: bold;")
        address_label.setStyleSheet("font-size: 19px; color: red; font-weight: bold;")

        contact_info_layout.addWidget(email_label)
        contact_info_layout.addWidget(phone_label)
        contact_info_layout.addWidget(address_label)

        
        form_layout = QtWidgets.QFormLayout()
        form_layout.setSpacing(20)

        name_label = QtWidgets.QLabel("Imię i nazwisko:")
        name_input = QtWidgets.QLineEdit()
        name_input.setStyleSheet("font-size: 19px; border: 2px solid #ccc; border-radius: 5px;")

        subject_label = QtWidgets.QLabel("Temat:")
        subject_input = QtWidgets.QLineEdit()
        subject_input.setStyleSheet("font-size: 19px; border: 2px solid #ccc; border-radius: 5px;")

        message_label = QtWidgets.QLabel("Wiadomość:")
        message_input = QtWidgets.QTextEdit()
        message_input.setStyleSheet("font-size: 19px; border: 2px solid #ccc; border-radius: 5px;")
        
        name_label.setStyleSheet("font-size: 19px; color: yellow; font-weight: bold;")
        subject_label.setStyleSheet("font-size: 19px; color: yellow; font-weight: bold;")
        message_label.setStyleSheet("font-size: 19px; color: yellow; font-weight: bold;")

        form_layout.addRow(name_label, name_input)
        form_layout.addRow(subject_label, subject_input)
        form_layout.addRow(message_label, message_input)

        send_button = QtWidgets.QPushButton("Wyślij")
        send_button.setStyleSheet("background-color: #007bff; color: white; font-size: 18px; border: none; border-radius: 5px; padding: 10px;") 

        send_button.clicked.connect(self.send_message)

        contact_info_layout.addLayout(form_layout) 

        main_layout.addLayout(contact_info_layout)  
        main_layout.addWidget(send_button, alignment=QtCore.Qt.AlignRight)  

        self.setLayout(main_layout)

    def send_message(self):
        # Tutaj można dodać logikę wysyłania wiadomości e-mail
        QtWidgets.QMessageBox.information(self, "Wysłano", "Wiadomość została wysłana pomyślnie.")

    def resizeEvent(self, event):
        self.update_background()
        super().resizeEvent(event)

    def update_background(self):
        pixmap = QtGui.QPixmap('C:/Users/mperz/Desktop/MAIG WAREHOUSE/JPEGEIMAGE/New-World-niszczy-GPU.jpg')
        pixmap = pixmap.scaled(self.width(), self.height())
        self.background_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = HelpWindow()
    window.show()
    app.exec_()









