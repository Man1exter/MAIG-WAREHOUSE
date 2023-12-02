import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QDialogButtonBox, QHeaderView
from PyQt5.QtCore import Qt, QDateTime

class FakturaWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.faktury = []

        layout = QVBoxLayout()

        self.nazwa_edit = QLineEdit(self)
        self.index_edit = QLineEdit(self)
        self.data_wystawienia_edit = QLineEdit(self)
        self.data_wpisania_edit = QLineEdit(self)
        self.firma_edit = QLineEdit(self)

        self.pozycje_table = QTableWidget(self)
        self.pozycje_table.setColumnCount(6)
        self.pozycje_table.setHorizontalHeaderLabels(["Nazwa", "Ilość", "Cena Netto", "Cena Brutto", "Stawka VAT", "Suma"])
        self.pozycje_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        dodaj_pozycje_button = QPushButton("Dodaj pozycję", self)
        dodaj_pozycje_button.clicked.connect(self.dodaj_pozycje)

        zapisz_button = QPushButton("Zapisz fakturę", self)
        zapisz_button.clicked.connect(self.zapisz_fakture)

        zapisane_faktury_button = QPushButton("Zapisane faktury zakupowe", self)
        zapisane_faktury_button.clicked.connect(self.pokaz_zapisane_faktury)

        layout.addWidget(QLabel("Nazwa Dokumentu:"))
        layout.addWidget(self.nazwa_edit)
        layout.addWidget(QLabel("Index Faktury:"))
        layout.addWidget(self.index_edit)
        layout.addWidget(QLabel("Data Wystawienia:"))
        layout.addWidget(self.data_wystawienia_edit)
        layout.addWidget(QLabel("Data Wpisania:"))
        layout.addWidget(self.data_wpisania_edit)
        layout.addWidget(QLabel("Firma:"))
        layout.addWidget(self.firma_edit)
        layout.addWidget(QLabel("Pozycje:"))
        layout.addWidget(self.pozycje_table)
        layout.addWidget(dodaj_pozycje_button)
        layout.addWidget(zapisz_button)
        layout.addWidget(zapisane_faktury_button)

        # Ustaw kolorystykę i styl
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f8f8;
                color: #333;
                font-size: 16px;
            }

            QLineEdit, QTableWidget, QDialog {
                background-color: #ffffff;
                color: #333;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #4CAF50;
                color: #fff;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.setLayout(layout)

    def dodaj_pozycje(self):
        dialog = DodajPozycjeDialog(self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            nazwa = dialog.nazwa_edit.text()
            ilosc = float(dialog.ilosc_edit.text())
            cena_netto = float(dialog.cena_netto_edit.text())
            cena_brutto = float(dialog.cena_brutto_edit.text())
            stawka_vat = float(dialog.stawka_vat_edit.text())

            suma = ilosc * cena_brutto

            row_position = self.pozycje_table.rowCount()
            self.pozycje_table.insertRow(row_position)
            self.pozycje_table.setItem(row_position, 0, QTableWidgetItem(nazwa))
            self.pozycje_table.setItem(row_position, 1, QTableWidgetItem(str(ilosc)))
            self.pozycje_table.setItem(row_position, 2, QTableWidgetItem(str(cena_netto)))
            self.pozycje_table.setItem(row_position, 3, QTableWidgetItem(str(cena_brutto)))
            self.pozycje_table.setItem(row_position, 4, QTableWidgetItem(str(stawka_vat)))
            self.pozycje_table.setItem(row_position, 5, QTableWidgetItem(str(suma)))

    def zapisz_fakture(self):
        nazwa = self.nazwa_edit.text()
        index = self.index_edit.text()
        data_wystawienia = self.data_wystawienia_edit.text()
        data_wpisania = self.data_wpisania_edit.text()
        firma = self.firma_edit.text()

        pozycje = []
        for row in range(self.pozycje_table.rowCount()):
            pozycja = {
                "nazwa": self.pozycje_table.item(row, 0).text(),
                "ilosc": float(self.pozycje_table.item(row, 1).text()),
                "cena_netto": float(self.pozycje_table.item(row, 2).text()),
                "cena_brutto": float(self.pozycje_table.item(row, 3).text()),
                "stawka_vat": float(self.pozycje_table.item(row, 4).text()),
                "suma": float(self.pozycje_table.item(row, 5).text())
            }
            pozycje.append(pozycja)

        faktura = {
            "nazwa": nazwa,
            "index": index,
            "data_wystawienia": data_wystawienia,
            "data_wpisania": data_wpisania,
            "firma": firma,
            "pozycje": pozycje,
            "timestamp": QDateTime.currentDateTime().toString(Qt.ISODate)
        }

        self.faktury.append(faktura)
        self.clear_fields()

    def pokaz_zapisane_faktury(self):
        zapisane_faktury_dialog = ZapisaneFakturyDialog(self.faktury, self)
        zapisane_faktury_dialog.exec_()

    def clear_fields(self):
        self.nazwa_edit.clear()
        self.index_edit.clear()
        self.data_wystawienia_edit.clear()
        self.data_wpisania_edit.clear()
        self.firma_edit.clear()
        self.pozycje_table.setRowCount(0)


class DodajPozycjeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QFormLayout()

        self.nazwa_edit = QLineEdit(self)
        self.ilosc_edit = QLineEdit(self)
        self.cena_netto_edit = QLineEdit(self)
        self.cena_brutto_edit = QLineEdit(self)
        self.stawka_vat_edit = QLineEdit(self)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addRow("Nazwa:", self.nazwa_edit)
        layout.addRow("Ilość:", self.ilosc_edit)
        layout.addRow("Cena Netto:", self.cena_netto_edit)
        layout.addRow("Cena Brutto:", self.cena_brutto_edit)
        layout.addRow("Stawka VAT:", self.stawka_vat_edit)
        layout.addWidget(buttons)

        self.setLayout(layout)


class ZapisaneFakturyDialog(QDialog):
    def __init__(self, faktury, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        self.faktury_list = QTableWidget(self)
        self.faktury_list.setColumnCount(4)
        self.faktury_list.setHorizontalHeaderLabels(["Nazwa", "Index", "Data Wystawienia", "Firma"])
        self.faktury_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for faktura in faktury:
            row_position = self.faktury_list.rowCount()
            self.faktury_list.insertRow(row_position)
            self.faktury_list.setItem(row_position, 0, QTableWidgetItem(faktura["nazwa"]))
            self.faktury_list.setItem(row_position, 1, QTableWidgetItem(faktura["index"]))
            self.faktury_list.setItem(row_position, 2, QTableWidgetItem(faktura["data_wystawienia"]))
            self.faktury_list.setItem(row_position, 3, QTableWidgetItem(faktura["firma"]))

        layout.addWidget(self.faktury_list)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)

        layout.addWidget(buttons)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    faktura_window = FakturaWindow()
    faktura_window.showMaximized()
    sys.exit(app.exec_())






        

