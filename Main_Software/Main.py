import sys
from PyQt6.QtWidgets import QApplication

from PyQt6 import QtCore, QtGui, QtWidgets
from loginUI import Ui_Login
from ManagementSystem import ManagementSystem
from Font_installer import FontInstaller
import icons_rc
# from UploadToDropbox import DropboxSync

app = QApplication(sys.argv)

class LoginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.loginbtnClick)
        self.traders = None
        custom_font_path = ".\Main_Software\Fonts\RussoOne-Regular.ttf"
        custom_font_id = QtGui.QFontDatabase.addApplicationFont(custom_font_path)
        if custom_font_id != -1:
            # print("yes working font")
            custom_font_family = QtGui.QFontDatabase.applicationFontFamilies(custom_font_id)[0]
        else:
            # Handle font loading error
            # print("Error loading font")
            custom_font_family = "Russo One"
        # fontins = FontInstaller()
        # fontins.install_font_from_file("./Main_Software/Fonts/RussoOne-Regular.ttf")
    def loginbtnClick(self):
        if self.ui.loginsucess == 1:
            self.close()
            self.traders = ManagementSystem()
            # self.traders
            self.traders.show()
            def view_login():
                self.traders.close()
                login_dialog.show()
            self.traders.login_btn.clicked.connect(view_login)
                # self.traders.close()
                # self.show()

login_dialog = LoginDialog()
login_dialog.show()

# traders = ManagementSystem()

sys.exit(app.exec())
