from PyQt6 import QtCore, QtGui, QtWidgets
from All_function import all_function
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QAction
from PyQt6.QtWidgets import (
    QTableWidgetItem,
    QMenu,
    QHeaderView,
    QApplication,
    QTableWidget,
)
from DialogBox_alltype import *
import datetime




class Ui_Stock(object):
    def setupUi(self, Stock):
        Stock.setObjectName("Stock")
        Stock.resize(1120, 793)
        Stock.setStyleSheet("QLabel {\n"
"    font-family: Russo One;\n"
"    font-size: 18px;\n"
"    border : 0px;\n"
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
"QDialog{\n"
"    background-color: rgb(242,240,247);\n"
"}\n"
"\n"
"QPushButton {\n"
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
"}\n"
"\n"
"#frame,#frame_2{\n"
"border: 2px solid #c0c0c0;\n"
"border-radius: 5px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Stock)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=Stock)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setStyleSheet("frame{\n"
"border: 2px  solid;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.method_label_9 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_9.setFont(font)
        self.method_label_9.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_9.setStyleSheet("")
        self.method_label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_9.setObjectName("method_label_9")
        self.verticalLayout.addWidget(self.method_label_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.comboBox_product = QtWidgets.QComboBox(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Belanosima")
        font.setPointSize(-1)
        self.comboBox_product.setFont(font)
        self.comboBox_product.setStyleSheet("QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-family: Belanosima;\n"
"    font-size: 18px;\n"
"    background-color: rgb(231, 255, 215);\n"
"}\n"
"")
        self.comboBox_product.setObjectName("comboBox_product")
        self.comboBox_product.addItem("")
        self.comboBox_product.addItem("")
        self.comboBox_product.addItem("")
        self.comboBox_product.addItem("")
        self.verticalLayout.addWidget(self.comboBox_product)
        self.lineEdit_quantity = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_quantity.setFont(font)
        self.lineEdit_quantity.setInputMask("")
        self.lineEdit_quantity.setText("")
        self.lineEdit_quantity.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_quantity.setObjectName("lineEdit_quantity")
        self.verticalLayout.addWidget(self.lineEdit_quantity)
        self.lineEdit_price = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setInputMask("")
        self.lineEdit_price.setText("")
        self.lineEdit_price.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.verticalLayout.addWidget(self.lineEdit_price)
        self.lineEdit_comment = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_comment.setFont(font)
        self.lineEdit_comment.setInputMask("")
        self.lineEdit_comment.setText("")
        self.lineEdit_comment.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.verticalLayout.addWidget(self.lineEdit_comment)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_submit = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_submit.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-submit-60.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_submit.setIcon(icon)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.verticalLayout.addWidget(self.pushButton_submit)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 2, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.method_label_11 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_11.setFont(font)
        self.method_label_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_11.setObjectName("method_label_11")
        self.gridLayout_2.addWidget(self.method_label_11, 0, 1, 1, 1)
        self.tableWidget_incoming_stock = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tableWidget_incoming_stock.setStyleSheet("QTableWidget {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #F7F7F7, stop:1 #E8E8E8);\n"
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
"}")
        self.tableWidget_incoming_stock.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.CurrentChanged|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget_incoming_stock.setWordWrap(True)
        self.tableWidget_incoming_stock.setObjectName("tableWidget_incoming_stock")
        self.tableWidget_incoming_stock.setColumnCount(6)
        self.tableWidget_incoming_stock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_incoming_stock.setHorizontalHeaderItem(5, item)
        self.tableWidget_incoming_stock.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget_incoming_stock, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=Stock)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.method_label_12 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_12.setFont(font)
        self.method_label_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_12.setObjectName("method_label_12")
        self.gridLayout_3.addWidget(self.method_label_12, 0, 1, 1, 1)
        self.tableWidget_outgoing_stock = QtWidgets.QTableWidget(parent=self.frame_4)
        self.tableWidget_outgoing_stock.setStyleSheet("QTableWidget {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                      stop:0 #F7F7F7, stop:1 #E8E8E8);\n"
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
"}")
        self.tableWidget_outgoing_stock.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.CurrentChanged|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget_outgoing_stock.setWordWrap(True)
        self.tableWidget_outgoing_stock.setObjectName("tableWidget_outgoing_stock")
        self.tableWidget_outgoing_stock.setColumnCount(5)
        self.tableWidget_outgoing_stock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_outgoing_stock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_outgoing_stock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_outgoing_stock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_outgoing_stock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_outgoing_stock.setHorizontalHeaderItem(4, item)
        self.tableWidget_outgoing_stock.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableWidget_outgoing_stock, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_2.setStyleSheet("#label_cement, #label_gitti, #label_maurang, #label_sariya\n"
"{\n"
"color: red;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.method_label_4 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_4.setFont(font)
        self.method_label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_4.setObjectName("method_label_4")
        self.gridLayout.addWidget(self.method_label_4, 4, 0, 1, 1)
        self.label_maurang = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_maurang.setFont(font)
        self.label_maurang.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_maurang.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_maurang.setObjectName("label_maurang")
        self.gridLayout.addWidget(self.label_maurang, 4, 1, 1, 1)
        self.method_label_2 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_2.setFont(font)
        self.method_label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_2.setObjectName("method_label_2")
        self.gridLayout.addWidget(self.method_label_2, 2, 0, 1, 1)
        self.label_sariya = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_sariya.setFont(font)
        self.label_sariya.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_sariya.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sariya.setObjectName("label_sariya")
        self.gridLayout.addWidget(self.label_sariya, 2, 1, 1, 1)
        self.label_cement = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_cement.setFont(font)
        self.label_cement.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_cement.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cement.setObjectName("label_cement")
        self.gridLayout.addWidget(self.label_cement, 1, 1, 1, 1)
        self.method_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label.setFont(font)
        self.method_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label.setObjectName("method_label")
        self.gridLayout.addWidget(self.method_label, 1, 0, 1, 1)
        self.method_label_3 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_3.setFont(font)
        self.method_label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_3.setObjectName("method_label_3")
        self.gridLayout.addWidget(self.method_label_3, 3, 0, 1, 1)
        self.label_gitti = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.label_gitti.setFont(font)
        self.label_gitti.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_gitti.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gitti.setObjectName("label_gitti")
        self.gridLayout.addWidget(self.label_gitti, 3, 1, 1, 1)
        self.method_label_10 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(-1)
        self.method_label_10.setFont(font)
        self.method_label_10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.method_label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.method_label_10.setObjectName("method_label_10")
        self.gridLayout.addWidget(self.method_label_10, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 2, 1)
        self.verticalLayout_2.addWidget(self.frame_4)

        self.retranslateUi(Stock)
        QtCore.QMetaObject.connectSlotsByName(Stock)

    def retranslateUi(self, Stock):
        _translate = QtCore.QCoreApplication.translate
        Stock.setWindowTitle(_translate("Stock", "STOCK"))
        self.method_label_9.setText(_translate("Stock", "STOCK Entry"))
        self.comboBox_product.setItemText(0, _translate("Stock", "Cement"))
        self.comboBox_product.setItemText(1, _translate("Stock", "Gitti"))
        self.comboBox_product.setItemText(2, _translate("Stock", "Maurang"))
        self.comboBox_product.setItemText(3, _translate("Stock", "Sariya"))
        self.lineEdit_quantity.setPlaceholderText(_translate("Stock", "Quantity"))
        self.lineEdit_price.setPlaceholderText(_translate("Stock", "Price"))
        self.lineEdit_comment.setPlaceholderText(_translate("Stock", "Comment"))
        self.pushButton_submit.setText(_translate("Stock", "Submit"))
        self.method_label_11.setText(_translate("Stock", "Incoming STOCK Details"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(0)
        item.setText(_translate("Stock", "Date"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(1)
        item.setText(_translate("Stock", "Product"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(2)
        item.setText(_translate("Stock", "Quantity"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(3)
        item.setText(_translate("Stock", "Price"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(4)
        item.setText(_translate("Stock", "Comment"))
        item = self.tableWidget_incoming_stock.horizontalHeaderItem(5)
        item.setText(_translate("Stock", "Time"))
        self.method_label_12.setText(_translate("Stock", "Outgoing STOCK Details"))
        item = self.tableWidget_outgoing_stock.horizontalHeaderItem(0)
        item.setText(_translate("Stock", "Date"))
        item = self.tableWidget_outgoing_stock.horizontalHeaderItem(1)
        item.setText(_translate("Stock", "Gitti"))
        item = self.tableWidget_outgoing_stock.horizontalHeaderItem(2)
        item.setText(_translate("Stock", "Cement"))
        item = self.tableWidget_outgoing_stock.horizontalHeaderItem(3)
        item.setText(_translate("Stock", "Maurang"))
        item = self.tableWidget_outgoing_stock.horizontalHeaderItem(4)
        item.setText(_translate("Stock", "Sariya"))
        self.method_label_4.setText(_translate("Stock", "Maurang"))
        self.label_maurang.setText(_translate("Stock", "35000"))
        self.method_label_2.setText(_translate("Stock", "Sariya"))
        self.label_sariya.setText(_translate("Stock", "35000"))
        self.label_cement.setText(_translate("Stock", "35000"))
        self.method_label.setText(_translate("Stock", "Cement"))
        self.method_label_3.setText(_translate("Stock", "Gitti"))
        self.label_gitti.setText(_translate("Stock", "35000"))
        self.method_label_10.setText(_translate("Stock", "Remaining STOCK"))


############################# Main Code ########################################
        screen_height = QApplication.primaryScreen().availableGeometry().height() - 30
        Stock.resize(840+100, screen_height)
        font = QtGui.QFont()
        font.setPointSize(11) 
        self.tableWidget_incoming_stock.setFont(font)
        self.tableWidget_outgoing_stock.setFont(font)
        self.tableWidget_incoming_stock.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget_outgoing_stock.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tableWidget_incoming_stock.setAlternatingRowColors(True)
        self.tableWidget_outgoing_stock.setAlternatingRowColors(True)
        self.tableWidget_incoming_stock.setColumnHidden(5, True)
        regex = QRegularExpression("^([+-]?\\d*\\.\\d+)$|^a$")
        validator = QRegularExpressionValidator(regex)
        self.lineEdit_price.setValidator(validator)
        self.lineEdit_quantity.setValidator(validator)
        self.tableWidget_incoming_stock.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidget_incoming_stock.customContextMenuRequested.connect(self.show_context_menu)
        self.today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.fn = all_function()
        self.show_table()
        self.pushButton_submit.clicked.connect(self.stock_entry)

    def show_context_menu(self, position):
        row = self.tableWidget_incoming_stock.currentRow()
        context_menu = QMenu()
        delete_date = QAction("Delete")
        delete_date.triggered.connect(lambda: self.Delete_stock_Data(row))
        context_menu.addAction(delete_date)
        context_menu.exec(self.tableWidget_incoming_stock.viewport().mapToGlobal(position))

    def Delete_stock_Data(self,row):
        date = self.tableWidget_incoming_stock.item(row,0).text()
        time = self.tableWidget_incoming_stock.item(row,5).text()
        print(date, time)
        print(time)
        result = DialogBox.show_yes_no_dialog( "Are you sure you want to delete all record of date?")        
        if result == False:
            return
        query = "DELETE FROM stock_table WHERE date = ? and time = ?"
        val = (date,time)
        fn = all_function()
        fn.insert_db(query, val)
        self.tableWidget_incoming_stock.clearContents()
        self.tableWidget_outgoing_stock.clearContents()
        # self.entry()
        self.show_table()
        
    def remaining_stock_data(self):
        stock_quantity = self.fn.select_db("select sum(Quantity) from Stock_table GROUP BY Product_desc")
        cement_rem = stock_quantity[0][0]  - self.fn.select_db("select sum(quantity) from product where prod like '%cement%'")[0][0]
        gitti_rem = stock_quantity[1][0] - self.fn.select_db("select sum(quantity) from product where prod like '%gitti%'")[0][0]
        maurang_rem = stock_quantity[2][0] - self.fn.select_db("select sum(quantity) from product where prod like '%maurang%'")[0][0]
        sariya_rem = stock_quantity[3][0] - self.fn.select_db("select sum(quantity) from product where prod like '%sariya%'")[0][0]
        # print(cement_rem, gitti_rem, maurang_rem, sariya_rem)
        self.label_cement.setText(str("{:.1f}".format(cement_rem)))
        self.label_gitti.setText(str("{:.1f}".format(gitti_rem)) + " ft")
        self.label_maurang.setText(str("{:.1f}".format(maurang_rem)) + " ft")
        self.label_sariya.setText(str("{:.1f}".format(sariya_rem) + " kg"))

    def today_sale(self):
        
        # sale order return as [gitti, cement, maurang, sariya]
        today_sale = self.fn.select_db(f"""SELECT
                        SUM(CASE WHEN prod LIKE '%gitti%' THEN quantity ELSE 0 END) AS gitti_sum,
                        SUM(CASE WHEN prod LIKE '%cement%' THEN quantity ELSE 0 END) AS cement_sum,
                        SUM(CASE WHEN prod LIKE '%maurang%' THEN quantity ELSE 0 END) AS maurang_sum,
                        SUM(CASE WHEN prod LIKE '%sariya%' THEN quantity ELSE 0 END) AS sariya_sum
                        FROM product
                        WHERE (prod LIKE '%gitti%' OR prod LIKE '%cement%' OR prod LIKE '%maurang%' OR prod LIKE '%sariya%')
                        and date = '{self.today_date}'"""
            )
        return today_sale
        
    def profit_loss(self):
        #per unit price order [cement, gitti, maurang, sariya]
        per_unit_price = self.fn.select_db(f"select sum(Rate)/sum(quantity) from stock_table group by product_desc")
        print(per_unit_price)
        today_sale = list(self.today_sale()[0])
        for i in range(4):
            if today_sale[i] == None:
                today_sale[i] = 0
        print(today_sale)
        cement_profit =  per_unit_price[0][0] * today_sale[1]
        sariya_profit = per_unit_price[3][0] * today_sale[3]
        gitti_profit = per_unit_price[1][0] * today_sale[0]
        maurang_profit = per_unit_price[2][0] * today_sale[2]
        print(cement_profit, sariya_profit, gitti_profit, maurang_profit)
        total_profit = cement_profit + sariya_profit + gitti_profit + maurang_profit
        print(total_profit)
        check_profit_date = self.fn.select_db(f"select profit from Profit_table where date = '{self.today_date}'")
        if  len(check_profit_date) == 0:
            self.fn.insert_db(f"insert into Profit_table values(?,?)",(self.today_date, total_profit))
        else:
            self.fn.insert_db(f"update Profit_table set profit = ? where date = ?",(total_profit, self.today_date))
        print(check_profit_date) 
        
    def show_table(self):
        try:
            incoming_data = self.fn.select_db("SELECT * FROM stock_table ORDER BY date desc,time desc limit 1000")
            self.tableWidget_incoming_stock.setRowCount(0)
            for row_number, row_data in enumerate(incoming_data):
                self.tableWidget_incoming_stock.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if isinstance(data, float):  # Check if data is a float
                        formatted_data = "{:.0f}".format(data)
                        self.tableWidget_incoming_stock.setItem(
                            row_number, column_number, QTableWidgetItem(formatted_data)
                        )
                    else:
                        self.tableWidget_incoming_stock.setItem(
                            row_number, column_number, QTableWidgetItem(str(data))
                        )
            
            outgoing_data = self.fn.select_db("""SELECT
                        strftime('%d-%m-%Y', date),
                        SUM(CASE WHEN prod LIKE '%gitti%' THEN quantity ELSE 0 END) AS gitti_sum,
                        SUM(CASE WHEN prod LIKE '%cement%' THEN quantity ELSE 0 END) AS cement_sum,
                        SUM(CASE WHEN prod LIKE '%maurang%' THEN quantity ELSE 0 END) AS maurang_sum,
                        SUM(CASE WHEN prod LIKE '%sariya%' THEN quantity ELSE 0 END) AS sariya_sum
                        FROM product
                        WHERE prod LIKE '%gitti%' OR prod LIKE '%cement%' OR prod LIKE '%maurang%' OR prod LIKE '%sariya%'
                        GROUP BY date ORDER by date desc limit 1000"""
            )
            self.tableWidget_outgoing_stock.setRowCount(0)
            for row_number, row_data in enumerate(outgoing_data):
                self.tableWidget_outgoing_stock.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if isinstance(data, float):  # Check if data is a float
                        formatted_data = "{:.0f}".format(data)  # Format with 2 decimal places
                        self.tableWidget_outgoing_stock.setItem(
                            row_number, column_number, QTableWidgetItem(formatted_data)
                        )
                    else:
                        self.tableWidget_outgoing_stock.setItem(
                            row_number, column_number, QTableWidgetItem(str(data))
                        )
            
            self.tableWidget_outgoing_stock.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch)

        ######
            # self.profit_loss()
            self.remaining_stock_data()
        except Exception as e:
            print(e)
            
    def stock_entry(self):
        try:
            product = self.comboBox_product.currentText()
            quantity = self.lineEdit_quantity.text()
            price = self.lineEdit_price.text()
            comment = self.lineEdit_comment.text()
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            if quantity in ["-",".","+",""] or price == ["-",".","+",""]:
                self.dialog = DialogBox()
                self.dialog.show_warning_dialog("Please Fill All Fields Correctly")
            else:
                self.fn.insert_db(
                    f"""INSERT INTO stock_table (Date, Product_desc, Quantity, Rate, Comment,time)
                    VALUES (?,?,?,?,?,?);""",(date, product, quantity, price, comment,time)
                )
                print(product, quantity, price, comment, date,time)
                # self.dialog = DialogBox("Stock Entry Successfully")
                # self.dialog.s()
                self.lineEdit_quantity.clear()
                self.lineEdit_price.clear()
                self.lineEdit_comment.clear()
                self.show_table()
        except Exception as e:
            print(e)


# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     Stock = QtWidgets.QDialog()
#     ui = Ui_Stock()
#     ui.setupUi(Stock)
#     Stock.show()
#     sys.exit(app.exec())
