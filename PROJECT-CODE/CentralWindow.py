from PyQt5 import QtWidgets, QtGui, QtCore
from settings import SetUserSpace
from helpBarSection import HelpWindow
from settoptionspy import OknoUstawien
from seasonoftrends import TrendSeasonalityWindow
import sys
import subprocess

class CentralWindowMain(QtWidgets.QDialog):
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
        
        navigation_layout = QtWidgets.QHBoxLayout()
        button_labels = ['Wystaw Dokument', 'Przegląd Dokumentów', 'Zakupy i Koszty', 'Przegląd Towarów', 'Klienci', 'Reklamacje', 'Raporty i Statystyki', 'Trend i Sezonowość', 'Ustawienia Programu', 'Pomoc']
        
        for label in button_labels:
            button = QtWidgets.QPushButton(label)
            button.setCursor(QtCore.Qt.PointingHandCursor)
            navigation_layout.addWidget(button)
            button.setStyleSheet("color: white; font-weight: bold; font-size: 18px; background-color: red; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
            
            if label == 'Pomoc':
                button.clicked.connect(self.help_move)
                
            elif label == 'Ustawienia Programu':
                button.clicked.connect(self.settings)
                
            elif label == 'Trend i Sezonowość':
                button.clicked.connect(self.trends)
        
        help_button = QtWidgets.QPushButton('Pomoc')
        help_button.setStyleSheet("color: white; font-weight: bold; font-size: 18px; background-color: green; "
                                  "border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
        help_button.setCursor(QtCore.Qt.PointingHandCursor)
        help_button.clicked.connect(self.on_help_button_clicked)  # Połącz przycisk z funkcją on_help_button_clicked
        
        add_button = QtWidgets.QPushButton('Dodaj nowe zadanie')
        edit_button = QtWidgets.QPushButton('Edytuj zadanie')
        delete_button = QtWidgets.QPushButton('Usuń zadanie')
        
        button_style = (
            "color: white; font-weight: bold; font-size: 16px; background-color: blue; border: 2px solid black; "
            "border-radius: 5px; margin: 10px; padding: 10px; width: 50%;"
        )
        
        add_button.setStyleSheet(button_style + "background-color: rgba(0, 0, 255, 0.5);")  # Dodanie przezroczystości
        edit_button.setStyleSheet(button_style + "background-color: rgba(0, 0, 255, 0.5);")
        delete_button.setStyleSheet(button_style + "background-color: rgba(0, 0, 255, 0.5);")
        
        add_button.setCursor(QtCore.Qt.PointingHandCursor)
        edit_button.setCursor(QtCore.Qt.PointingHandCursor)
        delete_button.setCursor(QtCore.Qt.PointingHandCursor)
        
        add_button.clicked.connect(self.add_task)
        edit_button.clicked.connect(self.edit_task)
        delete_button.clicked.connect(self.delete_task)
        
        self.todo_listwidget = QtWidgets.QListWidget()
        self.todo_listwidget.setStyleSheet(
            "font-weight: bold; font-size: 25px; background-color: rgba(173, 216, 230, 0.5); border: 2px solid black; border-radius: 5px; margin: 0px; padding: 10px; spacing: 10px; height: 50%;"
        )
        self.todo_listwidget.setContentsMargins(30, 30, 30, 30)
        
        self.todo_listwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.todo_listwidget.customContextMenuRequested.connect(self.show_context_menu)
        self.context_menu = QtWidgets.QMenu(self)
        delete_action = QtWidgets.QAction('Usuń', self)
        delete_action.triggered.connect(self.delete_task)
        self.context_menu.addAction(delete_action)
        
        employee_button = QtWidgets.QPushButton("JASNOŚĆ", self)
        employee_button.setStyleSheet("background-color: yellow; color: black; font-weight: bold; font-size: 16px; border: 2px solid black; border-radius: 3px; padding: 10px;")
        employee_button.setCursor(QtCore.Qt.PointingHandCursor)
        employee_button.clicked.connect(self.employee)
        
        logout_button = QtWidgets.QPushButton('Wyloguj Się 👤')
        logout_button.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: yellow; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
        logout_button.setCursor(QtCore.Qt.PointingHandCursor)
        logout_button.clicked.connect(self.logout_click)
        
        user_button = QtWidgets.QPushButton('Zalogowany użytkownik: Mariusz 👤')
        user_button.setStyleSheet("color: black; font-weight: bold; font-size: 18px; background-color: yellow; border: 2px solid black; border-radius: 3px; font-family: Arial; margin: 10px; padding: 5px;")
        user_button.setCursor(QtCore.Qt.PointingHandCursor)
        
        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)
        
        squares_layout = QtWidgets.QVBoxLayout()
        squares_layout.addWidget(self.todo_listwidget)
        squares_layout.addLayout(buttons_layout)
        
        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addWidget(user_button)
        bottom_layout.addStretch()
        bottom_layout.addWidget(logout_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(navigation_layout)
        main_layout.addLayout(squares_layout)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)
        
    def logout_click(self):
        confirmation = QtWidgets.QMessageBox(self)
        confirmation.setWindowTitle('Potwierdzenie')
        confirmation.setIcon(QtWidgets.QMessageBox.Question)
        confirmation.setText('Czy na pewno chcesz się wylogować?')

        yes_button = confirmation.addButton('Tak', QtWidgets.QMessageBox.YesRole)
        yes_button.setStyleSheet("background-color: green; color: white; font-weight: bold; font-size: 16px;")

        no_button = confirmation.addButton('Nie', QtWidgets.QMessageBox.NoRole)
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
            
    def add_task(self):
        task, ok = QtWidgets.QInputDialog.getText(self, 'Dodaj nowe zadanie', 'Wprowadź nowe zadanie:')
        if ok:
            self.todo_listwidget.addItem(task)

    def edit_task(self):
        current_item = self.todo_listwidget.currentItem()
        if current_item:
            new_task, ok = QtWidgets.QInputDialog.getText(self, 'Edytuj zadanie', 'Edytuj zadanie:', text=current_item.text())
            if ok:
                current_item.setText(new_task)

    def show_context_menu(self, position):
        item = self.todo_listwidget.itemAt(position)
        if item:
            self.context_menu.exec_(self.todo_listwidget.mapToGlobal(position))

    def delete_task(self):
        current_item = self.todo_listwidget.currentItem()
        if current_item:
            self.todo_listwidget.takeItem(self.todo_listwidget.row(current_item))
  
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
        sett_season_window = TrendSeasonalityWindow()
        sett_season_window.exec_()
    
    def on_sett_button_clicked(self):
        if self.sender().text() == 'Ustawienia Programu':
            self.settings()
      
    def settings(self):
        sett_window = OknoUstawien()
        sett_window.exec_()
    
    def on_help_button_clicked(self):
        if self.sender().text() == 'Pomoc':
            self.help_move()
    
    def help_move(self):
        help_window = HelpWindow(self)
        help_window.exec_()
    
    def employee(self):
        user_space_dialog = SetUserSpace(self)
        user_space_dialog.exec_()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CentralWindowMain()
    window.show()
    sys.exit(app.exec_())




       
