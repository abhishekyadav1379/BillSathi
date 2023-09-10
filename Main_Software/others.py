from PyQt6 import QtCore, QtGui, QtWidgets
from All_function import all_function



class Ui_Others(object):
    def setupUi(self, Others):
        Others.setObjectName("Others")
        Others.resize(1098, 696)
        Others.setStyleSheet("QPushButton {\n"
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
"QTextEdit {\n"
"                background-color: #f3f3f3;\n"
"                border: 2px solid #c0c0c0;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                selection-background-color: #a8a8a8;\n"
"            }\n"
"\n"
"            QTextEdit:focus {\n"
"                border: 2px solid #707070;\n"
"                background-color: #ffffff;\n"
"            }")
        self.gridLayout = QtWidgets.QGridLayout(Others)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_query = QtWidgets.QTextEdit(parent=Others)
        self.textEdit_query.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_query.setFont(font)
        self.textEdit_query.setObjectName("textEdit_query")
        self.gridLayout.addWidget(self.textEdit_query, 0, 0, 1, 1)
        self.pushButton_ok = QtWidgets.QPushButton(parent=Others)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout.addWidget(self.pushButton_ok, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=Others)
        font = QtGui.QFont()
        font.setFamily("Belanosima")
        font.setPointSize(-1)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    font-family: Belanosima;\n"
"    font-size: 18px;\n"
"    background-color: rgb(231, 255, 215);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=Others)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.retranslateUi(Others)
        QtCore.QMetaObject.connectSlotsByName(Others)

    def retranslateUi(self, Others):
        _translate = QtCore.QCoreApplication.translate
        Others.setWindowTitle(_translate("Others", "Others"))
        self.textEdit_query.setPlaceholderText(_translate("Others", "Write your Query here..."))
        self.pushButton_ok.setText(_translate("Others", "ok"))
        self.comboBox.setItemText(0, _translate("Others", "Max Udhari"))
        self.comboBox.setItemText(1, _translate("Others", "Annual record"))
        self.comboBox.setItemText(2, _translate("Others", "VIP Customer"))
        self.comboBox.setItemText(3, _translate("Others", "Custom"))

######################## My Code  ############################

        self.pushButton_ok.clicked.connect(self.add_values_to_table)
        self.comboBox.activated.connect(self.combo_selection)
        self.textEdit_query.setReadOnly(True)
        
        self.fn = all_function()
        self.query = "select Customer.id,Customer.name,customer.address, sum(total -give) as new_total from money,Customer where customer.id = money.id group by Customer.id order by new_total DESC"
        self.add_values_to_table()
        # self.column_name = ["dsf"]
    
    def combo_selection(self):
        self.column_name = []
        selected_Value = self.comboBox.currentText()
        self.textEdit_query.setText("")
        if selected_Value == "Max Udhari":
            self.column_name = ["id","name","Address","total"]
            self.query = f"select Customer.id,Customer.name,customer.address, sum(total -give) as new_total from money,Customer where customer.id = money.id group by Customer.id order by new_total DESC"
        elif selected_Value == "Annual record":
            self.column_name = ["year","Remianing","total_sum"]
            self.query = '''SELECT substr(date, 0, 5) AS year,sum(total) - sum(Give) as udhari, SUM(total) AS total_sum
                            FROM Money
                            GROUP BY year
                            ORDER BY year;'''
        elif selected_Value == "VIP Customer":
            self.column_name = ["id","name","total"]
            self.query =  "select id, name, sum(total) as new_total from money group by id order by new_total DESC"
        elif selected_Value == "Custom":
            self.textEdit_query.setReadOnly(False)
        self.tableWidget.setHorizontalHeaderLabels(self.column_name)
        self.add_values_to_table()
        # elif selected_Value == "Best Area":
        
            
        # print(selected_Value)
    def add_values_to_table(self):
        # self.query = "select * from Customer"
        self.result = self.fn.select_db(self.query)
        matrix_data = self.result
        input_query = self.textEdit_query.toPlainText()
        if input_query != "":
            self.column_name = []
            self.result = self.fn.select_db(input_query)
            matrix_data = self.result
        # Sample matrix data
        # self.column_name= ['Column A', 'Column B', 'Column C']

        # Set the number of rows and columns in the table
        rows = len(matrix_data)
        if rows == 0:
            matrix_data.append(["No Data Found"])
            rows = len(matrix_data)
            # matrix_data = [["No Data Found"]]
            # return
        cols = len(matrix_data[0])
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        # Set custom column names
        # self.tableWidget.setHorizontalHeaderLabels(self.column_name)

        # Add data to the table
        for row_idx, row_data in enumerate(matrix_data):
            for col_idx, cell_value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_value))
                self.tableWidget.setItem(row_idx, col_idx, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Others = QtWidgets.QDialog()
    ui = Ui_Others()
    ui.setupUi(Others)
    Others.show()
    sys.exit(app.exec())
