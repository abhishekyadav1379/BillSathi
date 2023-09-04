import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input Dialog")
        
        self.nameLineEdit = QLineEdit(self)
        self.addressLineEdit = QLineEdit(self)
        self.phoneLineEdit = QLineEdit(self)
        
        self.submitButton = QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.accept)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Id"))
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.nameLineEdit)
        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.addressLineEdit)
        layout.addWidget(QLabel("Phone number:"))
        layout.addWidget(self.phoneLineEdit)
        layout.addWidget(self.submitButton)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Example")
        
        self.button = QPushButton("Open Input Dialog", self)
        self.button.setGeometry(50, 50, 200, 30)
        self.button.clicked.connect(self.showInputDialog)
    
    def showInputDialog(self):
        dialog = InputDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name = dialog.nameLineEdit.text()
            Address = dialog.addressLineEdit.text()
            phone_number = dialog.phoneLineEdit.text()
            print("Name:", name)
            print("Email:", Address)
            print("Phone number:", phone_number)
            return [name,Address,phone_number]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(300, 300, 300, 150)
    window.show()
    sys.exit(app.exec())
