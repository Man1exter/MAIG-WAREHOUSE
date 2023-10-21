import random
import requests
from PyQt5 import QtWidgets, QtGui, QtCore

class TrendSeasonalityWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trend i Sezonowość")
        self.setFixedSize(800, 600)

        # Centrowanie okna na ekranie
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.rect().center())

        # Kolor tła
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(240, 240, 240))  # Jasnoszare tło
        self.setPalette(palette)

        self.trend_label = QtWidgets.QLabel("Aktualny Trend - Top 10 Produktów:")
        self.trend_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")

        self.trend_text = QtWidgets.QTextEdit()
        self.trend_text.setReadOnly(True)
        self.trend_text.setStyleSheet("font-size: 16px; background-color: white; color: #333;")

        self.seasonality_label = QtWidgets.QLabel("Sezonowość - Okres czasu:")
        self.seasonality_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")

        self.seasonality_text = QtWidgets.QTextEdit()
        self.seasonality_text.setReadOnly(True)
        self.seasonality_text.setStyleSheet("font-size: 16px; background-color: white; color: #333;")

        self.fetch_data_button = QtWidgets.QPushButton("Pobierz Dane")
        self.fetch_data_button.setStyleSheet(
            "font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; padding: 10px 20px;")

        # Efekt zaokrąglenia przycisku
        self.fetch_data_button.setStyleSheet("border-radius: 5px;")

        # Efekt cienia pod przyciskiem
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(2)
        shadow.setYOffset(2)
        shadow.setColor(QtGui.QColor(50, 50, 50, 100))
        self.fetch_data_button.setGraphicsEffect(shadow)

        self.fetch_data_button.clicked.connect(self.fetch_data)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.trend_label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.trend_text)
        layout.addWidget(self.seasonality_label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.seasonality_text)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.fetch_data_button, alignment=QtCore.Qt.AlignCenter)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def fetch_data(self):
        try:
            trend_data = self.get_trend_data_from_api()
            seasonality_data = self.get_seasonality_data_from_api()

            self.trend_text.setPlainText(trend_data)
            self.seasonality_text.setPlainText(seasonality_data)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Błąd Pobierania Danych", f"Wystąpił błąd podczas pobierania danych: {str(e)}")

    def get_trend_data_from_api(self):
        products = ["Krzesła", "Doniczki", "Laptopy", "Smartfony", "Telewizory", "Konsolki", "Książki", "Szklanki",
                    "Buty", "Rowery"]
        random_products = random.sample(products, 10)
        return "\n".join(random_products)

    def get_seasonality_data_from_api(self):
        import datetime
        today = datetime.date.today()
        one_year_later = today + datetime.timedelta(days=365)
        return f"Okres:     {today.strftime('%d-%m-%Y')} - {one_year_later.strftime('%d-%m-%Y')}"

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    trend_seasonality_window = TrendSeasonalityWindow()
    trend_seasonality_window.exec_()
















