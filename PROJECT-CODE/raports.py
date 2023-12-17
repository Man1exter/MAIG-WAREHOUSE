import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,
    QTableWidget, QTableWidgetItem, QFormLayout, QComboBox, QDateEdit,
    QMessageBox, QHeaderView
)
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import QDate

import matplotlib.pyplot as plt

class WarehouseReportsPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Raportów Magazynowych")
        self.setGeometry(100, 100, 1000, 600)  # Increased window width

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        # Stylizacja arkusza
        style_sheet = """
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QTableWidget {
                font-size: 14px;
                alternate-background-color: #f0f0f0;
            }
            QComboBox, QDateEdit {
                font-size: 14px;
            }
        """
        self.setStyleSheet(style_sheet)

        # Przykładowe dane do DataFrame
        self.df = self.generate_sample_data()

        # Widgety
        self.report_type_label = QLabel("Typ Raportu:", self)
        self.report_type_combobox = QComboBox(self)
        self.report_type_combobox.addItems([
            "Raport Dostaw", "Raport Wydań", "Raport Stanu Magazynowego",
            "Raport Sprzedaży", "Raport Wzrostu w Procentach", "Raport Wzrostu Cen w Procentach"
        ])
        self.report_type_combobox.currentIndexChanged.connect(self.update_sample_data)

        self.date_label = QLabel("Data:", self)
        self.date_edit = QDateEdit(QDate.currentDate(), self)
        self.date_edit.dateChanged.connect(self.update_sample_data)

        self.generate_report_button = QPushButton("Generuj Raport", self)
        self.generate_report_button.clicked.connect(self.show_report_dialog)

        self.table_widget = QTableWidget(self)
        self.update_table()

        plot_button = QPushButton("Generuj Wykres Kolumnowy", self)
        plot_button.clicked.connect(self.generate_column_chart)

        sales_report_button = QPushButton("Generuj Raport Sprzedaży", self)
        sales_report_button.clicked.connect(self.generate_sales_report)

        # Układ
        form_layout = QFormLayout()
        form_layout.addRow(self.report_type_label, self.report_type_combobox)
        form_layout.addRow(self.date_label, self.date_edit)
        form_layout.addRow(self.generate_report_button)
        form_layout.addRow(plot_button)
        form_layout.addRow(sales_report_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table_widget)

        self.central_widget.setLayout(main_layout)

    def generate_sample_data(self):
        data = np.random.randint(0, 100, size=(10, 8))
        columns = ['Produkt', 'Ilość', 'Wartość', 'Nazwa', 'EAN', 'Cena Netto', 'Cena Brutto', 'Rentowność']
        sample_data = pd.DataFrame(data, columns=columns)
        sample_data['Rentowność'] = np.round((sample_data['Cena Brutto'] - sample_data['Cena Netto']) / sample_data['Cena Netto'] * 100, 1)
        sample_data['Średnia Cena'] = np.round(np.random.uniform(10, 50, size=(10)), 2)
        sample_data['Średnia Ilość na Zamówienie'] = sample_data['Ilość'].mean()
        return sample_data

    def update_table(self, data=None):
        if data is None:
            data = self.df

        self.table_widget.clear()
        self.table_widget.setColumnCount(len(data.columns) + 4)
        self.table_widget.setRowCount(len(data))
        self.table_widget.setHorizontalHeaderLabels(
            ['Produkt', 'Ilość', 'Wartość', 'Nazwa', 'EAN', 'Cena Netto', 'Cena Brutto', 'Rentownosc', 'Średnia Cena',
             'Średnia Ilość na Zamówienie', 'Wartość Netto', 'Wartość Brutto', 'Suma Netto', 'Suma Brutto'])

        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                item = QTableWidgetItem(str(data.iloc[i, j]))

                # Zaznacz rentowność na czerwono, jeśli jest ujemna
                if data.columns[j] == 'Rentownosc' and data.iloc[i, j] < 0:
                    item.setBackground(QBrush(QColor(255, 0, 0)))  # Czerwony kolor tła

                self.table_widget.setItem(i, j, item)

            # Dodaj kolumny z przeliczonymi kwotami netto i brutto oraz sumą netto i brutto
            netto_column = data.columns.get_loc('Cena Netto') if 'Cena Netto' in data.columns else -1
            brutto_column = data.columns.get_loc('Cena Brutto') if 'Cena Brutto' in data.columns else -1
            ilosc_column = data.columns.get_loc('Ilość') if 'Ilość' in data.columns else -1

            self.table_widget.setItem(i, len(data.columns), QTableWidgetItem(str(data.iloc[i, netto_column] * data.iloc[i, ilosc_column])))
            self.table_widget.setItem(i, len(data.columns) + 1, QTableWidgetItem(str(data.iloc[i, brutto_column] * data.iloc[i, ilosc_column])))
            self.table_widget.setItem(i, len(data.columns) + 2, QTableWidgetItem(str(data.iloc[:i + 1, netto_column].sum())))
            self.table_widget.setItem(i, len(data.columns) + 3, QTableWidgetItem(str(data.iloc[:i + 1, brutto_column].sum())))

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def update_sample_data(self):
        self.df = self.generate_sample_data()
        self.update_table()

    def show_report_dialog(self):
        report_type = self.report_type_combobox.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        msg = self.generate_report(report_type, date)

        if report_type == "Raport Sprzedaży":
            sales_data = self.generate_sales_data()
            self.update_table(sales_data)
        elif report_type == "Raport Wzrostu w Procentach":
            growth_data = self.generate_growth_data()
            self.update_table(growth_data)
        elif report_type == "Raport Wzrostu Cen w Procentach":
            price_growth_data = self.generate_price_growth_data()
            self.update_table(price_growth_data)
        else:
            self.update_table()

        QMessageBox.information(self, f"Generowanie Raportu ({report_type})", msg)

    def generate_report(self, report_type, date):
        if report_type == "Raport Dostaw":
            return f"Generuję raport dostaw na dzień {date}"
        elif report_type == "Raport Wydań":
            return f"Generuję raport wydań na dzień {date}"
        elif report_type == "Raport Stanu Magazynowego":
            return f"Generuję raport stanu magazynowego na dzień {date}"
        elif report_type == "Raport Sprzedaży":
            return f"Generuję raport sprzedaży na dzień {date}"
        elif report_type == "Raport Wzrostu w Procentach":
            return f"Generuję raport wzrostu w procentach na dzień {date}"
        elif report_type == "Raport Wzrostu Cen w Procentach":
            return f"Generuję raport wzrostu cen w procentach na dzień {date}"

    def generate_sales_data(self):
        sales_data = np.random.randint(0, 50, size=(10, 8))
        sales_df = pd.DataFrame(
            sales_data,
            columns=['Produkt', 'Ilość Sprzedana', 'Wartość', 'Nazwa', 'EAN', 'Cena Netto', 'Cena Brutto', 'Rentowność']
        )
        sales_df['Rentowność'] = np.round(
            (sales_df['Cena Brutto'] - sales_df['Cena Netto']) / sales_df['Cena Netto'] * 100, 1
        )
        sales_df['Średnia Cena'] = np.round(np.random.uniform(10, 50, size=(10)), 2)
        sales_df['Średnia Ilość na Zamówienie'] = sales_df['Ilość Sprzedana'].mean()
        return sales_df

    def generate_growth_data(self):
        growth_data = np.random.uniform(0.1, 0.5, size=(10, 3))
        return pd.DataFrame(growth_data, columns=['Produkt', 'Wzrost Ilości', 'Wzrost Wartości'])

    def generate_price_growth_data(self):
        price_growth_data = np.random.uniform(0.1, 0.5, size=(10, 3))
        price_growth_data = pd.DataFrame(price_growth_data, columns=['Produkt', 'Wzrost Cena Netto', 'Wzrost Cena Brutto'])
        price_growth_data['Cena Netto'] = np.random.uniform(10, 50, size=(10))
        price_growth_data['Cena Brutto'] = price_growth_data['Cena Netto'] * (1 + price_growth_data['Wzrost Cena Brutto'])
        return price_growth_data

    def generate_column_chart(self):
        plt.bar(self.df['Produkt'], self.df['Ilość'])
        plt.xlabel('Produkt')
        plt.ylabel('Ilość')
        plt.title('Wykres Kolumnowy')
        plt.show()

    def generate_sales_report(self):
        sales_data = self.generate_sales_data()
        plt.bar(sales_data['Produkt'], sales_data['Ilość Sprzedana'])
        plt.xlabel('Produkt')
        plt.ylabel('Ilość Sprzedana')
        plt.title('Raport Sprzedaży - Wykres Kolumnowy')
        plt.show()
        msg = "Raport Sprzedaży:\n\n" + str(sales_data)
        QMessageBox.information(self, "Raport Sprzedaży", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseReportsPanel()
    window.show()
    sys.exit(app.exec_())












