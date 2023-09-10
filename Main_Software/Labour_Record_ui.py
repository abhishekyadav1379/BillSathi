

import configparser
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem,QTableWidget,QHeaderView,QApplication
from PyQt6.QtCore import QRegularExpression,QDate
from PyQt6.QtGui import QRegularExpressionValidator
from All_function import all_function
import sqlite3





class Ui_Labour_record(object):
    def setupUi(self, Labour_record):
        Labour_record.setObjectName("Labour_record")
        Labour_record.resize(940, 729)
        Labour_record.setStyleSheet("QDialog{\n"
"background-color: white;\n"
"}\n"
"\n"
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
"    font-size: 18px;\n"
"}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(Labour_record)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=Labour_record)
        self.frame_2.setStyleSheet("QLineEdit {\n"
"  color: red;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.frame_2)
        self.frame.setStyleSheet("QFrame {\n"
"  background-color: rgb(203, 235, 255);\n"
"  border: 0px solid #CCCCCC;\n"
"  border-radius: 5px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_sariya = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sariya.setFont(font)
        self.lineEdit_sariya.setReadOnly(True)
        self.lineEdit_sariya.setObjectName("lineEdit_sariya")
        self.gridLayout_2.addWidget(self.lineEdit_sariya, 5, 2, 1, 2)
        self.cement_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.cement_label.setFont(font)
        self.cement_label.setObjectName("cement_label")
        self.gridLayout_2.addWidget(self.cement_label, 1, 1, 1, 1)
        self.maurang_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.maurang_label.setFont(font)
        self.maurang_label.setObjectName("maurang_label")
        self.gridLayout_2.addWidget(self.maurang_label, 2, 1, 1, 1)
        self.gitti_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.gitti_label.setFont(font)
        self.gitti_label.setObjectName("gitti_label")
        self.gridLayout_2.addWidget(self.gitti_label, 3, 1, 1, 1)
        self.lineEdit_gitti = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_gitti.setFont(font)
        self.lineEdit_gitti.setReadOnly(True)
        self.lineEdit_gitti.setObjectName("lineEdit_gitti")
        self.gridLayout_2.addWidget(self.lineEdit_gitti, 3, 2, 1, 2)
        self.radioButton_rate = QtWidgets.QRadioButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_rate.setFont(font)
        self.radioButton_rate.setStyleSheet("")
        self.radioButton_rate.setObjectName("radioButton_rate")
        self.gridLayout_2.addWidget(self.radioButton_rate, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 2)
        self.label_sariya = QtWidgets.QLabel(parent=self.frame)
        self.label_sariya.setObjectName("label_sariya")
        self.gridLayout_2.addWidget(self.label_sariya, 5, 1, 1, 1)
        self.ring_label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.ring_label.setFont(font)
        self.ring_label.setObjectName("ring_label")
        self.gridLayout_2.addWidget(self.ring_label, 4, 1, 1, 1)
        self.lineEdit_maurang = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_maurang.setFont(font)
        self.lineEdit_maurang.setReadOnly(True)
        self.lineEdit_maurang.setObjectName("lineEdit_maurang")
        self.gridLayout_2.addWidget(self.lineEdit_maurang, 2, 2, 1, 2)
        self.lineEdit_cement = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cement.setFont(font)
        self.lineEdit_cement.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.lineEdit_cement.setInputMask("")
        self.lineEdit_cement.setText("")
        self.lineEdit_cement.setReadOnly(True)
        self.lineEdit_cement.setPlaceholderText("")
        self.lineEdit_cement.setClearButtonEnabled(True)
        self.lineEdit_cement.setObjectName("lineEdit_cement")
        self.gridLayout_2.addWidget(self.lineEdit_cement, 1, 2, 1, 2)
        self.lineEdit_ring = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_ring.setFont(font)
        self.lineEdit_ring.setReadOnly(True)
        self.lineEdit_ring.setObjectName("lineEdit_ring")
        self.gridLayout_2.addWidget(self.lineEdit_ring, 4, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no_of_ring_label = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.no_of_ring_label.setFont(font)
        self.no_of_ring_label.setObjectName("no_of_ring_label")
        self.horizontalLayout.addWidget(self.no_of_ring_label)
        self.lineEdit_no_of_ring = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_no_of_ring.setFont(font)
        self.lineEdit_no_of_ring.setObjectName("lineEdit_no_of_ring")
        self.horizontalLayout.addWidget(self.lineEdit_no_of_ring)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setStyleSheet("QFrame {\n"
"  background-color: rgb(211, 255, 239);\n"
"  border: 0px solid #CCCCCC;\n"
"  border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_total.setFont(font)
        self.lineEdit_total.setReadOnly(True)
        self.lineEdit_total.setObjectName("lineEdit_total")
        self.gridLayout.addWidget(self.lineEdit_total, 5, 3, 1, 1)
        self.total_label = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.gridLayout.addWidget(self.total_label, 5, 2, 1, 1)
        self.label_sariya_calc = QtWidgets.QLabel(parent=self.frame_3)
        self.label_sariya_calc.setStyleSheet("QLabel{\n"
"color: blue;\n"
"}")
        self.label_sariya_calc.setObjectName("label_sariya_calc")
        self.gridLayout.addWidget(self.label_sariya_calc, 4, 2, 1, 1)
        self.lineEdit_sariya_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sariya_total.setFont(font)
        self.lineEdit_sariya_total.setReadOnly(True)
        self.lineEdit_sariya_total.setObjectName("lineEdit_sariya_total")
        self.gridLayout.addWidget(self.lineEdit_sariya_total, 4, 3, 1, 1)
        self.lineEdit_gitti_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_gitti_total.setFont(font)
        self.lineEdit_gitti_total.setReadOnly(True)
        self.lineEdit_gitti_total.setObjectName("lineEdit_gitti_total")
        self.gridLayout.addWidget(self.lineEdit_gitti_total, 2, 3, 1, 1)
        self.cement_label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.cement_label_2.setFont(font)
        self.cement_label_2.setStyleSheet("")
        self.cement_label_2.setObjectName("cement_label_2")
        self.gridLayout.addWidget(self.cement_label_2, 0, 1, 1, 1)
        self.lineEdit_ring_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_ring_total.setFont(font)
        self.lineEdit_ring_total.setReadOnly(True)
        self.lineEdit_ring_total.setObjectName("lineEdit_ring_total")
        self.gridLayout.addWidget(self.lineEdit_ring_total, 3, 3, 1, 1)
        self.gitti_label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.gitti_label_2.setFont(font)
        self.gitti_label_2.setObjectName("gitti_label_2")
        self.gridLayout.addWidget(self.gitti_label_2, 2, 1, 1, 1)
        self.lineEdit_cement_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cement_total.setFont(font)
        self.lineEdit_cement_total.setReadOnly(True)
        self.lineEdit_cement_total.setObjectName("lineEdit_cement_total")
        self.gridLayout.addWidget(self.lineEdit_cement_total, 0, 3, 1, 1)
        self.label_sariya_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_sariya_2.setObjectName("label_sariya_2")
        self.gridLayout.addWidget(self.label_sariya_2, 4, 1, 1, 1)
        self.ring_label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.ring_label_2.setFont(font)
        self.ring_label_2.setObjectName("ring_label_2")
        self.gridLayout.addWidget(self.ring_label_2, 3, 1, 1, 1)
        self.label_cem_calc = QtWidgets.QLabel(parent=self.frame_3)
        self.label_cem_calc.setStyleSheet("QLabel{\n"
"color: blue;\n"
"}")
        self.label_cem_calc.setObjectName("label_cem_calc")
        self.gridLayout.addWidget(self.label_cem_calc, 0, 2, 1, 1)
        self.label_git_calc = QtWidgets.QLabel(parent=self.frame_3)
        self.label_git_calc.setStyleSheet("QLabel{\n"
"color: blue;\n"
"}")
        self.label_git_calc.setObjectName("label_git_calc")
        self.gridLayout.addWidget(self.label_git_calc, 2, 2, 1, 1)
        self.label_mau_calc = QtWidgets.QLabel(parent=self.frame_3)
        self.label_mau_calc.setStyleSheet("QLabel{\n"
"color: blue;\n"
"}")
        self.label_mau_calc.setObjectName("label_mau_calc")
        self.gridLayout.addWidget(self.label_mau_calc, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_ring_calc = QtWidgets.QLabel(parent=self.frame_3)
        self.label_ring_calc.setStyleSheet("QLabel{\n"
"color: blue;\n"
"}")
        self.label_ring_calc.setObjectName("label_ring_calc")
        self.gridLayout.addWidget(self.label_ring_calc, 3, 2, 1, 1)
        self.maurang_label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.maurang_label_2.setFont(font)
        self.maurang_label_2.setObjectName("maurang_label_2")
        self.gridLayout.addWidget(self.maurang_label_2, 1, 1, 1, 1)
        self.lineEdit_maurang_total = QtWidgets.QLineEdit(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_maurang_total.setFont(font)
        self.lineEdit_maurang_total.setReadOnly(True)
        self.lineEdit_maurang_total.setObjectName("lineEdit_maurang_total")
        self.gridLayout.addWidget(self.lineEdit_maurang_total, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)
        self.tableWidget_labour = QtWidgets.QTableWidget(parent=Labour_record)
        self.tableWidget_labour.setMinimumSize(QtCore.QSize(420, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_labour.setFont(font)
        self.tableWidget_labour.setAutoFillBackground(False)
        self.tableWidget_labour.setStyleSheet("QTableWidget {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #F7F7F7, stop:1 #E8E8E8);\n"
"    gridline-color: #DDDDDD;\n"
"    selection-background-color: #E6F1FF;\n"
"    selection-color: #333333;\n"
"\n"
"}\n"
"\n"
"QTableView::item:alternate { background-color: #c5edea; }\n"
"\n"
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
"    border-top-right-radius: 24px;\n"
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
"\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #E6F1FF;\n"
"}"
)
        self.tableWidget_labour.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget_labour.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget_labour.setLineWidth(1)
        self.tableWidget_labour.setMidLineWidth(0)
        self.tableWidget_labour.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_labour.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed)
        self.tableWidget_labour.setObjectName("tableWidget_labour")
        self.tableWidget_labour.setColumnCount(3)
        self.tableWidget_labour.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_labour.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_labour.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_labour.setHorizontalHeaderItem(2, item)
        self.tableWidget_labour.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_labour.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_labour.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget_labour, 0, 0, 1, 1)

        self.retranslateUi(Labour_record)
        QtCore.QMetaObject.connectSlotsByName(Labour_record)

    def retranslateUi(self, Labour_record):
        _translate = QtCore.QCoreApplication.translate
        Labour_record.setWindowTitle(_translate("Labour_record", "Labour Record"))
        self.cement_label.setText(_translate("Labour_record", "Cement"))
        self.maurang_label.setText(_translate("Labour_record", "Maurang"))
        self.gitti_label.setText(_translate("Labour_record", "Gitti"))
        self.radioButton_rate.setText(_translate("Labour_record", "Rate Change"))
        self.label_5.setText(_translate("Labour_record", "Rate per/Unit"))
        self.label_sariya.setText(_translate("Labour_record", "Sariya"))
        self.ring_label.setText(_translate("Labour_record", "Ring"))
        self.no_of_ring_label.setText(_translate("Labour_record", "No. of Rings:  "))
        self.total_label.setText(_translate("Labour_record", "Total"))
        self.label_sariya_calc.setText(_translate("Labour_record", "45 X 2.5"))
        self.cement_label_2.setText(_translate("Labour_record", "Cement:"))
        self.gitti_label_2.setText(_translate("Labour_record", "Gitti:"))
        self.label_sariya_2.setText(_translate("Labour_record", "Sariya"))
        self.ring_label_2.setText(_translate("Labour_record", "Ring:"))
        self.label_cem_calc.setText(_translate("Labour_record", "45 X 2.5"))
        self.label_git_calc.setText(_translate("Labour_record", "45 X 2.5"))
        self.label_mau_calc.setText(_translate("Labour_record", "45 X 2.5"))
        self.label_ring_calc.setText(_translate("Labour_record", "45 X 2.5"))
        self.maurang_label_2.setText(_translate("Labour_record", "Maurang: "))
        item = self.tableWidget_labour.horizontalHeaderItem(0)
        item.setText(_translate("Labour_record", "Name"))
        item = self.tableWidget_labour.horizontalHeaderItem(1)
        item.setText(_translate("Labour_record", "Description"))
        item = self.tableWidget_labour.horizontalHeaderItem(2)
        item.setText(_translate("Labour_record", "Quantity"))

#----------------------Main Working----------#
        self.fn = all_function()
        self.todayDate = QDate.currentDate().toString("yyyy-MM-dd")
        screen_height = QApplication.primaryScreen().availableGeometry().height() - 30
        Labour_record.resize(840, screen_height)
        # print(self.todayDate)
        font = QtGui.QFont()
        font.setPointSize(11) 
        self.tableWidget_labour.setFont(font)
        self.tableWidget_labour.setAlternatingRowColors(True)  # Enable alternating row colors
        self.Labour_Record()

        #Ui editing
        # self.date = QtCore.QDate.currentDate().toString(QtCore.Qt.DateFormat.ISODate)
        config = configparser.ConfigParser()
        config.read('./Main_Software/config.ini')

        # Create a regular expression to allow floating-point numbers and the letter 'a'
        regex = QRegularExpression('^([+-]?\\d*\\.\\d+)$|^a$')
        validator = QRegularExpressionValidator(regex)
        self.lineEdit_cement.setValidator(validator)
        self.lineEdit_gitti.setValidator(validator)
        self.lineEdit_maurang.setValidator(validator)
        self.lineEdit_sariya.setValidator(validator)
        self.lineEdit_ring.setValidator(validator)
        self.lineEdit_no_of_ring.setValidator(validator)
        
        self.lineEdit_cement.setText(config['Labour']['cement'])
        self.lineEdit_gitti.setText(config['Labour']['gitti'])
        self.lineEdit_maurang.setText(config['Labour']['maurang'])
        self.lineEdit_ring.setText(config['Labour']['ring'])
        self.lineEdit_sariya.setText(config['Labour']['sariya'])
        self.cem_gitti()
        self.lineEdit_no_of_ring.textChanged.connect(self.lineEdit_clicked)
        self.lineEdit_cement.textChanged.connect(self.lineEdit_clicked)
        self.lineEdit_gitti.textChanged.connect(self.lineEdit_clicked)
        self.lineEdit_maurang.textChanged.connect(self.lineEdit_clicked)
        self.lineEdit_sariya.textChanged.connect(self.lineEdit_clicked)
        self.lineEdit_ring.textChanged.connect(self.lineEdit_clicked)
        self.radioButton_rate.toggled.connect(self.on_radiobtn_click)

    #execute when radio btn is clicked
    def on_radiobtn_click(self):
        if self.radioButton_rate.isChecked():
            self.lineEdit_cement.setReadOnly(False)
            self.lineEdit_gitti.setReadOnly(False)
            self.lineEdit_maurang.setReadOnly(False)
            self.lineEdit_ring.setReadOnly(False)
            self.lineEdit_sariya.setReadOnly(False)
        else:
            self.lineEdit_cement.setReadOnly(True)
            self.lineEdit_gitti.setReadOnly(True)
            self.lineEdit_maurang.setReadOnly(True)
            self.lineEdit_ring.setReadOnly(True)
            self.lineEdit_sariya.setReadOnly(True)
            
    def lineEdit_clicked(self):
        self.cem_gitti()
                
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read an existing configuration file
    config.read('config.ini')
    def cem_gitti(self):
        try:
            # Establish SQLite connection
            # mydb = sqlite3.connect('./Main_Software/mahendra.db')
            # mycursor = mydb.cursor()
            query1 = f"SELECT SUM(quantity) AS total_quantity FROM product WHERE Prod LIKE '%cement%' and date = '{self.todayDate}'"
            # mycursor.execute(query1,)
            # cement = mycursor.fetchone()[0]
            cement = self.fn.select_db(query1)[0][0]

            query2 = f"SELECT sum(quantity) AS total_quantity FROM product WHERE Prod LIKE '%gitti%' and date = '{self.todayDate}'"
            # mycursor.execute(query2,)
            gitti = (self.fn.select_db(query2)[0][0] or 0)/100
            
            query3 = f"SELECT sum(quantity) AS total_quantity FROM product WHERE Prod LIKE '%maurang%' and date = '{self.todayDate}'"
            # mycursor.execute(query3,)
            maurang = ((self.fn.select_db(query3)[0][0]) or 0)/100
            
            query4 = f"SELECT SUM(quantity) AS total_quantity FROM product WHERE Prod LIKE '%sariya%' and date = '{self.todayDate}'"
            # mycursor.execute(query4,)
            sariya = self.fn.select_db(query4)[0][0]
            
            cem_lineEdit = self.lineEdit_cement
            gitt_lineEdit = self.lineEdit_gitti
            maurang_lineEdit = self.lineEdit_maurang
            sariya_lineEdit = self.lineEdit_sariya
            ring_lineEdit = self.lineEdit_ring
            calc_total = 0
            
            #Updata config file
            self.config['Labour'] = {
                'cement': cem_lineEdit.text(),
                'sariya': sariya_lineEdit.text(),
                'ring': ring_lineEdit.text(),
                'gitti': gitt_lineEdit.text(),
                'maurang': maurang_lineEdit.text()
                }
            
            # Write the updated configuration to a file
            with open('./Main_Software/config.ini', 'w') as config_file:
                self.config.write(config_file)
            # print(cement,"   ",maurang,"   ",gitti)
            #Storeing details in bottom label 
            def calculate_total(label_calc, line_edit_total, value, line_edit, calc_total, unit):
                if value is not None and line_edit is not None and line_edit.text() not in ["",".","-","+"]:
                    calc = line_edit.text()
                    label_calc.setText("{:.1f}".format((value)) + " " + unit)
                    line_edit_total.setText("{:.0f}".format(float(value) * float(calc)))
                    calc_total += (float(value) * float(calc))
                else:
                    label_calc.setText("")
                    line_edit_total.setText("")

                return int(calc_total)


            calc_total = 0  # Initialize calc_total before calling calculate_total

            calc_total = calculate_total(self.label_cem_calc, self.lineEdit_cement_total, cement, cem_lineEdit, calc_total,"bag")
            calc_total = calculate_total(self.label_mau_calc, self.lineEdit_maurang_total, maurang, maurang_lineEdit, calc_total,"Trali")
            calc_total = calculate_total(self.label_git_calc, self.lineEdit_gitti_total, gitti, gitt_lineEdit, calc_total,"Trali")
            calc_total = calculate_total(self.label_sariya_calc, self.lineEdit_sariya_total, sariya, sariya_lineEdit, calc_total,"kg")

                
            #For ring details
            no_of_ring = self.lineEdit_no_of_ring
            if (no_of_ring is not None and no_of_ring.text() != "" and ring_lineEdit is not None and ring_lineEdit.text() not in ["",".","-","+"]):
                no_ring = no_of_ring.text()
                rin = ring_lineEdit.text()
                self.label_ring_calc.setText(str(int(no_ring))+" rings")
                self.lineEdit_ring_total.setText(str(float(no_ring)*float(rin)))
                calc_total += (float(no_ring)*float(rin))
            else:
                self.label_ring_calc.setText("")
                self.lineEdit_ring_total.setText("")
            
            self.lineEdit_total.setText(str(calc_total))
        except Exception as e:
            print("Error:", e)
    def Labour_Record(self, combo_value=None, value=None):
        try:
            # Establish SQLite connection
            # mydb = sqlite3.connect('./Main_Software/mahendra.db')
            # mycursor = mydb.cursor()

            query = f"SELECT name, prod,quantity FROM product where date = '{self.todayDate}' order by time"
            # det = (value + '%',)
            # mycursor.execute(query,)
            # result = mycursor.fetchall()
            result = self.fn.select_db(query)
            self.tableWidget_labour.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_labour.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget_labour.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.tableWidget_labour.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tableWidget_labour.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
            
        except Exception as e:
            print("Error:", e)
