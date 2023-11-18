import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget, QListWidgetItem, QMessageBox, QFormLayout
from PyQt5.QtGui import QColor, QPixmap, QFont
from PyQt5.QtCore import Qt

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

class ClientInfoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Informacje o Kliencie")

        self.layout = QVBoxLayout()

        self.background_image_path = r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\alsn20210928150320120vwuc.jpg"
        background_image = QPixmap(self.background_image_path)
        self.background_label = QLabel(self)
        self.background_label.setPixmap(background_image)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.form_layout = QFormLayout()

        self.edit_pelna_nazwa = QLineEdit(self)
        self.edit_pelna_nazwa.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Pełna Nazwa Firmy:</font>"), self.edit_pelna_nazwa)

        self.edit_skrocona_nazwa = QLineEdit(self)
        self.edit_skrocona_nazwa.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Skrócona Nazwa Firmy:</font>"), self.edit_skrocona_nazwa)

        self.edit_nip = QLineEdit(self)
        self.edit_nip.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>NIP:</font>"), self.edit_nip)

        self.edit_kod_pocztowy = QLineEdit(self)
        self.edit_kod_pocztowy.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Kod Pocztowy:</font>"), self.edit_kod_pocztowy)

        self.edit_ulica = QLineEdit(self)
        self.edit_ulica.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Ulica:</font>"), self.edit_ulica)

        self.edit_wlasciciel = QLineEdit(self)
        self.edit_wlasciciel.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Właściciel:</font>"), self.edit_wlasciciel)

        self.edit_telefon = QLineEdit(self)
        self.edit_telefon.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Telefon:</font>"), self.edit_telefon)

        self.edit_email = QLineEdit(self)
        self.edit_email.setFont(QFont("Arial", 12, QFont.Bold))
        self.form_layout.addRow(QLabel("<font size='4'>Email:</font>"), self.edit_email)

        self.edit_informacje = QTextEdit(self)
        self.form_layout.addRow(QLabel("<font size='4'>Dodatkowe informacje:</font>"), self.edit_informacje)

        self.layout.addLayout(self.form_layout)

        self.button_zapisz = QPushButton("Zapisz", self)
        self.button_zapisz.setStyleSheet("font-size: 20px; background-color: #2ecc71; color: white; padding: 10px 20px;")
        self.button_zapisz.clicked.connect(self.zapisz_klienta)

        self.button_usun = QPushButton("Usuń", self)
        self.button_usun.setStyleSheet("font-size: 20px; background-color: #e74c3c; color: white; padding: 10px 20px;")
        self.button_usun.clicked.connect(self.usun_klienta)

        self.button_wyczysc = QPushButton("Wyczyść pola", self)
        self.button_wyczysc.setStyleSheet("font-size: 20px; background-color: #f39c12; color: white; padding: 10px 20px;")
        self.button_wyczysc.clicked.connect(self.wyczysc_pola)

        self.layout.addWidget(self.button_zapisz)
        self.layout.addWidget(self.button_usun)
        self.layout.addWidget(self.button_wyczysc)

        self.lista_klientow = QListWidget(self)
        self.lista_klientow.setStyleSheet("font-size: 18px; color: white; background-color: #34495e;")  
        self.layout.addWidget(self.lista_klientow)

        central_widget = QWidget(self)
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.klienci = []

        self.lista_klientow.itemClicked.connect(self.pokaz_informacje)

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

        klient = CompanyClient(pelna_nazwa, skrocona_nazwa, nip, kod_pocztowy, ulica, wlasciciel, telefon, email, informacje)
        self.klienci.append(klient)

        item = QListWidgetItem(pelna_nazwa, self.lista_klientow)
        item.setData(1, len(self.klienci) - 1)
        item.setBackground(QColor("#2c3e50")) 

    def usun_klienta(self):
        index = self.lista_klientow.currentRow()
        if index != -1:
            del self.klienci[index]
            self.lista_klientow.takeItem(index)

    def wyczysc_pola(self):
        self.edit_pelna_nazwa.clear()
        self.edit_skrocona_nazwa.clear()
        self.edit_nip.clear()
        self.edit_kod_pocztowy.clear()
        self.edit_ulica.clear()
        self.edit_wlasciciel.clear()
        self.edit_telefon.clear()
        self.edit_email.clear()
        self.edit_informacje.clear()

    def pokaz_informacje(self, item):
        index = item.data(1)
        if index is not None:
            klient = self.klienci[index]
            informacje = f"<b>NIP:</b> {klient.nip}<br><br><b>Kod Pocztowy:</b> {klient.kod_pocztowy}<br><br><b>Ulica:</b> {klient.ulica}<br><br><b>Właściciel:</b> {klient.wlasciciel}<br><br><b>Telefon:</b> {klient.telefon}<br><br><b>Email:</b> {klient.email}<br><br>{str(klient.informacje)}"
            QMessageBox.information(self, klient.pelna_nazwa, informacje)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientInfoWindow()
    window.showMaximized()
    sys.exit(app.exec_())



