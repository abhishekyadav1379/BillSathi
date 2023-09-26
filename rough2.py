import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QLabel, QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Example")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.checkbox = QCheckBox("Check me")
        self.label = QLabel("Unchecked")

        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)

        self.checkbox.clicked.connect(self.update_label)

    def update_label(self):
        if self.checkbox.isChecked():
            self.label.setText("Checked")
        else:
            self.label.setText("Unchecked")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()