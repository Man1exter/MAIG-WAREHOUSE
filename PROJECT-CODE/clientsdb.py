import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap, QFont, QDesktopServices
from PyQt5.QtCore import Qt, QUrl

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

        self.setWindowTitle("Aplikacja Klientów")

        button_zapisz = QPushButton("Zapisz Klienta", self)
        button_zapisz.setStyleSheet("font-size: 20px; background-color: #2ecc71; color: white; padding: 10px 20px;")
        button_zapisz.clicked.connect(self.show_zapisz_klienta)

        button_klienci = QPushButton("Klienci Już Zapisani", self)
        button_klienci.setStyleSheet("font-size: 20px; background-color: #3498db; color: white; padding: 10px 20px;")
        button_klienci.clicked.connect(self.show_klienci_zapisani)

        self.layout = QVBoxLayout()
        self.layout.addWidget(button_zapisz)
        self.layout.addWidget(button_klienci)

        central_widget = QWidget(self)
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.background_image_path_main = r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\New-World-niszczy-GPU.jpg"
        background_image_main = QPixmap(self.background_image_path_main)
        background_label_main = QLabel(self)
        background_label_main.setPixmap(background_image_main)
        self.setFixedSize(background_image_main.width(), background_image_main.height())
        self.layout.addWidget(background_label_main)

        # Wyśrodkowanie przycisków
        self.center_buttons()

    def show_zapisz_klienta(self):
        zapisz_okno = ZapiszKlientaWindow(self)
        zapisz_okno.exec_()

    def show_klienci_zapisani(self):
        klienci_okno = KlienciZapisaniWindow(self)
        klienci_okno.exec_()

    def center_buttons(self):
        desktop_geometry = QDesktopServices().availableGeometry()
        button_zapisz = self.layout.itemAt(0).widget()
        button_klienci = self.layout.itemAt(1).widget()

        # Obliczanie pozycji, aby umieścić przyciski na środku okna
        x_zapisz = (desktop_geometry.width() - button_zapisz.width()) // 2
        x_klienci = (desktop_geometry.width() - button_klienci.width()) // 2

        button_zapisz.move(x_zapisz, button_zapisz.y())
        button_klienci.move(x_klienci, button_klienci.y())

class ZapiszKlientaWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Zapisz Klienta")
        self.klienci = []

        self.background_image_path = r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\New-World-niszczy-GPU.jpg"
        background_image = QPixmap(self.background_image_path)
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        self.setFixedSize(background_image.width(), background_image.height())

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

        self.background_image_path = r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\New-World-niszczy-GPU.jpg"
        background_image = QPixmap(self.background_image_path)
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        self.setFixedSize(background_image.width(), background_image.height())

        self.layout = QVBoxLayout()

        self.lista_klientow = QListWidget(self)
        self.lista_klientow.setStyleSheet("font-size: 18px; color: white; background-color: #34495e;")
        self.layout.addWidget(self.lista_klientow)

        self.button_usun = QPushButton("Usuń", self)
        self.button_usun.setStyleSheet("font-size: 20px; background-color: #e74c3c; color: white; padding: 10px 20px;")
        self.button_usun.clicked.connect(self.usun_klienta)
        self.layout.addWidget(self.button_usun)

        self.setLayout(self.layout)

        self.klienci = []
        self.lista_klientow.itemClicked.connect(self.pokaz_informacje)

    def usun_klienta(self):
        index = self.lista_klientow.currentRow()
        if index != -1:
            del self.klienci[index]
            self.lista_klientow.takeItem(index)

    def pokaz_informacje(self, item):
        index = item.data(1)
        if index is not None:
            klient = self.klienci[index]
            informacje = f"<b>NIP:</b> {klient.nip}<br><br><b>Kod Pocztowy:</b> {klient.kod_pocztowy}<br><br><b>Ulica:</b> {klient.ulica}<br><br><b>Właściciel:</b> {klient.wlasciciel}<br><br><b>Telefon:</b> {klient.telefon}<br><br><b>Email:</b> {klient.email}<br><br>{str(klient.informacje)}"
            QMessageBox.information(self, klient.pelna_nazwa, informacje)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())









