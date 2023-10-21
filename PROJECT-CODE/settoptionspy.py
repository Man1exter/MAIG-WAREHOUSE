from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class CenteredComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        option = QtWidgets.QStyleOptionComboBox()
        option.initFrom(self)
        self.initStyleOption(option)
        painter = QtGui.QPainter(self)
        self.style().drawComplexControl(QtWidgets.QStyle.CC_ComboBox, option, painter, self)
        text_rect = self.style().subControlRect(QtWidgets.QStyle.CC_ComboBox, option, QtWidgets.QStyle.SC_ComboBoxEditField, self)
        painter.drawText(text_rect, QtCore.Qt.AlignCenter, self.currentText())

class OknoUstawien(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ustawienia Programu")
        self.setGeometry(0, 0, 500, 300)
        self.center()

        # Ustawienie tła
        palette = QtGui.QPalette()
        background_image = QtGui.QImage("C:/Users/mperz/Desktop/MAIG WAREHOUSE/JPEGEIMAGE/New-World-niszczy-GPU.jpg")
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background_image))
        self.setPalette(palette)

        self.label1 = QtWidgets.QLabel("Autozapis:")
        self.label1.setStyleSheet("font-size: 17px; font-weight: bold; color: red;")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.combo_box1 = CenteredComboBox()
        self.combo_box1.addItems(["Tak", "Nie"])
        self.combo_box1.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.label2 = QtWidgets.QLabel("Możliwość płatności przelewowych termin:")
        self.label2.setStyleSheet("font-size: 17px; font-weight: bold; color: red;")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)

        self.combo_box2 = CenteredComboBox()
        self.combo_box2.addItems(["30 dni", "45 dni", "90 dni"])
        self.combo_box2.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.label3 = QtWidgets.QLabel("Powiadomienia:")
        self.label3.setStyleSheet("font-size: 17px; font-weight: bold; color: red;")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)

        self.combo_box3 = CenteredComboBox()
        self.combo_box3.addItems(["Wyłącz", "Włącz", "Raz w miesiącu raport"])
        self.combo_box3.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.save_button = QtWidgets.QPushButton("Zapisz Ustawienia")
        self.save_button.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #4CAF50; color: white;")
        self.save_button.clicked.connect(self.zapisz_ustawienia)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.combo_box1)
        layout.addWidget(self.label2)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.label3)
        layout.addWidget(self.combo_box3)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def zapisz_ustawienia(self):
        ustawienie1 = self.combo_box1.currentText()
        ustawienie2 = self.combo_box2.currentText()
        ustawienie3 = self.combo_box3.currentText()

        QtWidgets.QMessageBox.information(self, "Zapisano Ustawienia", "Ustawienia zostały zapisane.")
        self.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    okno_ustawien = OknoUstawien()
    okno_ustawien.exec_()













