import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

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
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_imie = QLabel("Imię:", self)
        self.edit_imie = QLineEdit(self)

        self.label_nazwisko = QLabel("Nazwisko:", self)
        self.edit_nazwisko = QLineEdit(self)

        self.label_reklamacja = QLabel("Opis wady reklamacyjnej:", self)
        self.edit_reklamacja = QTextEdit(self)

        self.button_dodaj = QPushButton("Dodaj klienta", self)
        self.button_dodaj.clicked.connect(self.dodaj_klienta)

        self.button_edytuj = QPushButton("Edytuj klienta", self)
        self.button_edytuj.clicked.connect(self.edytuj_klienta)

        self.button_usun = QPushButton("Usuń klienta", self)
        self.button_usun.clicked.connect(self.usun_klienta)

        self.layout.addWidget(self.label_imie)
        self.layout.addWidget(self.edit_imie)
        self.layout.addWidget(self.label_nazwisko)
        self.layout.addWidget(self.edit_nazwisko)
        self.layout.addWidget(self.label_reklamacja)
        self.layout.addWidget(self.edit_reklamacja)
        self.layout.addWidget(self.button_dodaj)
        self.layout.addWidget(self.button_edytuj)
        self.layout.addWidget(self.button_usun)

        self.central_widget.setLayout(self.layout)

    def dodaj_klienta(self):
        imie = self.edit_imie.text()
        nazwisko = self.edit_nazwisko.text()
        reklamacja = self.edit_reklamacja.toPlainText()

        klient = Klient(imie, nazwisko, reklamacja)
        self.klienci.append(klient)

        self.show_message("Dodano klienta", f"Dodano klienta: {imie} {nazwisko}")

        self.clear_inputs()

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

    def usun_klienta(self):
        index = self.get_selected_index()

        if index != -1:
            imie = self.klienci[index].imie
            nazwisko = self.klienci[index].nazwisko

            del self.klienci[index]

            self.show_message("Usunięto klienta", f"Usunięto klienta: {imie} {nazwisko}")

            self.clear_inputs()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KlientWindow()
    window.show()
    sys.exit(app.exec_())
