import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QGridLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QFormLayout, QDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap, QColor, QPalette, QFont
from PyQt5.QtCore import Qt

class Product:
    def __init__(self, ean, name, description, net_price, vat_rate, quantity):
        self.ean = ean
        self.name = name
        self.description = description
        self.net_price = net_price
        self.vat_rate = vat_rate
        self.quantity = quantity
        self.calculate_gross_price()

    def calculate_gross_price(self):
        self.gross_price = self.net_price * (1 + self.vat_rate / 100)

class WarehouseWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Towary w Magazynie")
        self.setGeometry(100, 100, 800, 600)  # Ustaw rozmiar okna na przykład 800x600

        # Ustaw tło okna
        self.setStyleSheet("background-color: #2c3e50;")  # Kolor tła
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout(self.central_widget)

        # Tabela
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["EAN", "Nazwa", "Opis", "Cena Netto", "VAT", "Cena Brutto", "Ilość"])
        self.table.setStyleSheet("background-color: #ecf0f1; color: #333333; font-size: 14px;")
        self.layout.addWidget(self.table, 0, 0, 1, 3)

        # Formularz dodawania/edycji produktu
        self.form_layout = QFormLayout()
        self.ean_edit = QLineEdit(self)
        self.form_layout.addRow("EAN:", self.ean_edit)
        self.name_edit = QLineEdit(self)
        self.form_layout.addRow("Nazwa:", self.name_edit)
        self.description_edit = QLineEdit(self)
        self.form_layout.addRow("Opis:", self.description_edit)
        self.net_price_edit = QLineEdit(self)
        self.form_layout.addRow("Cena Netto:", self.net_price_edit)
        self.vat_rate_edit = QLineEdit(self)
        self.form_layout.addRow("VAT (%):", self.vat_rate_edit)
        self.gross_price_label = QLabel(self)
        self.form_layout.addRow("Cena Brutto:", self.gross_price_label)
        self.quantity_edit = QLineEdit(self)
        self.form_layout.addRow("Ilość:", self.quantity_edit)

        self.layout.addLayout(self.form_layout, 1, 0, 1, 2)

        # Przyciski
        self.add_button = QPushButton("Dodaj", self)
        self.add_button.clicked.connect(self.add_product)
        self.layout.addWidget(self.add_button, 2, 0)

        self.edit_button = QPushButton("Edytuj", self)
        self.edit_button.clicked.connect(self.edit_product)
        self.layout.addWidget(self.edit_button, 2, 1)

        self.remove_button = QPushButton("Usuń", self)
        self.remove_button.clicked.connect(self.remove_product)
        self.layout.addWidget(self.remove_button, 2, 2)

        # Inne ustawienia
        self.selected_row = -1  # Numer zaznaczonego wiersza w tabeli
        self.setup_styles()

    def setup_styles(self):
        # Stylizacja elementów
        self.setStyleSheet("QLabel { color: black; font-size: 14px; font-weight: bold; }"
                           "QLineEdit { background-color: #ffffff; color: #333333; font-size: 14px; }"
                           "QTableWidget { background-color: #ffffff; color: #333333; font-size: 14px; }"
                           "QPushButton { background-color: #3498db; color: white; font-size: 14px; }")

    def clear_form(self):
        self.ean_edit.clear()
        self.name_edit.clear()
        self.description_edit.clear()
        self.net_price_edit.clear()
        self.vat_rate_edit.clear()
        self.gross_price_label.clear()
        self.quantity_edit.clear()

    def update_gross_price_label(self):
        try:
            net_price = float(self.net_price_edit.text())
            vat_rate = float(self.vat_rate_edit.text())
            gross_price = net_price * (1 + vat_rate / 100)
            self.gross_price_label.setText(f"{gross_price:.2f}")
        except ValueError:
            self.gross_price_label.clear()

    def add_product(self):
        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        quantity = self.quantity_edit.text()

        try:
            net_price = float(net_price)
            vat_rate = float(vat_rate)
            quantity = int(quantity)

            product = Product(ean, name, description, net_price, vat_rate, quantity)

            # Dodaj produkt do tabeli
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(product.ean))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.name))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.description))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{product.net_price:.2f}"))
            self.table.setItem(row_position, 4, QTableWidgetItem(f"{product.vat_rate:.2f}"))
            self.table.setItem(row_position, 5, QTableWidgetItem(f"{product.gross_price:.2f}"))
            self.table.setItem(row_position, 6, QTableWidgetItem(str(product.quantity)))

            self.clear_form()

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Niepoprawne wartości liczbowe!")

    def edit_product(self):
        if self.selected_row == -1:
            QMessageBox.warning(self, "Błąd", "Nie wybrano produktu do edycji.")
            return

        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        quantity = self.quantity_edit.text()

        try:
            net_price = float(net_price)
            vat_rate = float(vat_rate)
            quantity = int(quantity)

            product = Product(ean, name, description, net_price, vat_rate, quantity)

            # Edytuj zaznaczony wiersz
            self.table.setItem(self.selected_row, 0, QTableWidgetItem(product.ean))
            self.table.setItem(self.selected_row, 1, QTableWidgetItem(product.name))
            self.table.setItem(self.selected_row, 2, QTableWidgetItem(product.description))
            self.table.setItem(self.selected_row, 3, QTableWidgetItem(f"{product.net_price:.2f}"))
            self.table.setItem(self.selected_row, 4, QTableWidgetItem(f"{product.vat_rate:.2f}"))
            self.table.setItem(self.selected_row, 5, QTableWidgetItem(f"{product.gross_price:.2f}"))
            self.table.setItem(self.selected_row, 6, QTableWidgetItem(str(product.quantity)))

            self.clear_form()

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Niepoprawne wartości liczbowe!")

    def remove_product(self):
        if self.selected_row == -1:
            QMessageBox.warning(self, "Błąd", "Nie wybrano produktu do usunięcia.")
            return

        self.table.removeRow(self.selected_row)
        self.clear_form()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseWindow()
    window.show()
    sys.exit(app.exec_())











