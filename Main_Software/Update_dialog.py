import shutil
import zipfile
import os,sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QProgressBar
import pretty_errors
from PyQt6 import QtCore, QtGui, QtWidgets, QtMultimedia
from All_function import all_function
import icons_rc

class Loading(QThread):
    send_signal = pyqtSignal(list)
    
    
    def __init__(self):
        super().__init__()
        self.fn = all_function()
        
    def run(self):
        self.url = self.fn.select_mysql_db("select value from settings where type = 'download_url'")[0][0]
        version = self.fn.select_mysql_db("select value from settings where type = 'version'")[0][0]
        file_size = self.fn.get_file_size(self.url)
        self.send_signal.emit([version, file_size])

class Ui_Update_dialog(object):
    def setupUi(self, Update_dialog):
        Update_dialog.setObjectName("Update_dialog")
        Update_dialog.resize(234, 228)
        Update_dialog.setStyleSheet("QDialog{\n"
"background-color: white;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Update_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Update_dialog)
        self.label.setMaximumSize(QtCore.QSize(100, 100))

        # Create a QMovie object to display the GIF
        self.movie = QtGui.QMovie(":/icons/work-in-progress.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(parent=Update_dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Update_dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.retranslateUi(Update_dialog)
        QtCore.QMetaObject.connectSlotsByName(Update_dialog)

    def retranslateUi(self, Update_dialog):
        _translate = QtCore.QCoreApplication.translate
        Update_dialog.setWindowTitle(_translate("Update_dialog", "Updater"))
        self.pushButton.setText(_translate("Update_dialog", "Download"))
        self.label_2.setText(_translate("Update_dialog", "Please wait..."))
        
        
################# Main ################
        self.file_info_thread = Loading()
        self.file_info_thread.send_signal.connect(self.update)
        self.file_info_thread.start()
        
    
    def update(self, progress):
        text = f"BillSathi \nversion: {progress[0]} \nUpdate size: {progress[1]} MB"
        self.label_2.setText(text)
        self.label.setPixmap(QtGui.QPixmap(":/icons/compony_logo.png"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_dialog = QtWidgets.QDialog()
    ui = Ui_Update_dialog()
    ui.setupUi(Update_dialog)
    Update_dialog.show()
    sys.exit(app.exec())
