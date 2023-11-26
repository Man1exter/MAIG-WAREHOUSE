import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QFormLayout, QLabel, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QWidget, QDesktopWidget, QMessageBox
)
from PyQt5.QtGui import QPixmap, QFont

class Product:
    def __init__(self, ean, name, description, net_price, gross_price, vat_rate, manufacturer, quantity):
        self.ean = ean
        self.name = name
        self.description = description
        self.net_price = net_price
        self.gross_price = gross_price
        self.vat_rate = vat_rate
        self.manufacturer = manufacturer
        self.quantity = quantity

class WarehouseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Towary w Magazynie")

        # Ustawienie rozmiaru okna na całą dostępną przestrzeń monitora
        screen_size = QDesktopWidget().availableGeometry()
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())

        # Dodanie obrazu jako tła
        background_label = QLabel(self)
        pixmap = QPixmap("C:/Users/mperz/Desktop/MAIG WAREHOUSE/PROJECT-CODE/main.png")
        background_label.setPixmap(pixmap.scaled(screen_size.width(), screen_size.height()))
        background_label.setGeometry(0, 0, screen_size.width(), screen_size.height())

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["EAN", "Nazwa", "Opis", "Cena Netto", "Cena Brutto", "Stawka VAT", "Producent", "Ilość"])
        self.layout.addWidget(self.table)

        self.button_add = QPushButton("Dodaj Produkt")
        self.button_add.clicked.connect(self.add_product)
        self.layout.addWidget(self.button_add)

    def add_product(self):
        dialog = AddProductDialog(self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            product = dialog.get_product()
            if product:
                self.add_to_table(product)

    def add_to_table(self, product):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(product.ean))
        self.table.setItem(row_position, 1, QTableWidgetItem(product.name))
        self.table.setItem(row_position, 2, QTableWidgetItem(product.description))
        self.table.setItem(row_position, 3, QTableWidgetItem(str(product.net_price)))
        self.table.setItem(row_position, 4, QTableWidgetItem(str(product.gross_price)))
        self.table.setItem(row_position, 5, QTableWidgetItem(str(product.vat_rate)))
        self.table.setItem(row_position, 6, QTableWidgetItem(product.manufacturer))
        self.table.setItem(row_position, 7, QTableWidgetItem(str(product.quantity)))

class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dodaj Produkt")

        self.setStyleSheet("background-color: lightblue;")

        self.layout = QFormLayout()

        self.ean_edit = QLineEdit(self)
        self.layout.addRow(QLabel("EAN:"), self.ean_edit)

        self.name_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Nazwa:"), self.name_edit)

        self.description_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Opis:"), self.description_edit)

        self.net_price_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Cena Netto:"), self.net_price_edit)

        self.gross_price_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Cena Brutto:"), self.gross_price_edit)

        self.vat_rate_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Stawka VAT:"), self.vat_rate_edit)

        self.manufacturer_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Producent:"), self.manufacturer_edit)

        self.quantity_edit = QLineEdit(self)
        self.layout.addRow(QLabel("Ilość:"), self.quantity_edit)

        self.button_add = QPushButton("Dodaj")
        self.button_add.clicked.connect(self.accept)
        self.layout.addWidget(self.button_add)

        self.setLayout(self.layout)

    def get_product(self):
        ean = self.ean_edit.text()
        name = self.name_edit.text()
        description = self.description_edit.text()
        net_price = self.net_price_edit.text()
        gross_price = self.gross_price_edit.text()
        vat_rate = self.vat_rate_edit.text()
        manufacturer = self.manufacturer_edit.text()
        quantity = self.quantity_edit.text()

        if not all([ean, name, description, net_price, gross_price, vat_rate, manufacturer, quantity]):
            QMessageBox.warning(self, "Błąd", "Wypełnij wszystkie pola!")
            return None

        try:
            net_price = float(net_price)
            gross_price = float(gross_price)
            vat_rate = float(vat_rate)
            quantity = int(quantity)
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Niepoprawne wartości liczbowe!")
            return None

        return Product(ean, name, description, net_price, gross_price, vat_rate, manufacturer, quantity)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseWindow()
    window.show()
    sys.exit(app.exec_())




