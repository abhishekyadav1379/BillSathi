from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox, QApplication
from PyQt6.QtCore import QTimer
import sys

class DialogBox():
    @staticmethod
    def show_yes_no_dialog(message):
        reply = QMessageBox.question(
            None,
            "Yes/No Dialog",
            message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            print("You clicked Yes")
            return True
        else:
            print("You clicked No")
            return False

    @staticmethod
    def show_warning_dialog(message):
        QMessageBox.warning(None, "Warning Dialog", message)

    @staticmethod
    def show_information_dialog(message):
        QMessageBox.information(None, "Information Dialog", message)