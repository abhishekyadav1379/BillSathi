# Form implementation generated from reading ui file 'c:\Users\mrabh\OneDrive\Desktop\Pyqt\Main_Software\UdhariGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem,QTableWidget, QMenu, QMessageBox, QHeaderView,QApplication
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QAction,QFont
from Customer_DetailsGUI_ui import Ui_Customer_details
from PyQt6.QtCore import Qt
from All_function import all_function, TooltipDelegate
import sqlite3
from EntryGUI_ui import SpeechRecognitionThread
import icons_rc


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication


class Ui_Udhari_Dialog(object):
    def setupUi(self, Udhari_Dialog):
        Udhari_Dialog.setObjectName("Udhari_Dialog")
        Udhari_Dialog.resize(743, 740)
        Udhari_Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Udhari_Dialog.setStyleSheet("QLineEdit {\n"
"                background-color: #f3f3f3;\n"
"                border: 2px solid #c0c0c0;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                selection-background-color: #a8a8a8;\n"
"            }\n"
"\n"
"            QLineEdit:focus {\n"
"                border: 2px solid #707070;\n"
"                background-color: #ffffff;\n"
"            }\n"
"\n"
"QDialog{\n"
"    background-color: #D2E9E9;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Udhari_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_udhari = QtWidgets.QTableWidget(parent=Udhari_Dialog)
        self.tableWidget_udhari.setStyleSheet("QTableWidget {\n"
"    background-color: white;\n"
"    gridline-color: #DDDDDD;\n"
"    selection-background-color: #E6F1FF;\n"
"    selection-color: #333333;\n"
"\n"
"}\n"
"QTableWidget::item {\n"
"    text-align: center;\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #4876AF, stop:1 #286090);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #355F8C;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section:second {\n"
"    border-top-right-radius: 14px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #B3D7FF;\n"
"    color: #333333;\n"
"}\n"
"QTableWidget QHeaderView::section:pressed {\n"
"    background-color: #4F8BC9;\n"
"}\n"
"\n"
"QTableWidget::item:alternate { background-color: #c5edea; }\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #E6F1FF;\n"
"}")
        self.tableWidget_udhari.setObjectName("tableWidget_udhari")
        self.tableWidget_udhari.setColumnCount(4)
        self.tableWidget_udhari.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_udhari.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_udhari.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_udhari.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_udhari.setHorizontalHeaderItem(3, item)
        self.tableWidget_udhari.horizontalHeader().setDefaultSectionSize(180)
        self.gridLayout.addWidget(self.tableWidget_udhari, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=Udhari_Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame {\n"
"    border: 2px solid #dddddd;\n"
"    border-radius: 5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_name = QtWidgets.QComboBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Belanosima")
        font.setPointSize(-1)
        self.comboBox_name.setFont(font)
        self.comboBox_name.setStyleSheet("QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-family: Belanosima;\n"
"    font-size: 18px;\n"
"    background-color: rgb(231, 255, 215);\n"
"}\n"
"")
        self.comboBox_name.setObjectName("comboBox_name")
        self.comboBox_name.addItem("")
        self.comboBox_name.addItem("")
        self.comboBox_name.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_name)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.toolButton_micro = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton_micro.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/microphone-black-shape.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_micro.setIcon(icon)
        self.toolButton_micro.setObjectName("toolButton_micro")
        self.horizontalLayout.addWidget(self.toolButton_micro)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_udhari_jma = QtWidgets.QCheckBox(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_udhari_jma.setFont(font)
        self.checkBox_udhari_jma.setObjectName("checkBox_udhari_jma")
        self.horizontalLayout.addWidget(self.checkBox_udhari_jma)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Udhari_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Udhari_Dialog)
        Udhari_Dialog.setTabOrder(self.lineEdit_name, self.checkBox_udhari_jma)
        Udhari_Dialog.setTabOrder(self.checkBox_udhari_jma, self.tableWidget_udhari)
        Udhari_Dialog.setTabOrder(self.tableWidget_udhari, self.toolButton_micro)
        Udhari_Dialog.setTabOrder(self.toolButton_micro, self.comboBox_name)

    def retranslateUi(self, Udhari_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Udhari_Dialog.setWindowTitle(_translate("Udhari_Dialog", "Udhari"))
        item = self.tableWidget_udhari.horizontalHeaderItem(0)
        item.setText(_translate("Udhari_Dialog", "ID"))
        item = self.tableWidget_udhari.horizontalHeaderItem(1)
        item.setText(_translate("Udhari_Dialog", "Name"))
        item = self.tableWidget_udhari.horizontalHeaderItem(2)
        item.setText(_translate("Udhari_Dialog", "Place"))
        item = self.tableWidget_udhari.horizontalHeaderItem(3)
        item.setText(_translate("Udhari_Dialog", "Phone No."))
        self.comboBox_name.setItemText(0, _translate("Udhari_Dialog", "Name"))
        self.comboBox_name.setItemText(1, _translate("Udhari_Dialog", "ID"))
        self.comboBox_name.setItemText(2, _translate("Udhari_Dialog", "Phone No."))
        self.toolButton_micro.setText(_translate("Udhari_Dialog", "..."))
        self.checkBox_udhari_jma.setText(_translate("Udhari_Dialog", "[Udhari, Jma]"))


# ------------------------------Main Editing--------------------#
        self.mainquery = "SELECT id,name,address,phone FROM Customer "
        self.checked = False
        self.recognition_thread = None
        self.toolButton_micro.clicked.connect(lambda: self.start_recognition(self.lineEdit_name, self.toolButton_micro))
        self.udhar_Record()
        screen_height = QApplication.primaryScreen().availableGeometry().height() - 30
        Udhari_Dialog.resize(743, screen_height)
        self.checkBox_udhari_jma.stateChanged.connect(self.checkBoxCode)
        self.lineEdit_name.textChanged.connect(self.update_table)
        # Connect the item clicked signal to a slot
        self.tableWidget_udhari.clicked.connect(self.on_table_item_clicked)
        # self.all_fn = all_function()
        self.tableWidget_udhari.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidget_udhari.customContextMenuRequested.connect(
            self.show_context_menu)
        initial_font_size = 11
        font = QFont()
        font.setPointSize(initial_font_size)
        self.lineEdit_name.setFont(font)

        # Menu
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget_udhari.setFont(font)
        self.tableWidget_udhari.setAlternatingRowColors(True)  # Enable alternating row colors

        self.delegate = TooltipDelegate()
        self.tableWidget_udhari.setItemDelegate(self.delegate)
        self.tableWidget_udhari.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
    fn = all_function()
    # show dialog box when right click

    def show_context_menu(self, position):
        indexes = self.tableWidget_udhari.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            menu = QMenu()
            delete_action = QAction("Delete Row")
            delete_action.triggered.connect(lambda: self.delete_row(row))
            menu.addAction(delete_action)

            action = menu.exec(
                self.tableWidget_udhari.viewport().mapToGlobal(position))

            # context_menu.exec(self.tableWidget_udhari.viewport().mapToGlobal(pos))
    # code for when clicked on row
    def delete_row(self, row):
        id = self.tableWidget_udhari.item(row, 0).text()
        name = self.tableWidget_udhari.item(row, 1).text()
        place = self.tableWidget_udhari.item(row, 2).text()
        phone = self.tableWidget_udhari.item(row, 3).text()
        # name = item.text()
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Warning)
        message_box.setText(
            f"Do you want to delete the data of \nID: '{id} \nName: '{name}' \nAddress: '{place} \nPhone No.: '{phone}' ?")
        message_box.setWindowTitle("Delete Row")
        message_box.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.No)

        reply = message_box.exec()
        if reply == QMessageBox.StandardButton.Yes:
            print("YES")
            self.fn.delete_db(id, 'Customer')
            self.fn.delete_db(id, 'Product')
            self.fn.delete_db(id, 'Money')
            self.udhar_Record()

    def on_table_item_clicked(self, item):
        # Get the selected row and column index
        row = item.row()
        column = item.column()
        # Get the data from the selected cell
        cell_value = self.tableWidget_udhari.item(row, 0).text()
        # Open the Customer Details dialog
        self.open_customer_details_dialog(cell_value)

    # it open the customer detils window when clicked in row
    def open_customer_details_dialog(self, cell_value):
        self.customer_dialog = QtWidgets.QDialog()
        self.customer_details_ui = Ui_Customer_details()
        self.customer_details_ui.setupUi(self.customer_dialog)
        self.customer_details_ui.update_data(cell_value)
        self.customer_dialog.exec()

    def update_table(self):
        # pass
        method = self.comboBox_name.currentText()
        value = self.lineEdit_name.text()
        if method == 'Name':
            self.udhar_Record(method, value)
        elif method == "ID":
            self.udhar_Record(method, value)
        elif method == "Phone No.":
            self.udhar_Record(method, value)

        # connect---------------------------

    def checkBoxCode(self):
        if self.checkBox_udhari_jma.isChecked():
            self.checked = True
            self.mainquery = '''SELECT c.id, c.name, c.address, c.phone
                                FROM customer c
                                JOIN money m ON c.id = m.id
                                WHERE m.method IN ('Udhar', 'Jma') group by c.id'''
            # !Udhar 'U'  should be in capital letter
            self.udhar_Record()
        else:
            self.checked = False
            self.mainquery = "SELECT id,name,address,phone FROM Customer "
            self.udhar_Record()

    def udhar_Record(self, combo_value=None, value=None):
        try:
            # Establish SQLite connection
            fn = all_function()
            # mydb = sqlite3.connect('./Main_Software/mahendra.db')
            # mycursor = mydb.cursor()
            # print(combo_value)

            if combo_value == "Name":
                if self.checked == False:
                    query = f"{self.mainquery} WHERE NAME LIKE '{value}%' order by name"
                else:
                  
                    query = f"{self.mainquery} AND c.NAME LIKE '{value}%' order by c.NAME"
                # det = (value + '%',)
                # mycursor.execute(query, det)
                # result = fn.select_db
            elif combo_value == "ID":
                if self.checked == False:
                    query = f"{self.mainquery} WHERE ID LIKE '{value}%' order by id"
                else:
                    query = f"{self.mainquery} AND c.ID LIKE '{value}%' order by c.id"
                # det = (value + '%',)
                # mycursor.execute(query, det)
            elif combo_value == "Phone No.":
                if self.checked == False:
                    query = f"{self.mainquery} WHERE phone LIKE '{value}%' order by phone"
                else:
                    query = f"{self.mainquery} AND c.phone LIKE '{value}%' order by c.phone"
                # det = (value + '%',)
                # mycursor.execute(query, det)
            else:
                if self.checked == False:
                    query = f"{self.mainquery} ORDER BY ID DESC"
                else:
                    query = f"{self.mainquery} ORDER BY c.ID DESC"
                # query = self.mainquery + " ORDER BY ID DESC"
                # mycursor.execute(query)

            
            # result = mycursor.fetchall()
            result = fn.select_db(query)
            self.tableWidget_udhari.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_udhari.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget_udhari.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
            self.tableWidget_udhari.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch)


        except Exception as e:
            print("Error:", e)

        
        
##################Speech recognition#####################
    def closeEvent(self, event):
        if self.recognition_thread is not None and self.recognition_thread.isRunning():
            self.recognition_thread.quit()
            self.recognition_thread.wait()
        event.accept()

    def start_recognition(self,lineEdit, button):
        if self.recognition_thread is not None and self.recognition_thread.isRunning():
            return

        # button.setEnabled(False)
        self.toolButton_micro.setEnabled(False)
        # self.toolButton_name_micro.setEnabled(False)
        lineEdit.clear()
        lineEdit.setPlaceholderText("Listening...")
        self.recognition_thread = SpeechRecognitionThread()
        handle_result = lambda result: self.handle_recognition_result(result, lineEdit, button)
        self.recognition_thread.recognition_result.connect(handle_result)
        self.recognition_thread.finished.connect(self.cleanup_recognition_thread)
        self.recognition_thread.start()

    def handle_recognition_result(self, text, lineEdit, button):
        # button.setEnabled(True)
        self.toolButton_micro.setEnabled(True)
        # self.toolButton_name_micro.setEnabled(True)
        if text != "Error":
            if text != "Not Recognized":
                if text != "Timeout":
                    lineEdit.setText(text)
                else:
                    lineEdit.setPlaceholderText("Timeout")
            else:
                lineEdit.setPlaceholderText("Not Recognized")
        else:
            lineEdit.setPlaceholderText("Error occurred")

    def cleanup_recognition_thread(self):
        self.recognition_thread = None

# ----------------Working Area----------------#
