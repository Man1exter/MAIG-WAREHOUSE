import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QWidget, QDesktopWidget, QMessageBox, QInputDialog
)
from PyQt5.QtGui import QFont

class CompanyClient:
    def __init__(self, pelna_nazwa, skrocona_nazwa, nip, kod_pocztowy, ulica, wlasciciel, telefon, email, informacje):
        self.pelna_nazwa = pelna_nazwa
        self.skrocona_nazwa = skrocona_nazwa
        self.nip = nip
        self.kod_pocztowy = kod_pocztowy
        self.ulica = ulica
        self.wlasciciel = wlasciciel
        self.telefon = telefon
        self.email = email
        self.informacje = informacje

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("QMainWindow {background-image: url(C:/Users/mperz/Desktop/MAIG WAREHOUSE/JPEGEIMAGE/New-World-niszczy-GPU.jpg);}")

        self.setWindowTitle("Aplikacja Klientów")

        button_zapisz = QPushButton("Zapisz nowego klienta", self)
        button_zapisz.setStyleSheet("font-size: 20px; background-color: #2ecc71; color: white; padding: 10px 20px;")
        button_zapisz.clicked.connect(self.show_zapisz_klienta)

        button_klienci = QPushButton("Klienci", self)
        button_klienci.setStyleSheet("font-size: 20px; background-color: #3498db; color: white; padding: 10px 20px;")
        button_klienci.clicked.connect(self.show_klienci_zapisani)

        self.layout = QVBoxLayout()
        self.layout.addWidget(button_zapisz)
        self.layout.addWidget(button_klienci)

        central_widget = QWidget(self)
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Set window size and center on screen
        self.resize(600, 400)  # Set the desired size
        self.center_on_screen()

    def center_on_screen(self):
        # Get the geometry of the main screen
        screen_geometry = QDesktopWidget().availableGeometry()

        # Get the size and position of the main window
        window_geometry = self.frameGeometry()

        # Center the window on the screen
        window_geometry.moveCenter(screen_geometry.center())

        # Set the new position of the window
        self.move(window_geometry.topLeft())

    def show_zapisz_klienta(self):
        zapisz_okno = ZapiszKlientaWindow(self)
        zapisz_okno.exec_()

    def show_klienci_zapisani(self):
        klienci_okno = KlienciZapisaniWindow(self)
        klienci_okno.exec_()

class ZapiszKlientaWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("QMainWindow {background-image: url(C:/Users/mperz/Desktop/MAIG WAREHOUSE/JPEGEIMAGE/New-World-niszczy-GPU.jpg);}")

        self.setWindowTitle("Zapisz Klienta")
        self.klienci = []

        self.form_layout = QFormLayout()

        self.create_input_field(self.form_layout, "Pełna Nazwa Firmy:", "edit_pelna_nazwa")
        self.create_input_field(self.form_layout, "Skrócona Nazwa Firmy:", "edit_skrocona_nazwa")
        self.create_input_field(self.form_layout, "NIP:", "edit_nip")
        self.create_input_field(self.form_layout, "Kod Pocztowy:", "edit_kod_pocztowy")
        self.create_input_field(self.form_layout, "Ulica:", "edit_ulica")
        self.create_input_field(self.form_layout, "Właściciel:", "edit_wlasciciel")
        self.create_input_field(self.form_layout, "Telefon:", "edit_telefon")
        self.create_input_field(self.form_layout, "Email:", "edit_email")

        self.edit_informacje = QTextEdit(self)
        self.edit_informacje.setStyleSheet("font-size: 12px; color: red;")
        self.form_layout.addRow(QLabel("<font size='4'><b>Dodatkowe informacje:</b></font>"), self.edit_informacje)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)

        self.button_zapisz = QPushButton("Zapisz", self)
        self.button_zapisz.setStyleSheet("font-size: 20px; background-color: #2ecc71; color: white; padding: 10px 20px;")
        self.button_zapisz.clicked.connect(self.zapisz_klienta)
        self.layout.addWidget(self.button_zapisz)

        self.setLayout(self.layout)

    def create_input_field(self, layout, label_text, widget_name):
        label = QLabel(f"<font size='4'>{label_text}</font>", self)
        label.setStyleSheet("font-weight: bold; color: red;")
        edit = QLineEdit(self)
        edit.setFont(QFont("Arial", 12, QFont.Bold))
        setattr(self, widget_name, edit)
        layout.addRow(label, edit)

    def zapisz_klienta(self):
        pelna_nazwa = self.edit_pelna_nazwa.text()
        skrocona_nazwa = self.edit_skrocona_nazwa.text()
        nip = self.edit_nip.text()
        kod_pocztowy = self.edit_kod_pocztowy.text()
        ulica = self.edit_ulica.text()
        wlasciciel = self.edit_wlasciciel.text()
        telefon = self.edit_telefon.text()
        email = self.edit_email.text()
        informacje = self.edit_informacje.toPlainText()

        if not any([pelna_nazwa, skrocona_nazwa, nip, kod_pocztowy, ulica, wlasciciel, telefon, email, informacje]):
            QMessageBox.warning(self, "Błąd", "Nie można dodać pustego klienta.")
            return

        klient = CompanyClient(pelna_nazwa, skrocona_nazwa, nip, kod_pocztowy, ulica, wlasciciel, telefon, email, informacje)
        self.klienci.append(klient)

        self.wyczysc_pola()

    def wyczysc_pola(self):
        for field in ["pelna_nazwa", "skrocona_nazwa", "nip", "kod_pocztowy", "ulica", "wlasciciel", "telefon", "email"]:
            getattr(self, f"edit_{field}").clear()
        self.edit_informacje.clear()

class KlienciZapisaniWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Klienci Już Zapisani")

        self.klienci = []

        self.layout = QVBoxLayout()

        self.lista_klientow = QListWidget(self)
        self.lista_klientow.setStyleSheet("font-size: 18px; color: white; background-color: #34495e;")
        self.layout.addWidget(self.lista_klientow)

        self.button_usun = QPushButton("Usuń", self)
        self.button_usun.setStyleSheet("font-size: 20px; background-color: #e74c3c; color: white; padding: 10px 20px;")
        self.button_usun.clicked.connect(self.usun_klienta)
        self.layout.addWidget(self.button_usun)

        self.button_edytuj = QPushButton("Edytuj", self)
        self.button_edytuj.setStyleSheet("font-size: 20px; background-color: #f39c12; color: white; padding: 10px 20px;")
        self.button_edytuj.clicked.connect(self.edytuj_klienta)
        self.layout.addWidget(self.button_edytuj)

        self.button_wyszukaj = QPushButton("Wyszukaj", self)
        self.button_wyszukaj.setStyleSheet("font-size: 20px; background-color: #3498db; color: white; padding: 10px 20px;")
        self.button_wyszukaj.clicked.connect(self.wyszukaj_klienta)
        self.layout.addWidget(self.button_wyszukaj)

        self.setLayout(self.layout)

        self.lista_klientow.itemClicked.connect(self.pokaz_informacje)

    def usun_klienta(self):
        index = self.lista_klientow.currentRow()
        if index != -1:
            del self.klienci[index]
            self.lista_klientow.takeItem(index)

    def edytuj_klienta(self):
        index = self.lista_klientow.currentRow()
        if index != -1:
            edytuj_okno = EdytujKlientaWindow(self, self.klienci[index])
            edytuj_okno.exec_()

    def wyszukaj_klienta(self):
        search_text, ok = QInputDialog.getText(self, 'Wyszukaj Klienta', 'Podaj nazwę klienta:')
        if ok and search_text:
            found_items = [item for item in self.klienci if search_text.lower() in item.pelna_nazwa.lower()]
            self.update_list(found_items)

    def update_list(self, items):
        self.lista_klientow.clear()
        for item in items:
            self.lista_klientow.addItem(QListWidgetItem(item.pelna_nazwa))

    def pokaz_informacje(self, item):
        index = item.data(1)
        if index is not None:
            klient = self.klienci[index]
            informacje = f"<b>NIP:</b> {klient.nip}<br><br><b>Kod Pocztowy:</b> {klient.kod_pocztowy}<br><br><b>Ulica:</b> {klient.ulica}<br><br><b>Właściciel:</b> {klient.wlasciciel}<br><br><b>Telefon:</b> {klient.telefon}<br><br><b>Email:</b> {klient.email}<br><br>{str(klient.informacje)}"
            QMessageBox.information(self, klient.pelna_nazwa, informacje)

class EdytujKlientaWindow(QDialog):
    def __init__(self, parent=None, klient=None):
        super().__init__(parent)

        self.setWindowTitle("Edytuj Klienta")
        self.klienci = parent.klienci
        self.edytowany_klient = klient

        self.form_layout = QFormLayout()

        self.create_input_field(self.form_layout, "Pełna Nazwa Firmy:", "edit_pelna_nazwa", self.edytowany_klient.pelna_nazwa)
        self.create_input_field(self.form_layout, "Skrócona Nazwa Firmy:", "edit_skrocona_nazwa", self.edytowany_klient.skrocona_nazwa)
        self.create_input_field(self.form_layout, "NIP:", "edit_nip", self.edytowany_klient.nip)
        self.create_input_field(self.form_layout, "Kod Pocztowy:", "edit_kod_pocztowy", self.edytowany_klient.kod_pocztowy)
        self.create_input_field(self.form_layout, "Ulica:", "edit_ulica", self.edytowany_klient.ulica)
        self.create_input_field(self.form_layout, "Właściciel:", "edit_wlasciciel", self.edytowany_klient.wlasciciel)
        self.create_input_field(self.form_layout, "Telefon:", "edit_telefon", self.edytowany_klient.telefon)
        self.create_input_field(self.form_layout, "Email:", "edit_email", self.edytowany_klient.email)

        self.edit_informacje = QTextEdit(self)
        self.edit_informacje.setStyleSheet("font-size: 12px; color: red;")
        self.edit_informacje.setPlainText(str(self.edytowany_klient.informacje))
        self.form_layout.addRow(QLabel("<font size='4'><b>Dodatkowe informacje:</b></font>"), self.edit_informacje)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)

        self.button_zapisz = QPushButton("Zapisz zmiany", self)
        self.button_zapisz.setStyleSheet("font-size: 20px; background-color: #2ecc71; color: white; padding: 10px 20px;")
        self.button_zapisz.clicked.connect(self.zapisz_edycje)
        self.layout.addWidget(self.button_zapisz)

        self.setLayout(self.layout)

    def create_input_field(self, layout, label_text, widget_name, default_value=""):
        label = QLabel(f"<font size='4'>{label_text}</font>", self)
        label.setStyleSheet("font-weight: bold; color: red;")
        edit = QLineEdit(self)
        edit.setFont(QFont("Arial", 12, QFont.Bold))
        edit.setText(default_value)
        setattr(self, widget_name, edit)
        layout.addRow(label, edit)

    def zapisz_edycje(self):
        self.edytowany_klient.pelna_nazwa = self.edit_pelna_nazwa.text()
        self.edytowany_klient.skrocona_nazwa = self.edit_skrocona_nazwa.text()
        self.edytowany_klient.nip = self.edit_nip.text()
        self.edytowany_klient.kod_pocztowy = self.edit_kod_pocztowy.text()
        self.edytowany_klient.ulica = self.edit_ulica.text()
        self.edytowany_klient.wlasciciel = self.edit_wlasciciel.text()
        self.edytowany_klient.telefon = self.edit_telefon.text()
        self.edytowany_klient.email = self.edit_email.text()
        self.edytowany_klient.informacje = self.edit_informacje.toPlainText()

        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())















