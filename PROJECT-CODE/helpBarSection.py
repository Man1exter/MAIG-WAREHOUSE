from PyQt5 import QtWidgets, QtGui, QtCore

class HelpWindow(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Pomoc")
        self.setGeometry(100, 100, 800, 600)
        
        contact_label = QtWidgets.QLabel("Skontaktuj się z NAMI!:")
        contact_info = QtWidgets.QLabel("MAIG SOFTWARE WAREHOUSE\n"
                                         "Adres: ul. Przykładowa 123, 00-000 Warszawa\n"
                                         "Telefon I: +48 123 456 789\n"
                                         "Telefon II: +48 987 654 321\n"
                                         "E-mail: kontakt@example.com\n"
                                         "Godziny pracy: Poniedziałek - Piątek, 8:00 - 16:00")
        contact_info.setAlignment(QtCore.Qt.AlignLeft)
        
        email_label = QtWidgets.QLabel("Wyślij wiadomość:")
        self.email_text = QtWidgets.QTextEdit(self)
        self.email_text.setPlaceholderText("Wprowadź treść wiadomości...")
        
        send_button = QtWidgets.QPushButton("Wyślij", self)
        send_button.clicked.connect(self.send_email)
        
        back_button = QtWidgets.QPushButton("Cofnij", self)
        back_button.clicked.connect(self.close)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(contact_label)
        layout.addWidget(contact_info)
        layout.addWidget(email_label)
        layout.addWidget(self.email_text)
        layout.addWidget(send_button)
        layout.addWidget(back_button)
        
        self.setLayout(layout)

    def send_email(self):
        email_content = self.email_text.toPlainText()
        # Tutaj możesz dodać kod do wysyłania e-maila, np. korzystając z modułu smtplib.
        # W rzeczywistości trzeba będzie dodać logikę obsługi wysyłania e-maila.

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    help_window = HelpWindow()
    help_window.show()
    app.exec_()