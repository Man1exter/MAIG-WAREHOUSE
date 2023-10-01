from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import subprocess

class CentralWindowMain(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        screen_resolution = QtWidgets.QDesktopWidget().screenGeometry()
        width, height = screen_resolution.width() * 1.0, screen_resolution.height() * 0.98
        self.setGeometry(0, 0, width, height)
        
        self.setWindowTitle("MAIG WAREHOUSE APPLICATION v1.0.1")
        
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        if not self.isMaximized():
          self.showMaximized()
        
        pixmap = QtGui.QPixmap(r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\JPEGEIMAGE\New-World-niszczy-GPU.jpg")
        pixmap = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.Window, QtGui.QBrush(pixmap))
        self.setPalette(palette)
        
        navigation_layout = QHBoxLayout()
        button_labels = ['Wystaw Dokument', 'Przegląd Dokumentów', 'Zakupy i Koszty', 'Przegląd Towarów', 'Klienci', 'Reklamacje', 'Raporty i Statystyki', 'Trend i Sezonowość', 'Ustawienia Programu', 'Pomoc']
        
        for label in button_labels:
            button = QPushButton(label)
            button.setCursor(QtCore.Qt.PointingHandCursor)
            navigation_layout.addWidget(button)
            button.setStyleSheet("color: white; font-weight: bold; font-size: 18px; background-color: red; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
            
        navigation_layout.setAlignment(QtCore.Qt.AlignTop)
        
        logout_button = QPushButton('Wyloguj Się')
        logout_button.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: yellow; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
        logout_button.setCursor(QtCore.Qt.PointingHandCursor)
        logout_button.clicked.connect(self.logout_click)
        
        user_button = QPushButton('Zalogowany użytkownik: Mariusz 👤')
        user_button.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: yellow; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
        user_button.setCursor(QtCore.Qt.PointingHandCursor)
        
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(user_button)
        bottom_layout.addStretch()
        bottom_layout.addWidget(logout_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(navigation_layout)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)
        
    def logout_click(self):
        confirmation = QMessageBox(self)
        confirmation.setWindowTitle('Potwierdzenie')
        confirmation.setIcon(QMessageBox.Question)
        confirmation.setText('Czy na pewno chcesz się wylogować?')

        yes_button = confirmation.addButton('Tak', QMessageBox.YesRole)
        yes_button.setStyleSheet("background-color: green; color: white; font-weight: bold; font-size: 16px;")

        no_button = confirmation.addButton('Nie', QMessageBox.NoRole)
        no_button.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 16px;")

        confirmation.exec_()

        if confirmation.clickedButton() == yes_button:
            self.start_new_program()

    def start_new_program(self):
        try:
            subprocess.Popen(["python", r"C:\Users\mperz\Desktop\MAIG WAREHOUSE\PROJECT-CODE\main.py"])
            self.close()
        except Exception as e:
            print(f"Error starting new program: {e}")
  
    def issue_docs(self):
        pass
        
    def show_docs(self):
        pass
      
    def purchases_costs(self):
        pass
      
    def goods_review(self):
        pass
      
    def clients(self):
        pass
      
    def complain_goods(self):
        pass
    
    def reports_stats(self):
        pass
      
    def trends(self):
        pass
      
    def settings(self):
        pass
    
    def help_move(self):
        pass
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CentralWindowMain()
    window.show()
    sys.exit(app.exec_())
            