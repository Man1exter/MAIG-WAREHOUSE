import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QGroupBox, QStackedWidget, QHBoxLayout, QDesktopWidget, QMessageBox,
    QVBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt

class Product:
    def __init__(self, ean, name, description, net_price, vat_rate, gross_price, quantity):
        self.ean = ean
        self.name = name
        self.description = description
        self.net_price = net_price
        self.vat_rate = vat_rate
        self.gross_price = gross_price
        self.quantity = quantity

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
        table_group = QGroupBox()
        table_layout = QVBoxLayout(table_group)

        self.table = QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["EAN", "Nazwa", "Opis", "Cena Netto", "VAT", "Cena Brutto", "Ilość", "", ""])
        table_layout.addWidget(self.table)

        main_layout.addWidget(table_group)

        # Grupa dla formularza
        form_group = QGroupBox("Formularz")
        form_group_layout = QVBoxLayout(form_group)

        # Odstęp od góry tekstu "Formularz"
        form_group_layout.setContentsMargins(0, 10, 0, 0)

        form_layout = QFormLayout()

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

        self.gross_price_edit = QLineEdit(self)
        form_layout.addRow("Cena Brutto:", self.gross_price_edit)

        self.quantity_edit = QLineEdit(self)
        form_layout.addRow("Ilość:", self.quantity_edit)

        # Przycisk Dodaj pod formularzem
        self.add_button = QPushButton("Dodaj", self)
        self.add_button.clicked.connect(self.add_product)
        form_layout.addRow(self.add_button)

        # Pole do wyszukiwania produktu po nazwie
        self.search_edit = QLineEdit(self)
        self.search_edit.setPlaceholderText("Wyszukaj produkt po nazwie")
        self.search_edit.textChanged.connect(self.search_products)
        form_layout.addRow(self.search_edit)

        form_group_layout.addLayout(form_layout)

        main_layout.addWidget(form_group)

        # Inne ustawienia
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

            QTableWidget::item {
                padding: 10px;  /* Zwiększenie wysokości rubryki */
            }

            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
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
        self.gross_price_edit.clear()
        self.quantity_edit.clear()

    def update_gross_price_edit(self):
        try:
            net_price = float(self.net_price_edit.text())
            vat_rate = float(self.vat_rate_edit.text())
            gross_price = net_price * (1 + vat_rate / 100)
            self.gross_price_edit.setText(f"{gross_price:.2f}")
        except ValueError:
            self.gross_price_edit.clear()

    def add_product(self):
        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        gross_price = self.gross_price_edit.text()
        quantity = self.quantity_edit.text()

        try:
            net_price = float(net_price)
            vat_rate = float(vat_rate)
            gross_price = float(gross_price)
            quantity = int(quantity)

            product = Product(ean, name, description, net_price, vat_rate, gross_price, quantity)

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(product.ean))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.name))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.description))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{product.net_price:.2f}"))
            self.table.setItem(row_position, 4, QTableWidgetItem(f"{product.vat_rate:.2f}"))
            self.table.setItem(row_position, 5, QTableWidgetItem(f"{product.gross_price:.2f}"))
            self.table.setItem(row_position, 6, QTableWidgetItem(str(product.quantity)))

            edit_button = QPushButton("Edytuj", self)
            edit_button.clicked.connect(lambda _, row=row_position: self.edit_product_row(row))
            edit_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 14px; border: 2px solid #2ecc71; border-radius: 8px; padding: 8px;")
            self.table.setCellWidget(row_position, 7, edit_button)

            remove_button = QPushButton("Usuń", self)
            remove_button.clicked.connect(lambda _, row=row_position: self.remove_product_row(row))
            remove_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 14px; border: 2px solid #e74c3c; border-radius: 8px; padding: 8px;")
            self.table.setCellWidget(row_position, 8, remove_button)

            self.clear_form()

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Niepoprawne wartości liczbowe!")

    def search_products(self):
        search_text = self.search_edit.text().lower()

        for row in range(self.table.rowCount()):
            name_item = self.table.item(row, 1)
            if search_text in name_item.text().lower():
                self.table.setRowHidden(row, False)
            else:
                self.table.setRowHidden(row, True)

    def edit_product_row(self, row):
        self.selected_row = row
        ean_item = self.table.item(row, 0)
        name_item = self.table.item(row, 1)
        description_item = self.table.item(row, 2)
        net_price_item = self.table.item(row, 3)
        vat_rate_item = self.table.item(row, 4)
        gross_price_item = self.table.item(row, 5)
        quantity_item = self.table.item(row, 6)

        self.ean_edit.setText(ean_item.text())
        self.name_edit.setText(name_item.text())
        self.description_edit.setText(description_item.text())
        self.net_price_edit.setText(net_price_item.text())
        self.vat_rate_edit.setText(vat_rate_item.text())
        self.gross_price_edit.setText(gross_price_item.text())
        self.quantity_edit.setText(quantity_item.text())

    def edit_product(self):
        if self.selected_row == -1:
            QMessageBox.warning(self, "Błąd", "Nie wybrano produktu do edycji.")
            return

        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        gross_price = self.gross_price_edit.text()
        quantity = self.quantity_edit.text()

        try:
            net_price = float(net_price)
            vat_rate = float(vat_rate)
            gross_price = float(gross_price)
            quantity = int(quantity)

            product = Product(ean, name, description, net_price, vat_rate, gross_price, quantity)

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

    def remove_product_row(self, row):
        confirmation = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno chcesz usunąć ten produkt?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.table.removeRow(row)
            self.clear_form()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseWindow()
    window.show()
    sys.exit(app.exec_())






















