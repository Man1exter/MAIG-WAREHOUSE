from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QDialog, QTableWidget, QTableWidgetItem, QGridLayout
from PySide6.QtGui import QScreen

class UserApprovalWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista Użytkowników do Akceptacji")
        self.setGeometry(0, 0, 800, 400)  # Zmiana rozmiaru na 800x400

        # Center the window on the primary screen
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.move((screen_geometry.width() - self.width()) // 2,
                  (screen_geometry.height() - self.height()) // 2)

        layout = QVBoxLayout()

        user_data = [
            {"Imię": "John", "Nazwisko": "Doe", "Telefon": "123-456-789", "Login": "john.doe", "Hasło": "secret", "NIP firmy": "1234567890"},
            {"Imię": "Jane", "Nazwisko": "Smith", "Telefon": "987-654-321", "Login": "jane.smith", "Hasło": "password", "NIP firmy": "0987654321"},
            {"Imię": "Alice", "Nazwisko": "Johnson", "Telefon": "111-222-333", "Login": "alice.johnson", "Hasło": "123456", "NIP firmy": "11112222333"},
            {"Imię": "Bob", "Nazwisko": "Brown", "Telefon": "555-666-777", "Login": "bob.brown", "Hasło": "qwerty", "NIP firmy": "555666777"},
            {"Imię": "Eva", "Nazwisko": "Green", "Telefon": "111-222-333", "Login": "eva.green", "Hasło": "abcdef", "NIP firmy": "11112222333"},
            {"Imię": "Charlie", "Nazwisko": "Chaplin", "Telefon": "555-666-777", "Login": "charlie.chaplin", "Hasło": "xyz123", "NIP firmy": "555666777"}
        ]

        # Dodanie tabeli
        table = QTableWidget(self)
        table.setColumnCount(len(user_data[0]) + 2)  # Dodatkowe kolumny na przyciski "Przyjmij" i "Odrzuć"
        table.setHorizontalHeaderLabels(list(user_data[0].keys()) + ["Akcje"])

        for row, user in enumerate(user_data):
            table.insertRow(row)
            for col, value in enumerate(user.values()):
                item = QTableWidgetItem(str(value))
                table.setItem(row, col, item)

            accept_button = QPushButton("Przyjmij", self)
            accept_button.clicked.connect(lambda _, row=row: self.accept_user(row))
            accept_button.setStyleSheet("background-color: #5cb85c; color: white;")
            table.setCellWidget(row, len(user_data[0]), accept_button)

            reject_button = QPushButton("Odrzuć", self)
            reject_button.clicked.connect(lambda _, row=row: self.reject_user(row))
            reject_button.setStyleSheet("background-color: #d9534f; color: white;")
            table.setCellWidget(row, len(user_data[0]) + 1, reject_button)

        layout.addWidget(table)

        # Dodanie przycisku na samym dole okna
        show_all_users_button = QPushButton("Zalogowani użytkownicy", self)
        show_all_users_button.clicked.connect(self.show_all_users)
        show_all_users_button.setStyleSheet("background-color: #5bc0de; color: white;")
        layout.addWidget(show_all_users_button)

        self.setLayout(layout)

    def accept_user(self, row):
        reply = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno przyjąć użytkownika?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", f"Użytkownik {row + 1} zaakceptowany!")
        else:
            QMessageBox.information(self, "Potwierdzenie", f"Odrzucono akceptację użytkownika {row + 1}.")

    def reject_user(self, row):
        reply = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno odrzucić użytkownika?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", f"Użytkownik {row + 1} odrzucony!")
        else:
            QMessageBox.information(self, "Potwierdzenie", f"Anulowano odrzucenie użytkownika {row + 1}.")

    def delete_user(self, row):
        reply = QMessageBox.question(self, "Potwierdzenie", f"Czy na pewno usunąć użytkownika {row + 1}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", f"Użytkownik {row + 1} usunięty!")
        else:
            QMessageBox.information(self, "Potwierdzenie", f"Anulowano usunięcie użytkownika {row + 1}.")

    def show_all_users(self):
        dialog = AllUsersDialog(self)
        dialog.exec()


class AllUsersDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Zalogowani Użytkownicy")
        self.setGeometry(0, 0, 800, 600)  # Rozmiar na 800x600

        layout = QGridLayout()

        users = [
            {"Imię": "John", "Nazwisko": "Doe", "Login": "john.doe"},
            {"Imię": "Jane", "Nazwisko": "Smith", "Login": "jane.smith"},
            {"Imię": "Alice", "Nazwisko": "Johnson", "Login": "alice.johnson"},
            {"Imię": "Bob", "Nazwisko": "Brown", "Login": "bob.brown"},
            {"Imię": "Eva", "Nazwisko": "Green", "Login": "eva.green"},
            {"Imię": "Charlie", "Nazwisko": "Chaplin", "Login": "charlie.chaplin"}
        ]

        for row, user in enumerate(users):
            for col, (key, value) in enumerate(user.items()):
                label = QLabel(f"{key}: {value}")
                label.setStyleSheet("padding: 10px; border: 1px solid #ddd; background-color: #f5f5f5;")
                layout.addWidget(label, row, col)

            delete_button = QPushButton("Usuń", self)
            delete_button.clicked.connect(lambda _, user=user: self.delete_logged_in_user(user))
            delete_button.setStyleSheet("background-color: #d9534f; color: white;")
            layout.addWidget(delete_button, row, len(user))

        self.setLayout(layout)

    def delete_logged_in_user(self, user):
        login = user["Login"]
        reply = QMessageBox.question(self, "Potwierdzenie", f"Czy na pewno usunąć użytkownika {login}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, "Potwierdzenie", f"Użytkownik {login} usunięty!")
        else:
            QMessageBox.information(self, "Potwierdzenie", f"Anulowano usunięcie użytkownika {login}.")


if __name__ == "__main__":
    app = QApplication([])

    window = UserApprovalWindow()
    window.show()

    app.exec()












