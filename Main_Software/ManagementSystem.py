from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from MainGUI_ui import Ui_MainGUI, TestChartWidget
from EntryGUI_ui import Ui_Entry_Window
from UdhariGUI_ui import Ui_Udhari_Dialog
# from RecordGUI_ui import Ui_record
from Labour_Record_ui import Ui_Labour_record
from stock_new import Ui_Stock
from RecordGUI_ui import Ui_record
# from RecordGUI_code import MyRecordDialog
from NewEntryCode import *
from settingUI import Ui_Settings,UploadThread
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PyQt6.QtCharts import QBarCategoryAxis, QBarSeries, QBarSet, QChart, QChartView, QValueAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from others import Ui_Others
# from loginUI import Ui_Login
# from Main import LoginDialog



class ManagementSystem(QMainWindow, Ui_MainGUI):
    def __init__(self):
        super().__init__()
        # window = QMainWindow()
        # tab_widget = QTabWidget()
        # print(self.date_label.text())
        # chart_widget = TestChartWidget()
        # self.tab.addTab(chart_widget, "Bar Chart")
        self.setupUi(self)
        self.show()
        
        self.entry_btn.clicked.connect(self.view_entry)
        self.udhari_btn.clicked.connect(self.view_udhari)
        self.record_btn.clicked.connect(self.view_daily_record)
        self.labour_btn.clicked.connect(self.view_labour_record)
        self.stock_btn.clicked.connect(self.view_stock_record)
        self.setting_btn.clicked.connect(self.view_setting)
        self.others_btn.clicked.connect(self.view_other)
        # self.login_btn.clicked.connect(self.view_Login)
        
    # def view_Login(self):
        # dialog = QDialog()
        # ui = Ui_Login()
        # ui.setupUi(dialog)
        # self.close()
        # lg = LoginDialog()
        # self.show()
        # dialog.exec()
    
    def view_other(self):
        dialog = QDialog()
        ui = Ui_Others()

        ui.setupUi(dialog)
        dialog.exec()
    
    def view_setting(self):
        dialog = QDialog()
        ui = Ui_Settings()

        ui.setupUi(dialog)
        dialog.exec()
        
    def view_entry(self):
        my_dialog = NewEntry()
        my_dialog.exec()
        self.refresh_chart()
        

    def view_udhari(self):
        dialog = QDialog()
        ui = Ui_Udhari_Dialog()

        ui.setupUi(dialog)
        dialog.exec()
        self.refresh_chart()

    def view_daily_record(self):
        dialog = QDialog()
        ui = Ui_record()

        ui.setupUi(dialog)
        dialog.exec()
        # my_dialog = Ui_record()
        # my_dialog.exec()

    def view_labour_record(self):
        dialog = QDialog()
        ui = Ui_Labour_record()

        ui.setupUi(dialog)
        dialog.exec()

    def view_stock_record(self):
        dialog = QDialog()
        ui = Ui_Stock()

        ui.setupUi(dialog)
        dialog.exec()
