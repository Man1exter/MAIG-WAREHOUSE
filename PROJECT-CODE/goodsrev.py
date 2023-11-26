import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QGroupBox, QHeaderView, QDesktopWidget, QMessageBox
)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class Product:
    def __init__(self, index, ean, name, description, net_price, vat_rate, gross_price, quantity):
        self.index = index
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
        main_layout = QVBoxLayout(main_widget)

        # Grupa dla tabeli
        table_group = QGroupBox()
        table_layout = QVBoxLayout(table_group)

        self.table = QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["INDEX", "EAN", "Nazwa", "Opis", "Cena Brutto", "VAT", "Cena Netto", "Ilość", ""])
        table_layout.addWidget(self.table)

        # Stylizacja nagłówków tabeli
        header = self.table.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #3498db; color: black; font-size: 14px; }")
        header.setSectionResizeMode(QHeaderView.Stretch)  # Maksymalna szerokość nagłówków

        main_layout.addWidget(table_group)

        # Grupa dla formularza
        form_group = QGroupBox("Formularz")
        form_group_layout = QVBoxLayout(form_group)

        # Odstęp od góry tekstu "Formularz"
        form_group_layout.setContentsMargins(0, 10, 0, 0)

        form_layout = QFormLayout()

        self.index_edit = QLineEdit(self)
        form_layout.addRow("INDEX:", self.index_edit)

        self.ean_edit = QLineEdit(self)
        form_layout.addRow("EAN:", self.ean_edit)

        self.name_edit = QLineEdit(self)
        form_layout.addRow("Nazwa:", self.name_edit)

        self.description_edit = QLineEdit(self)
        form_layout.addRow("Opis:", self.description_edit)

        self.gross_price_edit = QLineEdit(self)
        self.gross_price_edit.textChanged.connect(self.update_net_price_edit)
        form_layout.addRow("Cena Brutto:", self.gross_price_edit)

        self.vat_rate_edit = QLineEdit(self)
        form_layout.addRow("VAT (%):", self.vat_rate_edit)

        self.net_price_edit = QLineEdit(self)
        self.net_price_edit.textChanged.connect(self.update_gross_price_edit)
        form_layout.addRow("Cena Netto:", self.net_price_edit)

        self.quantity_edit = QLineEdit(self)
        form_layout.addRow("Ilość:", self.quantity_edit)

        # Przycisk Dodaj pod formularzem
        self.add_button = QPushButton("Dodaj", self)
        self.add_button.clicked.connect(self.add_product)
        form_layout.addRow(self.add_button)

        # Pole do wyszukiwania produktu po nazwie, indeksie i EANie
        self.search_edit = QLineEdit(self)
        self.search_edit.setPlaceholderText("Wyszukaj produkt po nazwie, indeksie lub EAN")
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
                padding: 20px;  /* Zwiększenie wysokości rubryki */
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
                padding: 12px;  /* Zwiększenie paddingu */
            }
        """)

    def clear_form(self):
        self.index_edit.clear()
        self.ean_edit.clear()
        self.name_edit.clear()
        self.description_edit.clear()
        self.gross_price_edit.clear()
        self.vat_rate_edit.clear()
        self.net_price_edit.clear()
        self.quantity_edit.clear()

    def update_gross_price_edit(self):
        try:
            net_price = float(self.net_price_edit.text())
            vat_rate = float(self.vat_rate_edit.text())
            gross_price = net_price * (1 + vat_rate / 100)
            self.gross_price_edit.setText(f"{gross_price:.2f}")
        except ValueError:
            self.gross_price_edit.clear()

    def update_net_price_edit(self):
        try:
            gross_price = float(self.gross_price_edit.text())
            vat_rate = float(self.vat_rate_edit.text())
            net_price = gross_price / (1 + vat_rate / 100)
            self.net_price_edit.setText(f"{net_price:.2f}")
        except ValueError:
            self.net_price_edit.clear()

    def add_product(self):
        index = self.index_edit.text()
        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        gross_price = self.gross_price_edit.text()
        quantity = self.quantity_edit.text()

        try:
            index = int(index)
            net_price = float(net_price)
            vat_rate = float(vat_rate)
            gross_price = float(gross_price)
            quantity = int(quantity)

            product = Product(index, ean, name, description, net_price, vat_rate, gross_price, quantity)

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(str(product.index)))
            self.table.setItem(row_position, 1, QTableWidgetItem(product.ean))
            self.table.setItem(row_position, 2, QTableWidgetItem(product.name))
            self.table.setItem(row_position, 3, QTableWidgetItem(product.description))
            self.table.setItem(row_position, 4, QTableWidgetItem(f"{product.gross_price:.2f}"))
            self.table.setItem(row_position, 5, QTableWidgetItem(f"{product.vat_rate:.2f}"))
            self.table.setItem(row_position, 6, QTableWidgetItem(f"{product.net_price:.2f}"))
            self.table.setItem(row_position, 7, QTableWidgetItem(str(product.quantity)))

            remove_button = QPushButton("Usuń", self)
            remove_button.clicked.connect(lambda _, row=row_position: self.remove_product_row(row))
            remove_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 14px; border: 2px solid #e74c3c; border-radius: 8px; padding: 12px;")
            self.table.setCellWidget(row_position, 8, remove_button)

            # Zwiększenie wysokości rubryki o 20 pikseli
            self.table.setRowHeight(row_position, self.table.rowHeight(row_position) + 20)

            self.clear_form()

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Niepoprawne wartości liczbowe!")

    def search_products(self):
        search_text = self.search_edit.text().lower()

        for row in range(self.table.rowCount()):
            index_item = self.table.item(row, 0)
            ean_item = self.table.item(row, 1)
            name_item = self.table.item(row, 2)
            if (
                search_text in str(index_item.text()) or
                search_text in ean_item.text().lower() or
                search_text in name_item.text().lower()
            ):
                self.table.setRowHidden(row, False)
            else:
                self.table.setRowHidden(row, True)

    def remove_product_row(self, row):
        confirmation = QMessageBox.question(self, "Potwierdzenie", "Czy na pewno chcesz usunąć ten produkt?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            # Zmniejszenie wysokości rubryki o 20 pikseli
            self.table.setRowHeight(row, self.table.rowHeight(row) - 20)
            self.table.removeRow(row)
            self.clear_form()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseWindow()
    window.show()
    sys.exit(app.exec_())






























