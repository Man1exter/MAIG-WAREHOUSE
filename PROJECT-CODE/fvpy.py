import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QTextEdit, QFormLayout, QGroupBox, QStyleFactory, QSpacerItem, QSizePolicy, QGridLayout, QMessageBox, QInputDialog
)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
import random

class Product:
    def __init__(self, name, price_netto, vat, stock):
        self.name = name
        self.price_netto = price_netto
        self.vat = vat
        self.stock = stock

class Transaction:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class InvoiceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Aplikacja Fakturowa')
        self.setGeometry(100, 100, 800, 600)

        # Dane firmy
        self.company_data = {
            'nazwa': 'Twoja Firma',
            'adres': 'ul. Główna 123, Miasto, Kraj',
            'email': 'twoja_firma@example.com',
            'telefon': '123-456-7890'
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
            Product('Produkt 1', 50.0, 23, 100),
            Product('Produkt 2', 30.0, 8, 50),
            Product('Produkt 3', 70.0, 23, 75),
            Product('Produkt 4', 20.0, 8, 120),
            Product('Produkt 5', 60.0, 23, 90)
        ]

        self.transactions = []

        # Widgets
        self.invoice_text_edit = QTextEdit(self)
        self.invoice_text_edit.setReadOnly(True)

        self.print_button = QPushButton('Drukuj Fakturę', self)
        self.print_button.clicked.connect(self.show_invoice_preview)
        self.print_button.setStyleSheet('background-color: #008CBA; color: white;')

        self.send_email_button = QPushButton('Wyślij Email', self)
        self.send_email_button.clicked.connect(self.send_email)
        self.send_email_button.setStyleSheet('background-color: #f44336; color: white;')

        self.product_table = QTableWidget(self)
        self.product_table.setColumnCount(4)
        self.product_table.setHorizontalHeaderLabels(['Nazwa', 'Cena Netto', 'VAT', 'Stan Magazynowy'])
        self.product_table.setRowCount(len(self.products))
        self.product_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Blokowanie edycji komórek

        for i, product in enumerate(self.products):
            self.product_table.setItem(i, 0, QTableWidgetItem(product.name))
            self.product_table.setItem(i, 1, QTableWidgetItem(str(product.price_netto)))
            self.product_table.setItem(i, 2, QTableWidgetItem(str(product.vat)))
            self.product_table.setItem(i, 3, QTableWidgetItem(str(product.stock)))

        self.customer_info_layout = QFormLayout()
        self.customer_info_layout.addRow('Imię i Nazwisko:', QLineEdit())
        self.customer_info_layout.addRow('Adres:', QLineEdit())
        self.customer_info_layout.addRow('Email:', QLineEdit())
        self.customer_info_layout.addRow('Telefon:', QLineEdit())

        self.add_transaction_button = QPushButton('Dodaj Produkt do Faktury', self)
        self.add_transaction_button.clicked.connect(self.add_transaction)

        # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)

        product_layout = QVBoxLayout()
        product_layout.addWidget(QLabel('Dostępne Produkty'))
        product_layout.addWidget(self.product_table)
        product_layout.addWidget(self.add_transaction_button)

        main_layout.addLayout(product_layout)

        invoice_layout = QVBoxLayout()
        invoice_layout.addWidget(QLabel('Podgląd Faktury'))
        invoice_layout.addWidget(self.invoice_text_edit)

        main_layout.addLayout(invoice_layout)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.print_button)
        button_layout.addWidget(self.send_email_button)

        main_layout.addLayout(button_layout)

        customer_info_groupbox = QGroupBox('Dane Klienta')
        customer_info_groupbox.setLayout(self.customer_info_layout)
        main_layout.addWidget(customer_info_groupbox)

    def add_transaction(self):
        selected_row = self.product_table.currentRow()
        if selected_row >= 0:
            quantity, ok = self.get_quantity_input()
            if ok:
                selected_product = self.products[selected_row]
                if selected_product.stock >= quantity:
                    selected_product.stock -= quantity
                    self.transactions.append(Transaction(selected_product, quantity))
                    self.update_invoice_preview()
                else:
                    QMessageBox.warning(self, 'Stan Magazynowy', 'Nie wystarczająca ilość produktu na magazynie.')
        else:
            QMessageBox.warning(self, 'Brak Wybranego Produktu', 'Proszę wybrać produkt z tabeli.')

    def get_quantity_input(self):
        quantity, ok = QInputDialog.getInt(self, 'Ilość', 'Podaj ilość produktu:')
        return quantity, ok

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

        # Dodaj tabelę z transakcjami
        self.invoice_text_edit.append('Produkty w Fakturze:\n')
        table_text = '{:<20} {:<10} {:<10} {:<10} {:<10}'.format('Nazwa', 'Ilość', 'Cena Netto', 'VAT', 'Cena Brutto')
        self.invoice_text_edit.append(table_text)
        self.invoice_text_edit.append('-' * len(table_text))

        suma_netto = 0
        suma_brutto = 0

        for transaction in self.transactions:
            product = transaction.product
            quantity = transaction.quantity

            cena_netto = product.price_netto * quantity
            vat = product.vat
            cena_brutto = cena_netto + cena_netto * (vat / 100)

            suma_netto += cena_netto
            suma_brutto += cena_brutto

            row_text = '{:<20} {:<10} {:<10.2f} {:<10} {:<10.2f}'.format(
                product.name, quantity, cena_netto, f'{vat}%', cena_brutto)
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









