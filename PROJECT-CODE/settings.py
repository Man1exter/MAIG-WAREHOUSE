from PyQt5 import QtWidgets

class SetUserSpace(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle("Ustawienia użytkownika")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QtWidgets.QVBoxLayout()
        
        label = QtWidgets.QLabel("Tutaj możesz dostosować ustawienia użytkownika.")
        layout.addWidget(label)
        
        save_button = QtWidgets.QPushButton("Zapisz ustawienia")
        layout.addWidget(save_button)
        
        self.setLayout(layout)
    