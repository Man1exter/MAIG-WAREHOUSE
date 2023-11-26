import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QGroupBox, QStackedWidget, QHBoxLayout, QDesktopWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap, QPalette, QColor
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

        # Ustawienie tła
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        self.setPalette(palette)

        # Główny widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Układ główny
        main_layout = QHBoxLayout(main_widget)

        # Grupa dla tabeli
        table_group = QGroupBox("Tabela")
        table_layout = QVBoxLayout(table_group)

        self.table = QTableWidget(self)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["EAN", "Nazwa", "Opis", "Cena Netto", "VAT", "Cena Brutto", "Ilość", ""])
        table_layout.addWidget(self.table)

        main_layout.addWidget(table_group)

        # Grupa dla formularza
        form_group = QGroupBox("Formularz")
        form_layout = QFormLayout(form_group)

        self.ean_edit = QLineEdit(self)
        form_layout.addRow("EAN:", self.ean_edit)

        self.name_edit = QLineEdit(self)
        form_layout.addRow("Nazwa:", self.name_edit)

        self.description_edit = QLineEdit(self)
        form_layout.addRow("Opis:", self.description_edit)

        self.net_price_edit = QLineEdit(self)
        form_layout.addRow("Cena Netto:", self.net_price_edit)

        self.vat_rate_edit = QLineEdit(self)
        form_layout.addRow("VAT (%):", self.vat_rate_edit)

        self.gross_price_label = QLabel(self)
        form_layout.addRow("Cena Brutto:", self.gross_price_label)

        self.quantity_edit = QLineEdit(self)
        form_layout.addRow("Ilość:", self.quantity_edit)

        main_layout.addWidget(form_group)

        # Przyciski
        button_layout = QVBoxLayout()

        self.add_button = QPushButton("Dodaj", self)
        self.add_button.clicked.connect(self.add_product)
        button_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edytuj", self)
        self.edit_button.clicked.connect(self.edit_product)
        button_layout.addWidget(self.edit_button)

        self.remove_button = QPushButton("Usuń", self)
        self.remove_button.clicked.connect(self.remove_product)
        button_layout.addWidget(self.remove_button)

        main_layout.addLayout(button_layout)

        # Inne ustawienia
        self.selected_row = -1
        self.setup_styles()

        # Ustawienie rozmiarów okna na całą dostępną przestrzeń ekranu
        screen_geometry = QDesktopWidget().availableGeometry()
        self.setGeometry(screen_geometry)
        self.showMaximized()

    def setup_styles(self):
        # Stylizacja elementów
        self.setStyleSheet("""
            QGroupBox {
                font-size: 18px;
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                background-color: white;
            }

            QLabel {
                font-size: 14px;
                font-weight: bold;
            }

            QLineEdit {
                font-size: 14px;
                padding: 6px;
            }

            QTableWidget {
                background-color: white;
                color: #333333;
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 8px;
            }

            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 8px;
            }
        """)

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

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(product.ean))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.name))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.description))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{product.net_price:.2f}"))
            self.table.setItem(row_position, 4, QTableWidgetItem(f"{product.vat_rate:.2f}"))
            self.table.setItem(row_position, 5, QTableWidgetItem(f"{product.gross_price:.2f}"))
            self.table.setItem(row_position, 6, QTableWidgetItem(str(product.quantity)))

            remove_button = QPushButton("Usuń", self)
            remove_button.clicked.connect(lambda _, row=row_position: self.remove_product_row(row))
            remove_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 14px; border: 2px solid #e74c3c; border-radius: 8px; padding: 8px;")
            self.table.setCellWidget(row_position, 7, remove_button)

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

    def remove_product_row(self, row):
        self.table.removeRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseWindow()
    window.show()
    sys.exit(app.exec_())

















