import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget, QListWidgetItem, QMessageBox
from PySide6.QtGui import QColor, QFont

class Klient:
    def __init__(self, imie, nazwisko, reklamacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.reklamacja = reklamacja

class KlientWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.klienci = []

        self.setWindowTitle("Okno Reklamacji")
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(), QApplication.primaryScreen().size().height())

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()

        # Lewa strona
        self.left_layout = QVBoxLayout()

        self.label_imie = QLabel("Imię:", self)
        self.label_imie.setStyleSheet("font-size: 20px; color: #003366;")
        self.edit_imie = QLineEdit(self)
        self.edit_imie.setStyleSheet("font-size: 18px;")

        self.label_nazwisko = QLabel("Nazwisko:", self)
        self.label_nazwisko.setStyleSheet("font-size: 20px; color: #003366;")
        self.edit_nazwisko = QLineEdit(self)
        self.edit_nazwisko.setStyleSheet("font-size: 18px;")

        self.label_reklamacja = QLabel("Opis wady reklamacyjnej:", self)
        self.label_reklamacja.setStyleSheet("font-size: 20px; color: #003366;")
        self.edit_reklamacja = QTextEdit(self)
        self.edit_reklamacja.setStyleSheet("font-size: 18px;")

        self.button_dodaj = QPushButton("Dodaj klienta", self)
        self.button_dodaj.setStyleSheet("font-size: 20px; background-color: #4CAF50; color: white; padding: 10px 20px;")
        self.button_dodaj.clicked.connect(self.dodaj_klienta)

        self.button_edytuj = QPushButton("Edytuj klienta", self)
        self.button_edytuj.setStyleSheet("font-size: 20px; background-color: #FFD700; color: white; padding: 10px 20px;")
        self.button_edytuj.clicked.connect(self.edytuj_klienta)

        self.button_usun = QPushButton("Usuń klienta", self)
        self.button_usun.setStyleSheet("font-size: 20px; background-color: #FF6347; color: white; padding: 10px 20px;")
        self.button_usun.clicked.connect(self.usun_klienta)

        self.left_layout.addWidget(self.label_imie)
        self.left_layout.addWidget(self.edit_imie)
        self.left_layout.addWidget(self.label_nazwisko)
        self.left_layout.addWidget(self.edit_nazwisko)
        self.left_layout.addWidget(self.label_reklamacja)
        self.left_layout.addWidget(self.edit_reklamacja)
        self.left_layout.addWidget(self.button_dodaj)
        self.left_layout.addWidget(self.button_edytuj)
        self.left_layout.addWidget(self.button_usun)

        # Prawa strona
        self.right_layout = QVBoxLayout()

        self.label_reklamacje = QLabel("Aktualne reklamacje:", self)
        self.label_reklamacje.setStyleSheet("font-size: 20px; color: #003366;")

        self.list_reklamacje = QListWidget(self)
        self.list_reklamacje.setStyleSheet("font-size: 18px;")
        self.right_layout.addWidget(self.label_reklamacje)
        self.right_layout.addWidget(self.list_reklamacje)

        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)

        self.central_widget.setLayout(self.layout)

    def dodaj_klienta(self):
        imie = self.edit_imie.text()
        nazwisko = self.edit_nazwisko.text()
        reklamacja = self.edit_reklamacja.toPlainText()

        klient = Klient(imie, nazwisko, reklamacja)
        self.klienci.append(klient)

        self.show_message("Dodano klienta", f"Dodano klienta: {imie} {nazwisko}")

        self.clear_inputs()
        self.refresh_reklamacje_list()

    def edytuj_klienta(self):
        index = self.get_selected_index()

        if index != -1:
            imie = self.edit_imie.text()
            nazwisko = self.edit_nazwisko.text()
            reklamacja = self.edit_reklamacja.toPlainText()

            self.klienci[index].imie = imie
            self.klienci[index].nazwisko = nazwisko
            self.klienci[index].reklamacja = reklamacja

            self.show_message("Zaktualizowano klienta", f"Zaktualizowano klienta: {imie} {nazwisko}")

            self.clear_inputs()
            self.refresh_reklamacje_list()

    def usun_klienta(self):
        index = self.get_selected_index()

        if index != -1:
            imie = self.klienci[index].imie
            nazwisko = self.klienci[index].nazwisko

            del self.klienci[index]

            self.show_message("Usunięto klienta", f"Usunięto klienta: {imie} {nazwisko}")

            self.clear_inputs()
            self.refresh_reklamacje_list()

    def clear_inputs(self):
        self.edit_imie.clear()
        self.edit_nazwisko.clear()
        self.edit_reklamacja.clear()

    def get_selected_index(self):
        # Ta funkcja zwraca indeks zaznaczonego klienta lub -1, jeśli nic nie jest zaznaczone.
        # Możesz dostosować tę funkcję w zależności od sposobu, w jaki będziesz zarządzać zaznaczonym klientem.
        # W tym przykładzie zakładam, że zawsze będzie dostępny tylko jeden zaznaczony klient.
        return 0 if self.klienci else -1

    def show_message(self, title, content):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.exec_()

    def refresh_reklamacje_list(self):
        self.list_reklamacje.clear()
        for klient in self.klienci:
            item = QListWidgetItem(f"{klient.imie} {klient.nazwisko}: {klient.reklamacja}")
            self.list_reklamacje.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow {background-color: #F5F5F5;}")
    window = KlientWindow()
    window.show()
    sys.exit(app.exec_())



