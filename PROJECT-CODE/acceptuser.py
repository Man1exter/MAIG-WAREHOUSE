from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox

class UserApprovalWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Approval")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        label = QLabel("Czy zaakceptować użytkownika?")
        layout.addWidget(label)

        accept_button = QPushButton("Przyznaj dostęp")
        accept_button.clicked.connect(self.accept_user)
        layout.addWidget(accept_button)

        reject_button = QPushButton("Odrzuć dostęp")
        reject_button.clicked.connect(self.reject_user)
        layout.addWidget(reject_button)

        show_data_button = QPushButton("Wyświetl dane użytkownika")
        show_data_button.clicked.connect(self.show_user_data)
        layout.addWidget(show_data_button)

        self.setLayout(layout)

    def accept_user(self):
        reply = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno przyjąć użytkownika?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", "Użytkownik zaakceptowany!")
        else:
            QMessageBox.information(self, "Potwierdzenie", "Odrzucono akceptację użytkownika.")

    def reject_user(self):
        reply = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno odrzucić użytkownika?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", "Użytkownik odrzucony!")
        else:
            QMessageBox.information(self, "Potwierdzenie", "Anulowano odrzucenie użytkownika.")

    def show_user_data(self):
        user_data = {
            "Imię": "John",
            "Nazwisko": "Doe",
            "Telefon": "123-456-789",
            "Login": "john.doe",
            "Hasło": "secret",
            "NIP firmy": "1234567890"
        }

        data_str = "\n".join(f"{key}: {value}" for key, value in user_data.items())
        QMessageBox.information(self, "Dane użytkownika", data_str)

if __name__ == "__main__":
    app = QApplication([])

    window = UserApprovalWindow()
    window.show()

    app.exec()

