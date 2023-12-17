import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QComboBox, QDateEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate

class WarehouseReportsPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Panel Raportów Magazynowych")
        self.setGeometry(100, 100, 800, 600)

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
        self.report_type_combobox.addItems(["Raport Dostaw", "Raport Wydań", "Raport Stanu Magazynowego"])

        self.date_label = QLabel("Data:", self)
        self.date_edit = QDateEdit(QDate.currentDate(), self)
        self.date_edit.dateChanged.connect(self.update_sample_data)

        self.generate_report_button = QPushButton("Generuj Raport", self)
        self.generate_report_button.clicked.connect(self.show_report_dialog)

        self.table_widget = QTableWidget(self)
        self.update_table()

        add_transaction_button = QPushButton("Dodaj Przykładową Transakcję", self)
        add_transaction_button.clicked.connect(self.add_sample_transaction)

        # Układ
        form_layout = QFormLayout()
        form_layout.addRow(self.report_type_label, self.report_type_combobox)
        form_layout.addRow(self.date_label, self.date_edit)
        form_layout.addRow(self.generate_report_button)
        form_layout.addRow(add_transaction_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table_widget)

        self.central_widget.setLayout(main_layout)

    def generate_sample_data(self):
        data = np.random.randint(0, 100, size=(10, 3))
        return pd.DataFrame(data, columns=['Produkt', 'Ilość', 'Wartość'])

    def update_table(self):
        self.table_widget.clear()
        self.table_widget.setColumnCount(len(self.df.columns))
        self.table_widget.setRowCount(len(self.df))
        self.table_widget.setHorizontalHeaderLabels(self.df.columns)

        for i in range(len(self.df.index)):
            for j in range(len(self.df.columns)):
                item = QTableWidgetItem(str(self.df.iloc[i, j]))
                self.table_widget.setItem(i, j, item)

    def update_sample_data(self):
        self.df = self.generate_sample_data()
        self.update_table()

    def add_sample_transaction(self):
        new_transaction = pd.DataFrame([[np.random.randint(0, 100), np.random.randint(1, 10), np.random.randint(10, 100)]],
                                       columns=['Produkt', 'Ilość', 'Wartość'])
        self.df = pd.concat([self.df, new_transaction], ignore_index=True)
        self.update_table()

    def show_report_dialog(self):
        # Tutaj możesz dodać logikę generowania raportu i wyświetlania wyników w oknie dialogowym
        report_type = self.report_type_combobox.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        msg = f"Generowanie raportu dla {report_type} na dzień {date}"
        QMessageBox.information(self, "Generowanie Raportu", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarehouseReportsPanel()
    window.show()
    sys.exit(app.exec_())

