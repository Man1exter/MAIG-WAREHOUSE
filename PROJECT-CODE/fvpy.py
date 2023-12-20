import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QTextEdit, QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas

class InvoiceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Invoice Application')

        # Widgets
        self.product_list = QListWidget(self)
        self.product_list.addItems(['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'])
        self.product_list.setStyleSheet('background-color: #f0f0f0;')

        self.quantity_label = QLabel('Quantity:', self)
        self.quantity_input = QLineEdit(self)
        self.quantity_input.setStyleSheet('background-color: #e0e0e0;')

        self.price_label = QLabel('Price (brutto):', self)
        self.price_input = QLineEdit(self)
        self.price_input.setStyleSheet('background-color: #e0e0e0;')

        self.vat_label = QLabel('VAT (%):', self)
        self.vat_input = QLineEdit(self)
        self.vat_input.setStyleSheet('background-color: #e0e0e0;')

        self.description_label = QLabel('Description:', self)
        self.description_input = QLineEdit(self)
        self.description_input.setStyleSheet('background-color: #e0e0e0;')

        self.ean_label = QLabel('EAN:', self)
        self.ean_input = QLineEdit(self)
        self.ean_input.setStyleSheet('background-color: #e0e0e0;')

        self.add_button = QPushButton('Add Item', self)
        self.add_button.clicked.connect(self.add_item)
        self.add_button.setStyleSheet('background-color: #4CAF50; color: white;')

        self.print_button = QPushButton('Print Invoice', self)
        self.print_button.clicked.connect(self.print_invoice)
        self.print_button.setStyleSheet('background-color: #008CBA; color: white;')

        self.send_email_button = QPushButton('Send Email', self)
        self.send_email_button.clicked.connect(self.send_email)
        self.send_email_button.setStyleSheet('background-color: #f44336; color: white;')

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.product_list)
        self.layout.addWidget(self.quantity_label)
        self.layout.addWidget(self.quantity_input)
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.vat_label)
        self.layout.addWidget(self.vat_input)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.description_input)
        self.layout.addWidget(self.ean_label)
        self.layout.addWidget(self.ean_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.print_button)
        self.layout.addWidget(self.send_email_button)

        self.invoice_text_edit = QTextEdit(self)
        self.layout.addWidget(self.invoice_text_edit)

        # Dummy company data
        self.sender_company = {
            'name': 'Your Company Name',
            'address': '123 Main Street, City, Country',
            'email': 'yourcompany@example.com',
            'phone': '123-456-7890'
        }

        self.receiver_company = {
            'name': 'Client Company',
            'address': '456 Client Street, City, Country',
            'email': 'client@example.com',
            'phone': '987-654-3210'
        }

    def add_item(self):
        selected_product = self.product_list.currentItem().text()
        quantity = self.quantity_input.text()
        price = self.price_input.text()
        vat = self.vat_input.text()
        description = self.description_input.text()
        ean = self.ean_input.text()

        item_info = f'{quantity} x {selected_product}, Price: {price}, VAT: {vat}, Description: {description}, EAN: {ean}'
        self.invoice_text_edit.append(item_info)

    def print_invoice(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            painter = canvas.Canvas('invoice.pdf')
            invoice_content = self.invoice_text_edit.toPlainText()
            painter.drawString(100, 800, f'Invoice from {self.sender_company["name"]} to {self.receiver_company["name"]}')
            painter.drawString(100, 780, '-' * 50)
            painter.drawString(100, 760, invoice_content)
            painter.save()
            
    def send_email(self):
        try:
            server = smtplib.SMTP('your_smtp_server.com', 587)
            server.starttls()
            server.login('your_email@example.com', 'your_email_password')

            subject = 'Invoice from Your Company'
            body = self.invoice_text_edit.toPlainText()

            message = MIMEMultipart()
            message['From'] = self.sender_company['email']
            message['To'] = self.receiver_company['email']
            message['Subject'] = subject

            message.attach(MIMEText(body, 'plain'))

            attachment = MIMEApplication(open('invoice.pdf', 'rb').read(), _subtype="pdf")
            attachment.add_header('Content-Disposition', 'attachment', filename='invoice.pdf')
            message.attach(attachment)

            server.sendmail(self.sender_company['email'], self.receiver_company['email'], message.as_string())
            server.quit()

            QMessageBox.information(self, 'Email Sent', 'Invoice sent successfully.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Error sending email: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InvoiceApp()
    window.show()
    sys.exit(app.exec())



