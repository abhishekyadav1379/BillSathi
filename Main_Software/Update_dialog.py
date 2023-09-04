from PyQt6 import QtCore, QtGui, QtWidgets
from UploadToDropbox import DropboxSync
import sys,time

class DownloadThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    
    def run(self):
        self.stop_flag = False
        dropbox = DropboxSync()
        dropbox.delete_local_folder("./Main_Software/Download_files")
        dropbox.download_changed("./Main_Software/Download_files",'/Download')
        self.finished.emit()
        
    def stop(self):
        self.stop_flag = True
        self.terminate()

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)
    def __init__(self,parent=None,index = 0):
        super(ThreadClass,self).__init__(parent)
        self.index = index
        self.is_running = True
    
    def run(self):
        print('Thread started',self.index)
        cnt = 0
        cloud = DropboxSync()
        cloud.token_checker()
        dropbox_folder_size = int(cloud.get_folder_size("/Download/update_folder"))
        local_folder_size = 0
        download_flag = 0
        while int(local_folder_size) < dropbox_folder_size:
            if download_flag == 0:
                download_flag = 1
                # cloud.download_changed("./Main_Software/Download_files",'/Download')
            local_folder_size = cloud.get_local_folder_size("./Main_Software/Download_files")
            progress = int((local_folder_size / dropbox_folder_size) * 100)
            # print(progress)
            time.sleep(1)
            self.any_signal.emit(progress)
            
        # while (True):
        #     cnt+=1
        #     if cnt == 99:
        #         pass
        #         # cnt  =0
        #     time.sleep(0.01)
        #     self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        print('Thread stopped',self.index)
        self.terminate()
        
        
class Ui_Update_window(object):
    def setupUi(self, Update_window):
        Update_window.setObjectName("Update_window")
        Update_window.resize(339, 123)
        Update_window.setStyleSheet("QPushButton {\n"
"    background-color: rgb(29,94,255);\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"color: white;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-family: \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: skyblue;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: dodgerblue;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Update_window)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(parent=Update_window)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.label_note = QtWidgets.QLabel(parent=Update_window)
        self.label_note.setObjectName("label_note")
        self.gridLayout.addWidget(self.label_note, 0, 0, 1, 2)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=Update_window)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 5, 0, 1, 1)
        self.pushButton_download = QtWidgets.QPushButton(parent=Update_window)
        self.pushButton_download.setObjectName("pushButton_download")
        self.gridLayout.addWidget(self.pushButton_download, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)

        self.retranslateUi(Update_window)
        QtCore.QMetaObject.connectSlotsByName(Update_window)

    def retranslateUi(self, Update_window):
        _translate = QtCore.QCoreApplication.translate
        Update_window.setWindowTitle(_translate("Update_window", "Update_window"))
        self.label_note.setText(_translate("Update_window", "Update size is 24MB"))
        self.pushButton_cancel.setText(_translate("Update_window", "Cancel"))
        self.pushButton_download.setText(_translate("Update_window", "Download"))

        self.pushButton_download.clicked.connect(self.start_download)
        self.pushButton_cancel.clicked.connect(self.stop_download)

######################################## Main funciton ########################################

        cloud = DropboxSync()
        cloud.token_checker()
        dropbox_folder_size = int(cloud.get_folder_size("/Download/update_folder")/1000000)
        self.label_note.setText(f"Update size is {dropbox_folder_size}MB")
        self.progressBar.setValue(0)
        self.progressBar.hide()
        # self.cloud = DropboxSync()
        self.thread = {}
        
    

    def start_download(self):
        self.thread[1] = ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.progressBar.show()
        self.thread[1].any_signal.connect(self.my_funtion)
        self.pushButton_download.setEnabled(False)
        self.downl = DownloadThread()
        self.downl.finished.connect(self.stop_download)
        self.downl.start()
        
    def stop_download(self):
        self.thread[1].stop()
        self.label_note.setText("Download Complete...")
        # self.progressBar.hide()
        # self.pushButton_download.setEnabled(True)
    
    def my_funtion(self, counter):
        cnt = counter
        index = 1
        if index == 1:
            self.progressBar.setValue(cnt)
            
    # def download_process(self):
    #     self.cloud.token_checker()
    #     dropbox_folder_size = int(self.cloud.get_folder_size("/Download/update_folder"))
    #     print(dropbox_folder_size)
    #     local_folder_size = 0
    #     download_flag = 0
    #     # return
        
    #     while int(local_folder_size) < dropbox_folder_size:
    #         QtWidgets.QApplication.processEvents()
            
    #         if download_flag == 0:
    #             download_flag = 1
    #             self.cloud.download_changed("./Main_Software/Download_files",'/Download')
            
    #         local_folder_size = self.cloud.get_local_folder_size("./Main_Software/Download_files")
    #         self.update_progress_bar(local_folder_size, dropbox_folder_size)
            
    #         QtCore.QThread.msleep(50)  # Simulate some delay

    def update_progress_bar(self, current_size, total_size):
        progress = int((current_size / total_size) * 100)
        self.progressBar.setValue(progress)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_window = QtWidgets.QDialog()
    ui = Ui_Update_window()
    ui.setupUi(Update_window)
    Update_window.show()
    sys.exit(app.exec())
