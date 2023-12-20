import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QTextEdit, QFormLayout, QGroupBox, QStyleFactory, QSpacerItem, QSizePolicy, QGridLayout, QMessageBox
)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
import random

class InvoiceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Aplikacja Fakturowa')
        self.setGeometry(100, 100, 800, 600)

        # Dane firmy
        self.company_data = {
            'nazwa': '',
            'adres': '',
            'email': '',
            'telefon': ''
        }

        # Dane klienta
        self.client_data = {
            'nazwa': '',
            'adres': '',
            'email': '',
            'telefon': ''
        }

        # Produkty
        self.products = [
            {'nazwa': 'Produkt 1', 'cena_netto': 50.0, 'vat': 23},
            {'nazwa': 'Produkt 2', 'cena_netto': 30.0, 'vat': 8},
            {'nazwa': 'Produkt 3', 'cena_netto': 70.0, 'vat': 23},
            {'nazwa': 'Produkt 4', 'cena_netto': 20.0, 'vat': 8},
            {'nazwa': 'Produkt 5', 'cena_netto': 60.0, 'vat': 23}
        ]

        # Widgets
        self.invoice_text_edit = QTextEdit(self)
        self.invoice_text_edit.setReadOnly(True)

        self.print_button = QPushButton('Drukuj Fakturę', self)
        self.print_button.clicked.connect(self.show_invoice_preview)
        self.print_button.setStyleSheet('background-color: #008CBA; color: white;')

        self.send_email_button = QPushButton('Wyślij Email', self)
        self.send_email_button.clicked.connect(self.send_email)
        self.send_email_button.setStyleSheet('background-color: #f44336; color: white;')

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)

        invoice_layout = QVBoxLayout()
        invoice_layout.addWidget(QLabel('Podgląd Faktury'))
        invoice_layout.addWidget(self.invoice_text_edit)

        main_layout.addLayout(invoice_layout)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.print_button)
        button_layout.addWidget(self.send_email_button)

        main_layout.addLayout(button_layout)

        self.update_invoice_preview()

    def update_invoice_preview(self):
        self.invoice_text_edit.clear()

        # Dodaj dane firmy
        self.invoice_text_edit.append(f'Dane Twojej Firmy:\n\n'
                                      f'Nazwa: {self.company_data["nazwa"]}\n'
                                      f'Adres: {self.company_data["adres"]}\n'
                                      f'Email: {self.company_data["email"]}\n'
                                      f'Telefon: {self.company_data["telefon"]}\n\n')

        # Dodaj dane klienta
        self.invoice_text_edit.append(f'Dane Klienta:\n\n'
                                      f'Nazwa: {self.client_data["nazwa"]}\n'
                                      f'Adres: {self.client_data["adres"]}\n'
                                      f'Email: {self.client_data["email"]}\n'
                                      f'Telefon: {self.client_data["telefon"]}\n\n')

        # Dodaj tabelę z produktami
        self.invoice_text_edit.append('Produkty:\n')
        table_text = '{:<20} {:<15} {:<15} {:<15}'.format('Nazwa', 'Cena Netto', 'VAT', 'Cena Brutto')
        self.invoice_text_edit.append(table_text)
        self.invoice_text_edit.append('-' * len(table_text))

        suma_netto = 0
        suma_brutto = 0

        for product in self.products:
            cena_netto = product['cena_netto']
            vat = product['vat']
            cena_brutto = cena_netto + cena_netto * (vat / 100)

            suma_netto += cena_netto
            suma_brutto += cena_brutto

            row_text = '{:<20} {:<15.2f} {:<15} {:<15.2f}'.format(
                product['nazwa'], cena_netto, f'{vat}%', cena_brutto)
            self.invoice_text_edit.append(row_text)

        self.invoice_text_edit.append('\nŁączna suma Netto: {:.2f}'.format(suma_netto))
        self.invoice_text_edit.append('Łączna suma Brutto: {:.2f}'.format(suma_brutto))

    def show_invoice_preview(self):
        invoice_preview = QTextEdit()
        invoice_preview.setPlainText(self.invoice_text_edit.toPlainText())

        preview_window = QWidget(self)
        preview_window.setWindowTitle('Podgląd Faktury')
        preview_window.setGeometry(200, 200, 600, 400)
        layout = QVBoxLayout(preview_window)
        layout.addWidget(invoice_preview)

        print_dialog = QPrintDialog()
        if print_dialog.exec_() == QPrintDialog.Accepted:
            printer = QPrinter()
            printer.setOutputFileName('faktura.pdf')
            invoice_preview.print_(printer)

    def send_email(self):
        try:
            serwer = smtplib.SMTP('twoj_serwer_smtp.com', 587)
            serwer.starttls()
            serwer.login('twoj_email@example.com', 'twoje_haslo_email')

            temat = 'Faktura od Twojej Firmy'
            tresc = self.invoice_text_edit.toPlainText()

            wiadomosc = MIMEMultipart()
            wiadomosc['From'] = self.company_data['email']
            wiadomosc['To'] = self.client_data['email']
            wiadomosc['Subject'] = temat

            wiadomosc.attach(MIMEText(tresc, 'plain'))

            zalacznik = MIMEApplication(open('faktura.pdf', 'rb').read(), _subtype="pdf")
            zalacznik.add_header('Content-Disposition', 'attachment', filename='faktura.pdf')
            wiadomosc.attach(zalacznik)

            serwer.sendmail(self.company_data['email'], self.client_data['email'], wiadomosc.as_string())
            serwer.quit()

            QMessageBox.information(self, 'Email Wysłany', 'Faktura wysłana pomyślnie.')
        except Exception as e:
            QMessageBox.warning(self, 'Błąd', f'Błąd podczas wysyłania emaila: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = InvoiceApp()
    window.show()
    sys.exit(app.exec())








