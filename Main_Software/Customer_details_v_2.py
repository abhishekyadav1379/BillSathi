

import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QApplication, QTableWidgetItem
from PyQt6.QtWidgets import QTableWidgetItem, QMenu, QMessageBox, QToolTip
from PyQt6.QtGui import QStandardItemModel, QDoubleValidator, QFont, QStandardItem, QAction, QColor, QGuiApplication,QIcon
from PyQt6.QtCore import Qt
from DialogBox_alltype import *
from All_function import all_function, TooltipDelegate
from NewEntryCode import NewEntry
from pdf_create import *
import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtCore import QTimer, QDate
from NewEntryCode import NewEntry, FloatOrADelegate, FloatOrAValidator
import webbrowser
import icons_rc
from toaster import QToaster
from PyQt6.QtWidgets import QApplication, QHeaderView,QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QFont, QColor, QLinearGradient,QBrush,QGuiApplication
import sys
import webbrowser
from Invoice_generator import InvoiceGenerator


class Ui_Customer_details_v_2(object):
    def __init__(self, dialog):
        self.dialog = dialog
    def setupUi(self, Customer_details_v_2):
        Customer_details_v_2.setObjectName("Customer_details_v_2")
        Customer_details_v_2.resize(1168, 818)
        Customer_details_v_2.setStyleSheet("#frame,#frame_5,#frame_2{\n"
"border: 2px solid #c0c0c0;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    font-family: Russo One;\n"
"    font-size: 22px;\n"
"    border : 0px;\n"
"}")
        self.gridLayout_5 = QtWidgets.QGridLayout(Customer_details_v_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sales_report_label = QtWidgets.QLabel(parent=Customer_details_v_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.sales_report_label.setFont(font)
        self.sales_report_label.setObjectName("sales_report_label")
        self.gridLayout_5.addWidget(self.sales_report_label, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(parent=Customer_details_v_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=Customer_details_v_2)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setStyleSheet("#frame_4{\n"
"border: 2px solid #c0c0c0;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"}\n"
"QLineEdit {\n"
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
"\n"
"QLabel {\n"
"    font-family: Russo One;\n"
"    font-size: 22px;\n"
"    border : 0px;\n"
"}\n"
"QDialog{\n"
"background-color: rgb(50, 62, 67);\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setStyleSheet("QToolButton{\n"
"    font-size: 14px;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton_pdf = QtWidgets.QToolButton(parent=self.frame_5)
        self.toolButton_pdf.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-pdf-100.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_pdf.setIcon(icon)
        self.toolButton_pdf.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_pdf.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_pdf.setObjectName("toolButton_pdf")
        self.gridLayout_3.addWidget(self.toolButton_pdf, 0, 1, 1, 1)
        self.toolButton_entry = QtWidgets.QToolButton(parent=self.frame_5)
        self.toolButton_entry.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/new_entry_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_entry.setIcon(icon1)
        self.toolButton_entry.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_entry.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_entry.setObjectName("toolButton_entry")
        self.gridLayout_3.addWidget(self.toolButton_entry, 1, 1, 1, 1)
        self.toolButton_message = QtWidgets.QToolButton(parent=self.frame_5)
        self.toolButton_message.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-message-80.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_message.setIcon(icon2)
        self.toolButton_message.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_message.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_message.setObjectName("toolButton_message")
        self.gridLayout_3.addWidget(self.toolButton_message, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame_5)
        self.dateEdit.setStyleSheet("QDateEdit {\n"
"  background-color: rgb(213, 202, 255);\n"
"  border: 1px solid #dcdcdc;\n"
"  border-radius: 4px;\n"
"  selection-background-color: rgb(215, 192, 255);\n"
"  selection-color: #333333;\n"
"  font-size: 16px;\n"
"  color: #333333;\n"
"}\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_5)
        self.comboBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-family: Belanosima;\n"
"    font-size: 18px;\n"
"    background-color: rgb(231, 255, 215);\n"
"}\n"
"")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 2, 1, 1, 1)
        self.toolButton_telegram = QtWidgets.QToolButton(parent=self.frame_5)
        self.toolButton_telegram.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons8-telegram-480.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_telegram.setIcon(icon3)
        self.toolButton_telegram.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_telegram.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_telegram.setObjectName("toolButton_telegram")
        self.gridLayout_3.addWidget(self.toolButton_telegram, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.frame_4)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.gridLayout_2.addWidget(self.name_label, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.id_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("QLabel{\n"
" color: blue;\n"
"}")
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_3.addWidget(self.id_label)
        self.toolButton_copy = QtWidgets.QToolButton(parent=self.frame)
        self.toolButton_copy.setStyleSheet("QToolButton{\n"
"border: None;\n"
"margin-bottom: 10px;\n"
"margin-right: 15px\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/copy-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_copy.setIcon(icon4)
        self.toolButton_copy.setObjectName("toolButton_copy")
        self.horizontalLayout_3.addWidget(self.toolButton_copy)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.place_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.place_label.setFont(font)
        self.place_label.setObjectName("place_label")
        self.gridLayout_2.addWidget(self.place_label, 2, 0, 1, 1)
        self.phone_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout_2.addWidget(self.phone_label, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.overall_total_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.overall_total_label.setFont(font)
        self.overall_total_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.overall_total_label.setStyleSheet("")
        self.overall_total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.overall_total_label.setObjectName("overall_total_label")
        self.gridLayout.addWidget(self.overall_total_label, 0, 0, 1, 1)
        self.lineEdit_overall_total = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_overall_total.setStyleSheet("QLineEdit{\n"
"    color:red;\n"
"    font-size: 16px;\n"
"}")
        self.lineEdit_overall_total.setObjectName("lineEdit_overall_total")
        self.gridLayout.addWidget(self.lineEdit_overall_total, 0, 1, 1, 1)
        self.remaining_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.remaining_label.setFont(font)
        self.remaining_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.remaining_label.setObjectName("remaining_label")
        self.gridLayout.addWidget(self.remaining_label, 1, 0, 1, 1)
        self.lineEdit_rem_total = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_rem_total.setStyleSheet("QLineEdit{\n"
"    color:red;\n"
"    font-size: 16px;\n"
"}")
        self.lineEdit_rem_total.setReadOnly(True)
        self.lineEdit_rem_total.setObjectName("lineEdit_rem_total")
        self.gridLayout.addWidget(self.lineEdit_rem_total, 1, 1, 1, 1)
        self.give_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.give_label.setFont(font)
        self.give_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.give_label.setStyleSheet("")
        self.give_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.give_label.setObjectName("give_label")
        self.gridLayout.addWidget(self.give_label, 2, 0, 1, 1)
        self.lineEdit_give = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit_give.setStyleSheet("QLineEdit{\n"
"    color:red;\n"
"    font-size: 16px;\n"
"}")
        self.lineEdit_give.setObjectName("lineEdit_give")
        self.gridLayout.addWidget(self.lineEdit_give, 2, 1, 1, 1)
        self.lineEdit_comment = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_comment.setFont(font)
        self.lineEdit_comment.setStyleSheet("QLineEdit{\n"
"margin-bottom: 0px;\n"
"}")
        self.lineEdit_comment.setText("")
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 3, 0, 1, 1)
        self.pushButton_submit = QtWidgets.QPushButton(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet("QPushButton {\n"
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
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.gridLayout.addWidget(self.pushButton_submit, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 4, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(parent=Customer_details_v_2)
        self.treeWidget.setStyleSheet("QTreeWidget {\n"
"        font-size: 16px;\n"
"        background-color: rgb(218, 245, 255);\n"
"    }\n"
"    \n"
"    QTreeWidget::item {\n"
"        padding: 10px;\n"
"    }\n"
"\n"
"    QTreeWidget::item:selected {\n"
"        background-color: #89AEF9;\n"
"        color: white;\n"
"    }\n"
"    \n"
"    QTreeWidget::item:disabled {\n"
"        background-color: #DDD;\n"
"        color: #888;\n"
"    }\n"
"    QTableWidget::item:hover {\n"
"    background-color: #E6F1FF;\n"
"}\n"
"\n"
"    \n"
"    QTreeWidget QHeaderView::section {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                        stop:0 #4876AF, stop:1 #286090);\n"
"        color: white;\n"
"        font-weight: bold;\n"
"        padding: 4px;\n"
"        border: none;\n"
"        border-bottom: 1px solid #355F8C;\n"
"        border-radius: 4px;\n"
"        border-top-right-radius: 14px;\n"
"}\n"
"QTreeWidget::item:open:has-children {\n"
"        background-color: #007ACC;\n"
"        color: white;\n"
"        }\n"
"")
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.treeWidget, 1, 1, 1, 4)

        self.retranslateUi(Customer_details_v_2)
        QtCore.QMetaObject.connectSlotsByName(Customer_details_v_2)

    def retranslateUi(self, Customer_details_v_2):
        _translate = QtCore.QCoreApplication.translate
        Customer_details_v_2.setWindowTitle(_translate("Customer_details_v_2", "Customer Details"))
        self.sales_report_label.setText(_translate("Customer_details_v_2", "Sales Report"))
        self.checkBox.setText(_translate("Customer_details_v_2", "Expand"))
        self.toolButton_pdf.setText(_translate("Customer_details_v_2", "PDF       "))
        self.toolButton_entry.setText(_translate("Customer_details_v_2", "Entry     "))
        self.toolButton_message.setText(_translate("Customer_details_v_2", "Message"))
        self.comboBox.setItemText(0, _translate("Customer_details_v_2", "Cash"))
        self.comboBox.setItemText(1, _translate("Customer_details_v_2", "UPI"))
        self.comboBox.setItemText(2, _translate("Customer_details_v_2", "Cheaque"))
        self.toolButton_telegram.setText(_translate("Customer_details_v_2", "Telegram"))
        self.name_label.setText(_translate("Customer_details_v_2", "Name"))
        self.id_label.setText(_translate("Customer_details_v_2", "ID"))
        self.toolButton_copy.setText(_translate("Customer_details_v_2", "..."))
        self.place_label.setText(_translate("Customer_details_v_2", "Place"))
        self.phone_label.setText(_translate("Customer_details_v_2", "Phone"))
        self.overall_total_label.setText(_translate("Customer_details_v_2", "Overall Total"))
        self.remaining_label.setText(_translate("Customer_details_v_2", "Remaining Amount"))
        self.give_label.setText(_translate("Customer_details_v_2", "Paid"))
        self.lineEdit_comment.setPlaceholderText(_translate("Customer_details_v_2", "Comments"))
        self.pushButton_submit.setText(_translate("Customer_details_v_2", "Submit"))
        self.treeWidget.headerItem().setText(0, _translate("Customer_details_v_2", "Date"))
        self.treeWidget.headerItem().setText(1, _translate("Customer_details_v_2", "Time"))
        self.treeWidget.headerItem().setText(2, _translate("Customer_details_v_2", "Give"))
        self.treeWidget.headerItem().setText(3, _translate("Customer_details_v_2", "Total"))
        self.treeWidget.headerItem().setText(4, _translate("Customer_details_v_2", "Method"))


###################### Main code from here ######################
        width, height, taskbar_height = self.show_screen_dimensions()
        Customer_details_v_2.resize(width, height - taskbar_height)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.on_date_changed)
        self.checkBox.clicked.connect(self.expand_collapse_all_items)
        self.toolButton_telegram.clicked.connect(self.send_file_to_telegram)
        self.toolButton_message.clicked.connect(self.send_message_to_telegram)
        self.toolButton_pdf.clicked.connect(self.customer_pdf)
        self.toolButton_entry.clicked.connect(self.new_entry)
        self.toolButton_copy.clicked.connect(self.copyid)
        self.pushButton_submit.clicked.connect(self.submit_btn) 
        self.lineEdit_give.setValidator(QDoubleValidator())
        self.current_date = QtCore.QDate.currentDate().toString("yyyy-MM-dd")
        self.treeWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)  # Enable custom context menu
        self.treeWidget.customContextMenuRequested.connect(self.showContextMenu)


    current_time = QtCore.QTime.currentTime().toString("HH:mm:ss")
    fn = all_function()
    
    def on_date_changed(self):
        self.current_date = self.dateEdit.date().toString("yyyy-MM-dd")
    
    def refresh_data(self):
        self.treeWidget.clear()
        self.first_function(self.id)
        
    def new_entry(self):
        id = self.id_label.text()
        # id,name, phone,addr = self.fn.select_db(f"SELECT * FROM CUSTOMER WHERE ID = '{self.id_label.text()}'")[0]
        my_dialog = NewEntry()
        my_dialog.new_cust_entry(id)
        my_dialog.exec()
        self.refresh_data()
    
    def add_data(self):
        try:
            # Establish SQLite connection
            # mydb = sqlite3.connect('./Main_Software/mahendra.db')
            # mycursor = mydb.cursor()
            cust_id = self.id_label.text()
            name = self.name_label.text()
            give = self.lineEdit_give.text()
            method = self.comboBox.currentText()
            comment = self.lineEdit_comment.text()
            # date = datetime.date.today().strftime("%d-%m-%Y")
            time = datetime.datetime.now().time().strftime("%H:%M:%S")
            total = "0"
            comment = "*" + comment
            # Fill customer details
            query = f"INSERT INTO Money (ID, Date,Name,Give, Total,Method, Time,comment) VALUES (?,?,?,?,?,?,?,?)"
            val = (cust_id, self.current_date, name,
                   give, total, method, time, comment)
            self.fn.insert_db(query, val)

        except:
            print("Error: in add data customer_details.py")
    
    def submit_btn(self):
        item = self.lineEdit_give
        if item is not None and item.text() != "":
            rem = item.text()
            if len(rem) == 1 and (rem in ['-', '+', '.']):
                DialogBox.show_warning_dialog(
                    "Please Enter correct Details in Pay field")
                return
            self.add_data()
            self.refresh_data()
            item.setText("")
            self.lineEdit_comment.setText("")
            QToaster.showMessage("Record is Submitted.",parent = self.dialog, timeout=2000,corner=QtCore.Qt.Corner.BottomRightCorner)
            self.refresh_data()

    def customer_pdf(self):
        # id = self.id_label.text()
        InvoiceGenerator.Customer_details_pdf_create(self.id)
        # InvoicePdf.generate_customer_details(self.id)
        file_path = r"Main_Software\Image_pdf\customer_details.pdf"
        webbrowser.open(file_path)
        # self.open_pdf_in_default_browser()
    
    def send_file_to_telegram(self):
        id,name,address,phone = self.id_label.text(),self.name_label.text(),self.place_label.text(),self.phone_label.text()
        content = f"{id}\n{name}\n{address}\n{phone}"
        InvoiceGenerator.Customer_details_pdf_create(self.id)
        self.fn.send_pdf_with_text_to_telegram(r"./Main_Software/Image_pdf/customer_details.pdf",f"{name}_{id}.pdf",content)
        QToaster.showMessage("File send to Telegram.",parent = self.dialog, timeout=2000,corner=QtCore.Qt.Corner.BottomRightCorner)
        
    def send_message_to_telegram(self):
        id,name,address,phone = self.id_label.text(),self.name_label.text(),self.place_label.text(),self.phone_label.text()
        print(id)
        # content = f"{id}\n{name}\n{address}\n{phone}"
        amount = self.fn.select_db(f"select sum(Total - Give) from Money where id = '{id}'")[0][0]
        print(amount)
        message = f'''प्रिय {name},
हम आशा करते है कि आप नए निर्माण का लाभ उठा रहे होंगे | 
आपका  ₹ {amount} राशि बकाया है, कृपया इसका भुगतान करने का कष्ट करे | 
तो महान दया होगी| 

धन्यवाद
न्यू महेंद्रा ट्रेडर्स'''
        self.fn.send_message_to_telegram(message)
        QToaster.showMessage("Message send to Telegram.",parent = self.dialog, timeout=2000,corner=QtCore.Qt.Corner.BottomRightCorner)
        
        
    
    def copyid(self):
        id = self.id_label.text()
        clipboard = QGuiApplication.clipboard()
        clipboard.clear()
        clipboard.setText(id)

    
    def show_screen_dimensions(self):
        screen = QGuiApplication.primaryScreen()
        available_geometry = screen.availableGeometry()
        screen_size = available_geometry.size()
        taskbar_height = screen.geometry().height() - available_geometry.height()

        width = screen_size.width()
        height = screen_size.height()
        return [width, height, taskbar_height - 15]

    def convert_to_string_lists(self, input_list):
        result = [[str(item) for item in sublist] for sublist in input_list]
        return result
    
    def set_font(self,index, item):
        font = QFont()
        font.setBold(True)
        font.setPointSize(11)
        item.setFont(index, font)
    
    def set_speacial_font(self, index, item):
        font = QFont()
        font.setPointSize(13)
        item.setFont(index, font)
    
    def set_background_color(self,index, item, color):
        item.setBackground(index, color)
    
    def set_Foreground_color(self,index, item, color):
        item.setForeground(index, color)
        
    def showContextMenu(self, pos):
        current_item = self.treeWidget.itemAt(pos)
        if current_item is not None and current_item.parent() is None:  # Check if the right-clicked item is the parent
            row = self.treeWidget.currentItem()
            context_menu = QMenu()
            delete_action = context_menu.addAction(QIcon(":/icons/delete_icon.png"),'Delete')
            edit_date = context_menu.addAction(QIcon(":/icons/new_entry_icon.png"),'Edit')
            delete_action.triggered.connect(lambda: self.deleteDate(row))
            edit_date.triggered.connect(lambda: self.editDate(row))
            context_menu.exec(self.treeWidget.viewport().mapToGlobal(pos))
            
    def deleteDate(self, item):
        id = self.id
        get_date = item.text(0)
        time = item.text(1)
        result = DialogBox.show_yes_no_dialog(
            "Are you sure you want to delete date and time " + get_date + "?")
        if result == False:
            return
        get_date = self.fn.convert_date_format(get_date)
        time = self.fn.time_convert(time)
        query = "DELETE FROM product WHERE date = ? and id = ? and time = ?"
        val = (get_date, id, time)
        self.fn.insert_db(query, val)
        query = "DELETE FROM money WHERE date = ? and id = ? and time = ?"
        val = (get_date, id, time)
        self.fn.insert_db(query, val)
        self.refresh_data()
    
    def editDate(self, item):
        id = self.id
        get_date_table = item.text(0)
        time_table = item.text(1)
        fn = all_function()
        get_date = fn.convert_date_format(get_date_table)
        time = fn.time_convert(time_table)
        
        id, name, place, phone = self.fn.select_db(
            f"SELECT * FROM CUSTOMER WHERE ID = '{id}'")[0]
        table = self.fn.select_db(
            f"SELECT prod,quantity,rate,value FROM PRODUCT WHERE ID = '{id}' AND DATE = '{get_date}' AND TIME = '{time}'")
        method, give,comment = self.fn.select_db(
            f"SELECT METHOD,GIVE,comment FROM Money WHERE ID = '{id}' AND DATE = '{get_date}' AND TIME = '{time}' ")[0]
        
        if len(table) == 0:
            QToaster.showMessage("एडिट करना संभव नहीं | ",parent = self.dialog, timeout=2000,corner=QtCore.Qt.Corner.BottomRightCorner)
        
            return
        # rem = self
        # print(method,give)
        # print(table,id,name,place,phone)
        if method == "Udhar" or method == "Jma":
            method = "Udhar/Jma"
        my_dialog = NewEntry()
        my_dialog.Edit_Record(id, name, place, phone,
                              table, get_date_table, time_table, method, give,comment)
        my_dialog.exec()
        self.refresh_data()
    
    def expand_collapse_all_items(self):
        if self.checkBox.isChecked():
            self.expand_all_items()
        else:
            self.collapse_all_items()
    
    def expand_all_items(self):
        for item_index in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(item_index)
            self.expand_item(item)

    def collapse_all_items(self):
        for item_index in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(item_index)
            self.collapse_item(item)

    def expand_item(self, item):
        # Recursively expand the current item and its children
        item.setExpanded(True)
        for i in range(item.childCount()):
            child = item.child(i)
            self.expand_item(child)

    def collapse_item(self, item):
        # Recursively collapse the current item and its children
        item.setExpanded(False)
        for i in range(item.childCount()):
            child = item.child(i)
            self.collapse_item(child)
            
    def algorithm(self,id):
        parent_item = None
        fn = all_function()
        products = fn.select_db(
            f'''select strftime('%d-%m-%Y', Date),CASE
                    WHEN CAST(strftime('%H', time) AS INTEGER) >= 12 THEN
                        CASE
                            WHEN CAST(strftime('%H', time) AS INTEGER) > 12 THEN
                                printf('%02d', CAST(strftime('%H', time) AS INTEGER) - 12)
                            ELSE
                                '12'
                        END || ':' || 
                        strftime('%M:%S', time) || ' PM'
                    ELSE
                        time || ' AM'
                END AS converted_time,prod,quantity,rate,value,method from product where id = '{id}' order by date desc,time desc''')
        money = fn.select_db(
            f'''select strftime('%d-%m-%Y', Date),CASE
                WHEN CAST(strftime('%H', time) AS INTEGER) >= 12 THEN
                    CASE
                        WHEN CAST(strftime('%H', time) AS INTEGER) > 12 THEN
                            printf('%02d', CAST(strftime('%H', time) AS INTEGER) - 12)
                        ELSE
                            '12'
                    END || ':' || 
                    strftime('%M:%S', time) || ' PM'
                ELSE
                    time || ' AM'
            END AS converted_time,give,total,method,comment from money where id = '{id}' order by date desc,time desc''')
        products = self.convert_to_string_lists(products)
        money = self.convert_to_string_lists(money)
        
        # Algorithm to create the tree
        pro_len = len(products)
        mon_len = len(money)
        
        p, m = 0, 0
        a = 1
        while p != pro_len and m != mon_len:
            if pro_len == 0:
                break
            if (products[p][0] + products[p][1]) != (money[m][0] + money[m][1]):
                parent_item = QTreeWidgetItem(self.treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
                #set font in first parent for money
                if money[m][5] not in ["*","",None]:
                    parent_child = QTreeWidgetItem(parent_item, ["Comment: ",money[m][5]])
                    parent_child.setToolTip(1, money[m][5])
                for i in range(5):
                    self.set_font(i, parent_item)
                    self.set_Foreground_color(i, parent_item, QColor(255, 0, 0))
                m += 1
            else:
                parent_item = QTreeWidgetItem(self.treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
                parent_child = QTreeWidgetItem(parent_item, ["Product", "Quantity", "Rate", "Amount"])
                #it set backgorund color in money main parent
                for i in range(5):
                    self.set_speacial_font(i,parent_item)
                if a%2 == 0:
                    for i in range(5):
                        self.set_background_color(i, parent_item, QColor(229, 249, 255))
                        # self.set_font(i, parent_item)
                a+=1
                
                #it set the color in product first  row
                for i in range(4):
                    self.set_background_color(i, parent_child, QColor(120, 193, 243))
                    self.set_font(i, parent_child)
                
                
                
                # here we check when product purchase
                while (p != pro_len and m != mon_len) and ((products[p][0] + products[p][1]) == (money[m][0] + money[m][1])):
                    parent_child = QTreeWidgetItem(parent_item, [products[p][2], products[p][3], products[p][4], products[p][5]])
                    parent_child.setToolTip(0, products[p][2])
                    for i in range(4):
                        self.set_background_color(i, parent_child, QColor(230, 252, 255))
                    p += 1
                parent_child = QTreeWidgetItem(parent_item, ["Paid:", "₹ " + money[m][2], "Total:","₹ "+ money[m][3]])

                # here we set font andcolor in paid and total row
                for i in range(4):
                    if i%2==0:
                        self.set_Foreground_color(i, parent_child, QColor(255, 0, 0))
                    self.set_font(i, parent_child)
                    self.set_background_color(i, parent_child, QColor(200, 214, 255))
                if money[m][5] in ["*","", None]:
                    parent_child = QTreeWidgetItem(parent_item, ["Method:", money[m][4], "", ""])
                else:
                    parent_child = QTreeWidgetItem(parent_item, ["Method:", money[m][4], "Comment:", money[m][5]])
                    parent_child.setToolTip(3, money[m][5])
                #this is for method row
                for i in range(4):
                    if i%2 == 0:
                        self.set_Foreground_color(i, parent_child, QColor(255, 0, 0))
                    self.set_font(i, parent_child)
                    self.set_background_color(i, parent_child, QColor(200, 214, 255))
                m += 1

        while m != mon_len:
            parent_item = QTreeWidgetItem(self.treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
            if money[m][5] not in ["*","",None]:
                parent_child = QTreeWidgetItem(parent_item, ["Comment: ",money[m][5]])
                parent_child.setToolTip(1, money[m][5])
            for i in range(5):
                self.set_font(i, parent_item)
                self.set_Foreground_color(i, parent_item, QColor(255, 0, 0))
            m += 1

        # treeWidget.setAlternatingRowColors(True)
        self.treeWidget.header().setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch)
    
    def first_function(self,id):
        self.id = id
        id,name,address,phone = self.fn.select_db(f"SELECT id,name,address,phone FROM CUSTOMER WHERE ID = '{self.id}'")[0]
        self.name_label.setText(name)
        self.id_label.setText(id)
        self.place_label.setText(address)
        self.phone_label.setText(phone)
        
        remaining = self.fn.select_db(f"select sum(Total - Give) from Money where id = '{self.id}'")[0][0]
        if remaining is not None:
            remaining = round(remaining, 2)
        self.lineEdit_rem_total.setText(str(remaining))
        
        overall_total = self.fn.select_db(f"select sum(Total) from Money where id = '{self.id}'")[0][0]
        if overall_total is not None:
            overall_total = round(overall_total, 2)
        self.lineEdit_overall_total.setText(str(overall_total))
        self.algorithm(self.id)
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Customer_details_v_2 = QtWidgets.QDialog()
#     ui = Ui_Customer_details_v_2()
#     ui.setupUi(Customer_details_v_2)
#     Customer_details_v_2.show()
#     sys.exit(app.exec())
