from PyQt6 import QtCore, QtGui, QtWidgets
from UploadToDropbox import DropboxSync
from PyQt6.QtCore import QThread, pyqtSignal
from DialogBox_alltype import DialogBox
from All_function import all_function

class UploadThread(QThread):
    finished = pyqtSignal()

    def run(self):
        self.stop_flag = False
        fn = all_function()
        fn.copy_file(r"Main_Software\mahendra.db",r"D:")
        dropbox = DropboxSync()
        dropbox.upload_changed()
        self.finished.emit()
    
    def stop(self):
        self.stop_flag = True
        self.terminate()


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(333, 390)
        Settings.setStyleSheet("QLineEdit {\n"
"                background-color: #f3f3f3;\n"
"                border: 2px solid #c0c0c0;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                selection-background-color: #a8a8a8;\n"
"            margin-bottom: 5px;\n"
"            }\n"
"\n"
"            QLineEdit:focus {\n"
"                border: 2px solid #707070;\n"
"                background-color: #ffffff;\n"
"            }\n"
"\n"
"QLabel {\n"
"    font-family: Russo One;\n"
"    font-size: 15px;\n"
"    border : 0px;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-family: Belanosima;\n"
"    font-size: 18px;\n"
"    background-color: rgb(231, 255, 215);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Settings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=Settings)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_submit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.gridLayout.addWidget(self.pushButton_submit, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 5, 1, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 6, 0, 1, 1)
        self.pushButton_sync = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_sync.setObjectName("pushButton_sync")
        self.gridLayout.addWidget(self.pushButton_sync, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.label_7.setText(_translate("Settings", "Company Name"))
        self.label_3.setText(_translate("Settings", "Company Tag"))
        self.label.setText(_translate("Settings", "Printer"))
        self.comboBox.setItemText(0, _translate("Settings", "Samsung"))
        self.comboBox.setItemText(1, _translate("Settings", "hp"))
        self.comboBox.setItemText(2, _translate("Settings", "exnois"))
        self.label_4.setText(_translate("Settings", "Table Font Size"))
        self.label_5.setText(_translate("Settings", "Backup"))
        self.pushButton_submit.setText(_translate("Settings", "Submit"))
        self.label_6.setText(_translate("Settings", "Developer Mode"))
        self.checkBox.setText(_translate("Settings", "CheckBox"))
        self.pushButton_update.setText(_translate("Settings", "Update"))
        self.pushButton_sync.setText(_translate("Settings", "Sync"))
        self.label_2.setText(_translate("Settings", "setting currently Disable"))

################################ Main working ############################################
        self.pushButton_submit.clicked.connect(self.upload)
        
    
    def upload(self):
        # Start the upload in a separate QThread
        self.upload_thread = UploadThread()
        self.upload_thread.finished.connect(self.on_upload_finished)
        self.upload_thread.start()
    
    def on_upload_finished(self):
    # Handle any post-upload actions here
        print("finished")
        box = DialogBox()
        box.show_information_dialog("Upload Complete")
    
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Settings = QtWidgets.QDialog()
#     ui = Ui_Settings()
#     ui.setupUi(Settings)
#     Settings.show()
#     sys.exit(app.exec())
