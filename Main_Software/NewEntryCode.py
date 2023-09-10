from PyQt6 import QtWidgets
from EntryGUI_ui import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QCompleter, QLineEdit, QWidget, QApplication, QVBoxLayout, QTableWidget, QItemDelegate,
                             QHeaderView, QStyledItemDelegate, QTableWidgetItem, QMainWindow, QMessageBox, QPushButton,QDialog)
from PyQt6.QtCore import Qt,QTimer,QStringListModel,QThread, pyqtSignal, QDate, QDateTime
from PyQt6.QtGui import QFont, QPalette, QColor, QDoubleValidator
from All_function import all_function
from pdf_create import *
from DialogBox_alltype import *
import datetime
from DialogBox_alltype import *
import speech_recognition as sr
from datetime import datetime
from ReturnCombo import Ui_ReturnGUI
import webbrowser
import Invoice_generator
from printer import PrinterManager
                
class FloatOrAValidator(QtGui.QValidator):
    def validate(self, input_str, pos):
        if input_str == '' or input_str == "-" or input_str == ".":
            return QtGui.QValidator.State.Acceptable, input_str, pos
        double_validator = QDoubleValidator()
        state, input_str, pos = double_validator.validate(input_str, pos)
        if state == QtGui.QValidator.State.Acceptable:
            return QtGui.QValidator.State.Acceptable, input_str, pos
        return QtGui.QValidator.State.Invalid, input_str, pos


class FloatOrADelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        validator = FloatOrAValidator(parent)
        editor.setValidator(validator)
        return editor

# This is for Completer in table widget


class CaseInsensitiveCompleter(QCompleter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)


class CompleterDelegate(QStyledItemDelegate):
    def __init__(self, suggestions, parent=None):
        super().__init__(parent)
        self.completer = CaseInsensitiveCompleter(suggestions)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setCompleter(self.completer)
        return editor

    
class NewEntry(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Entry_Window()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
#-----------------Main Code---------------------------------#
        #Variables
        self.submit_btn_pressed = 0
        self.cust_entry = 0
        self.overall_rem = 0
        self.checkBox_value = ""
        self.default_cust_id = ""
        self.edit_entry_check = 0
        self.table_value_check = 0
        self.old_rem_value = 0
        self.overall_rem_during_edit = 0
        self.last_date = ""  #It is used to in delete data 
        self.last_time = ""
        self.name_completer = []
        
        self.completer = QCompleter()
        self.ui.lineEdit_name.setCompleter(self.completer)
        self.fn = all_function()
        self.ui_changes()
        
        self.ui.pushButton_submit.clicked.connect(self.submit)
        self.ui.tableWidget.currentCellChanged.connect(self.cell_enable)
        self.ui.tableWidget.cellChanged.connect(self.cell_changed)
        self.ui.lineEdit_giving.setValidator(QDoubleValidator())
        #Completer for table
        all_item = ["Cement","Cement JK Super","Cement Ultratech","Cement Wonder","Cement shree", "Gitti","Gitti 10mm","Gitti 20mm",
                    "Maurang","Maurang moti", "Maurang medium","Maurang Plaster", 
                    "Sariya", "Sariya 6mm", "Sariya 8mm","Sariya 10mm", "Sariya 12mm", "Sariya 16mm","Sariya 20mm",
                    "Fan Box","Tar","Tar Tata","Tractor Bhada","Pichla Baki","Labour unloading","Blade",
                    "PVC Pipe","PVC Band","Band","LED Box","Water proofing","Cover Block",
                    "Rings","Rings 7*7", "Rings 7*3", "Rings 7*10", "Rings 7*12"]
        completer_delegate = CompleterDelegate(
            all_item, self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(0, completer_delegate)

        #To enter only float value in table
        delegate = FloatOrADelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(1, delegate)
        self.ui.tableWidget.setItemDelegateForColumn(2, delegate)
        
        #time and date
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)
        self.update_time() # Set the initial time
        # self.edit()

        self.ui.lineEdit_id.textChanged.connect(self.details_from_id)
        self.ui.comboBox_cash.currentIndexChanged.connect(self.combo_box)
        self.ui.lineEdit_giving.textChanged.connect(self.update_reaming)
        self.ui.pushButton_print.clicked.connect(self.print_invoice)
        self.ui.checkBox_return.clicked.connect(self.checkBoxCode)
        self.ui.tableWidget.itemChanged.connect(self.table_item_changed)
        self.ui.dateEdit.dateChanged.connect(self.on_date_changed)
        self.ui.lineEdit_name.textEdited.connect(self.on_text_edited)
        self.ui.lineEdit_address.textEdited.connect(self.on_text_edited)
        self.ui.lineEdit_name.editingFinished.connect(lambda: self.on_text_finished(self.ui.lineEdit_name))
        self.ui.lineEdit_address.editingFinished.connect(lambda: self.on_text_finished(self.ui.lineEdit_address))
        self.ui.pushButton_telegram.clicked.connect(self.send_image_to_telegram)
        self.completer.activated.connect(self.on_completer_activated_or_clicked)
        
        self.last_date = self.ui.date_label.text()
        print(self.last_date)
    def ui_changes(self):
        
        self.hide_Table()
        self.make_cell_editable(self.ui.tableWidget, 0, 0)
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.dateEdit.setDate(QDate.currentDate())
        # self.last_date = QDate.currentDate().toString('dd-MM-yyyy')
        self.set_Cust_id()
        self.ui.dateEdit.setCalendarPopup(True)
        self.filled_value_in_name_completer()
    
    def filled_value_in_name_completer(self):
        fn = all_function()
        value = fn.select_db(f'''select customer.name,address, Phone, Customer.id from customer,Money
                             where customer.ID = Money.ID and (Money.method = 'Udhar' or Money.method = 'Jma') 
                             group by Customer.id''')
        for data in value:
            self.name_completer.append(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}")
        completer_model = QStringListModel(self.name_completer,self.completer)
        self.completer.setModel(completer_model)
        # self.name_completer
        # print(value)
    
    def on_completer_activated_or_clicked(self, text):
        cust_det = text.split(",")
        print(cust_det)
        def invoke_set_input():
            # self.ui.lineEdit_name.setText(cust_det[0].strip())
            # self.ui.lineEdit_address.setText(cust_det[1].strip())
            # self.ui.lineEdit_phone.setText(cust_det[2].strip())
            self.ui.lineEdit_id.setText(cust_det[3].strip())
        timer = QTimer(self)
        timer.singleShot(100, lambda: invoke_set_input())
        # self.ui.line
        
    def on_text_finished(self, lineEdit):
        text = lineEdit.text()
        trans = self.fn.translate_text( text)
        self.ui.note_label.setText(trans)
        
    id_selection = 0 
    # def on_text_edited(self):
    def on_text_edited(self, text):
        sender = self.sender()
        if len(text) > 1:
            return
        # print(text)
        if text and self.id_selection == 0:
            # Capitalize the first letter and update the text
            capitalized_text = text[0].upper() + text[1:]
            if sender == self.ui.lineEdit_name:
                self.ui.lineEdit_name.setText(capitalized_text)
            elif sender == self.ui.lineEdit_address:
                self.ui.lineEdit_address.setText(capitalized_text)
        # pass
        self.ui.lineEdit_id.setText(self.default_cust_id)
        self.ui.lineEdit_id.setReadOnly(True)
            
    # To make all table cell ueditable
    def hide_Table(self):
        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                item = QTableWidgetItem()
                self.ui.tableWidget.setItem(row, column, item)
                if item.text() == '':
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
        
    def cust_Details(self):
        name = self.ui.lineEdit_name.text() or ""
        id = self.ui.lineEdit_id.text() or ""
        phone = self.ui.lineEdit_phone.text() or ""
        addr = self.ui.lineEdit_address.text() or ""
        if name == "" or addr == "":
            DialogBox.show_warning_dialog("Pleaseui. Enter Name and Address")
            return []
        return [name, addr, phone, id]
    #Print invoice
    def print_invoice(self):
        id = self.ui.lineEdit_id.text() or " "
        name = self.ui.lineEdit_name.text() or " "
        addr = self.ui.lineEdit_address.text() or " "
        phone = self.ui.lineEdit_phone.text() or " "    
        date = self.ui.date_label.text() or " "
        time = self.ui.time_label.text() or " "
        total = self.ui.lineEdit_total.text() or "0"
        giving = self.ui.lineEdit_giving.text() or "0"
        method = self.ui.comboBox_cash.currentText() or " "
        remaining = self.ui.lineEdit_remaining.text() or "0"
        date = date + " " + time
        if method == "Udhar/Jma":
            if float(giving)>0:
                method = "Jma"
            else:
                method = "Udhar"  
        table = self.table_Data()
        # table.insert(0,["Description","Qty","Rate","Amount"])
        table.append(["","","कुल",total])
        # InvoicePdf.generate_invoice(id, name, addr, phone, table,date,time, method, giving, total,remaining)
        Invoice_generator.InvoiceGenerator.generate_invoice_pdf(id, name, addr, phone, date,table, method, total, giving, remaining)
        fn = all_function()
        fn.convert_pdf_to_image("./Main_Software/Image_pdf/Invoice.pdf")
        PrinterManager.print_image("Everycom-80-Series", "./Main_Software/Image_pdf/invoice.png")
        self.submit()
        print("prnt complete")
        # self.open_pdf_in_default_browser()
        
    def open_pdf_in_default_browser(self):
        try:
            pdf_path = "Main_Software/Invoice.pdf"
            webbrowser.open(pdf_path, new=2)
        except Exception as e:
            print("Error:", e)
        
    def set_Cust_id(self):
        try:
            fn = all_function()
            result = fn.select_db("SELECT * FROM Id_table")[0]
            table_date = result[0]
            table_id = result[1]
            self.ui.lineEdit_id.setReadOnly(False)
            today_date = QDate.currentDate().toString("yyyy-MM-dd")
            if table_date != today_date:
                fn.insert_db("UPDATE Id_table set DATE = ?, ID = ? WHERE ID = ?", (today_date, '01', table_id))
            
            number = fn.select_db("SELECT ID FROM Id_table")[0][0]
            number = str('{:02}'.format(int(number)))
            formate_date = QDate.currentDate().toString("yyMMdd")
            id = formate_date+str(number)
            self.default_cust_id = id
            self.ui.lineEdit_id.setText(id)
            
        except Exception as e:
            print(f"Error in set_Cust_id {e}")
        
    def details_from_id(self):
        id = self.ui.lineEdit_id.text()
        if len(id) == 8 or len(id) == 3:
            result = self.fn.select_db(f"select * from customer where id = '{id}'")
            if len(result) == 0:
                return
            self.cust_entry = 1
            # self.id_selection = 1
            # print("check prev overall rem " + str(self.overall_rem))
            self.overall_rem = self.fn.select_db(f"select sum(total) - sum(give) from money where id = '{id}'")[0][0]
            self.overall_rem_during_edit = self.overall_rem
            print(f"overall rem {self.overall_rem}")
            # if self.edit_entry_check == 1:
            #     self.overall_rem -= float(self.ui.lineEdit_giving.text())
                # self.overall_rem +=  float(self.old_rem_value )
                # print(f"entry value check and passed {self.overall_rem} old_rem_Value {self.old_rem_value} ")
            # self.ui.lineEdit_remaining.setText(str(self.overall_rem))
            self.combo_box()
            # self.overall_total()
            result = self.fn.select_db(f"select * from customer where id = '{id}'")[0]
            id, name,phone,addr = result
            self.ui.lineEdit_name.setText(name)
            self.ui.lineEdit_phone.setText(phone)
            self.ui .lineEdit_address.setText(addr)
    #----------------------Cell enable-------------------------# 
    def make_cell_editable(self, table_widget: QTableWidget, row: int, column: int):
        item = table_widget.item(row, column)
        if item is not None:
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEnabled)

    # to enable cell
    def cell_enable(self, c_row, c_column, p_row, p_col):
        if c_column < 2:
            row = c_row
            column = c_column + 1
            self.make_cell_editable(self.ui.tableWidget, row, column)
        elif c_column == 2:
            row = c_row+1
            column = 0
            self.make_cell_editable(self.ui.tableWidget, row, column)
    
    #It return sum of value column
    def overall_total(self):
        total = 0
        for i in range(15):
            item = self.ui.tableWidget.item(i, 3)
            if item is not None and item.text() != "":
                total = total + float(item.text())
        self.ui.lineEdit_total.setText(str(total))
        # self.ui.lineEdit_giving.setText(str(total))
        return total
            
    #For total and value calcualte
    def value_update(self, row, column):
        try:
            col1 = self.ui.tableWidget.item(row, 1)
            col2 = self.ui.tableWidget.item(row, 2)
            if col1 is None or col1.text() == "":
                return
            
            if col2 is not None and col2.text() != "":
                value1,value2 = float(col1.text()), float(col2.text())
                result = value1 * value2
                result = round(result)
                col_value = QTableWidgetItem(str(result))
                font = col_value.font()
                font.setBold(True)
                col_value.setFont(font) 
                col_value.setForeground(QtGui.QColor("red"))
                self.ui.tableWidget.setItem(row, 3, col_value)
                # total = self.overall_total()

                item = self.ui.tableWidget.item(row,3)
                if item is None:
                    item = QTableWidgetItem()
                    self.ui.tableWidget.setItem(row, 3, item)
                #To make uneditable the cell
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)   
                self.combo_box()
            
        except Exception as e:
            
            print(f"Error in value update {e}")
    
    # To fill remaing total       
    def update_reaming(self):
        # self.overall_rem = self.fn.select_db(f"select sum(total - give) as rem from money where id = '{id}'")[0][0] or "0"
        # print(f"new over all is {self.overall_rem}")
        # if self.edit_entry_check == 1:
            
        #     return
        if self.ui.lineEdit_giving.text() == "" or self.ui.lineEdit_total.text() == "":
            self.ui.lineEdit_remaining.setText(str(self.ui.lineEdit_total.text()))
            return
        total = float(self.ui.lineEdit_total.text())
        total = round(total,2)
        giving = self.ui.lineEdit_giving
        if giving is None or self.overall_rem is None or giving.text() == "":
            return
        giving = float(giving.text())
            
        remaining = float(self.overall_rem) + total - giving
        remaining = round(remaining,2)
        # if self.edit_entry_check == 1:
        #     remaining -= (total - giving)
        self.ui.lineEdit_remaining.setText(str(remaining))   
        
    def combo_box(self):
        mode = self.ui.comboBox_cash.currentText()   
        index = self.ui.comboBox_cash.currentIndex()
        total = self.ui.lineEdit_total
        give = self.ui.lineEdit_giving
        rem = self.ui.lineEdit_remaining
        # print(mode)
        self.ui.lineEdit_giving.setReadOnly(True)   
        if index == 0: #Cash
            give.setText(str(total.text()))
            # self.ui.lineEdit_giving.setText(str(self.ui.lineEdit_total.text()))
            self.ui.lineEdit_remaining.setText(str(self.overall_rem))
        elif index == 1: #Udhar/jma
            if total.text() == give.text():
                give.setText("0")
                # rem.setText(total.text())
            else:
                give.setText(str(give.text()))
            # self.ui.lineEdit_remaining.setText(str(self.ui.lineEdit_total.text()))
            # self.ui.lineEdit_giving.setText("0")
            self.ui.lineEdit_giving.setReadOnly(False)
            self.update_reaming()
        elif index == 2 or index == 3:
            self.ui.note_label.setText("कृपया दिए गए पैसे डाले।")
            self.ui.lineEdit_giving.setReadOnly(False)
            self.ui.lineEdit_giving.setText(str(self.ui.lineEdit_total.text()))
            self.ui.lineEdit_remaining.setText(str(self.overall_rem))
            self.update_reaming()
            # pass
            
    # fill value field coulumn
    def cell_changed(self, row, column):
        item = self.ui.tableWidget.item(row, column)
        if column == 0:
            if item is not None:
                # Set the font size and color for column 1
                font = QFont()
                font.setPointSize(15)
                item.setFont(font)
                item.setForeground(QColor("blue"))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        if column == 1:
            col1 = self.ui.tableWidget.item(row, 1)
            col2 = self.ui.tableWidget.item(row, 2)
            if col1.text() != "" and self.checkBox_value != "":
                text = col1.text()
                if text[0] != "-":
                    hyphenated_text = "-" + text
                    item.setText(hyphenated_text)
            if col1.text() != "" and col2.text() != "":
                self.value_update(row, column)
            else:
                col_value = QTableWidgetItem("")
                self.ui.tableWidget.setItem(row, 3, col_value)
            # self.overall_total()
        if column == 2:
            if item is None or item.text() == "":
                col_value = QTableWidgetItem("")
                self.ui.tableWidget.setItem(row, 3, col_value)
            self.value_update(row, column)
        self.overall_total()
            # self.ui.total_upadat(row, column)
    #it check table should fill perfectly
    def check_table(self):
        rows = self.ui.tableWidget.rowCount()
        cols = self.ui.tableWidget.columnCount()
        emp = 0
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.ui.tableWidget.item(row, col)
                if item is not None and item.text() != "":
                    row_data.append(item.text())
            if len(row_data) == 0:
                emp = 1
            if emp == 1 and len(row_data) != 0:
                return False
            if len(row_data) != 0  and len(row_data) <4:
                return False
        return True

    def table_Data(self):
        prod_values = []
        for row in range(self.ui.tableWidget.rowCount()):
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None and item.text() != "":
                    row_data.append(item.text())
            if len(row_data) > 3:
                prod_values.append(row_data)
        return prod_values
    #------------------------------------------------------------#
    
    #Update Time every second
    def update_time(self):
        current_date = QDate.currentDate()
        date_str = current_date.toString("dd-MM-yyyy")
        self.ui.date_label.setText(date_str)
        # self.last_date = date_str   
        
        current_time = QtCore.QTime.currentTime()
        time_str = current_time.toString("hh:mm:ss AP")
        self.ui.time_label.setText(time_str)
        
    #It count no. of customer and also useless
    def no_of_daily_customer(self):
        result = self.fn.select_db("SELECT COUNT(*) FROM CUSTOMER")[0][0]
        return result

    def insert_customer(self, cust_id, cust_name, phone, address):
        query = "INSERT INTO CUSTOMER(ID, Name, Phone, Address) VALUES (?, ?, ?, ?)"
        values = (cust_id, cust_name, phone, address)
        return self.fn.insert_db(query, values)
        

    def insert_product(self, cust_id, cust_name, date, desc, quantity,rate, value, method, gi_time):
        query = "INSERT INTO PRODUCT(ID, Name, date, prod, Quantity, Rate,  value, method, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (cust_id, cust_name, date, desc, quantity, rate, value, method, gi_time)
        return self.fn.insert_db(query, values)
        # if not result:
        #     return

    def insert_money(self, cust_id, date, cust_name, give, total, method, gi_time, comment):
        query = "INSERT INTO MONEY(ID, date, Name, Give, total, method, time, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        values = (cust_id, date, cust_name, give, total, method, gi_time, comment)
        return self.fn.insert_db(query, values)
        # if not result:
        #     return 
        
    def update_customer(self, cust_id, cust_name, phone, address):
        query = "UPDATE CUSTOMER SET Name = ?, Phone = ?, Address = ? WHERE ID = ?"
        values = (cust_name, phone, address, cust_id)

        return self.fn.insert_db(query, values)
        # if result is None:
        #     return
        # print("udpate check kiya")
    def warning_occur(self,msg,num = 0):
        DialogBox.show_warning_dialog(f"Error {msg} {num}")
        
    # def time_convert(self,time):
    #     return datetime.strptime(time, "%I:%M:%S %p").strftime("%H:%M:%S")
    
    def Insert_all_Record(self):
        try:
            cust_Details = self.cust_Details()
            name, addr, phone, id = cust_Details
            date, time = self.ui.date_label.text(), self.ui.time_label.text()
            method = self.ui.comboBox_cash.currentText()
            give,total = self.ui.lineEdit_giving.text() or "0", self.ui.lineEdit_total.text() or "0"
            table_data = self.table_Data()
            comment = self.ui.lineEdit_comment.text()
            fn = all_function()
            time = fn.time_convert(time)
            date = fn.date_convert_format(date)
            #check cusotmer details in 'customer' table or not
            # fn = all_function()
            check_Reocrd = fn.select_db(f"select id from customer where id = '{id}'")
            # print(check_Reocrd)
            
            if len(check_Reocrd) == 0:
                result = self.insert_customer(id, name, phone, addr)
                if result == "Error":
                    self.warning_occur(result,1)
                    return
                fn = all_function()
                number = int(fn.select_db("SELECT id from Id_table")[0][0])
                number+=1
                # print("id is updated")
                if self.datechanged == True:
                    fn.insert_db("update Id_table set id = ?",(number,))
                else:
                    fn.insert_db("update Id_table set id = ? where date = ?",(number,date))
                    
            else:
                result = self.update_customer(id, name, phone, addr)
                if result == "Error":
                    self.warning_occur(result,2)
                    return
                
            if method == "Udhar/Jma":
                if float(give)>0:
                    method = "Jma"
                else:
                    method = "Udhar"   
            #Insert Product Details
                
            if self.table_value_check == 1:
                self.Delete_record()
            
            self.last_time = time
            if len(table_data) == 0:
                if method != "Cash":
                    fn.insert_db(f"Insert into money(id, date, name, give, total, method, time, comment) values(?,?,?,?,?,?,?,?)",(id,date,name,give,total,method,self.last_time,"*"+comment))
                    self.ui.note_label.setText("Record Inserted Successfully")
                self.show_popup("Customer details are updated")
                return
            else:
                self.table_value_check = 1
            
            for data in table_data:
                desc, quantity, rate, value = data
                result = self.insert_product(id, name, date, desc,quantity, rate, value, method, self.last_time)
                if result == "Error":
                    self.warning_occur(result,3)
                    return
            #Insert Money Details
            if self.checkBox_value == "Cash":
                comment = "Money returned in cash" + comment
                # self.insert_money(id, date, name, give, total, method, time,comment)
            elif self.checkBox_value == "Udhar":
                give = "0"
                comment = "Return as Udhar" + comment
            result = self.insert_money(id, date, name, give, total, method, time,comment)
            if result == "Error":
                self.warning_occur(result,4)
                return
            
            self.show_popup("Record Inserted Successfully")
            # fn.show_popup("Record Inserted Successfully")
            self.ui.note_label.setText("Record Inserted Successfully")
            self.ui.main_label.setStyleSheet("color: green")
        except Exception as e:
            DialogBox.show_warning_dialog(f"Failed to insert \n{e}")
    
    def Delete_record(self):
        try:
            id = self.ui.lineEdit_id.text()
            date = self.last_date
            fn = all_function()
            date = fn.convert_date_format(date)
            # date = self.ui.date_label.text()
            if self.edit_entry_check == 1:
                last_time = self.ui.time_label.text()
                last_time = fn.time_convert(last_time)
            else:
                last_time = self.last_time
                # last_time = self.fn.select_db(f"SELECT time FROM PRODUCT WHERE ID = '{id}' and date = '{date}' ORDER BY time DESC LIMIT 1")[0][0]
                
            self.fn.insert_db("DELETE FROM PRODUCT WHERE ID = ? and date = ? and time = ?", (id,date,last_time))
            self.fn.insert_db("DELETE FROM MONEY WHERE ID = ? and date = ? and time = ?", (id,date,last_time))
            # self.Insert_all_Record()
        except Exception as e:
            DialogBox.show_warning_dialog(f"Failed to delete data \n{e}")
    
    
    #this funtion not yet working
    def Insert_Record_again(self):
        # if self.record_again_gate == 0:
        #     return
        try:
            id = self.ui.lineEdit_id.text()
            date = self.ui.date_label.text()
            if self.edit_entry_check == 1:
                last_time = self.ui.time_label.text()
            else:
                last_time = self.fn.select_db(f"SELECT time FROM PRODUCT WHERE ID = '{id}' and date = '{date}' ORDER BY time DESC LIMIT 1")[0][0]
            
            self.fn.insert_db("DELETE FROM PRODUCT WHERE ID = ? and date = ? and time = ?", (id,date,last_time))
            self.fn.insert_db("DELETE FROM MONEY WHERE ID = ? and date = ? and time = ?", (id,date,last_time))
            self.Insert_all_Record()
        except Exception as e:
            DialogBox.show_warning_dialog(f"Failed to insert InsertAgain \n{e}")
    
    def Edit_Record(self,id,name,addr,phone,table,date,time,method,give):
        self.default_cust_id = id   #! order matter here
        self.ui.lineEdit_id.setReadOnly(True)
        self.edit_entry_check = 1
        self.table_value_check = 1
        self.timer.start(2147483642)
        # fn = all_function()
        # date = fn.convert_date_format_ddmmyyyy(date)
        self.ui.date_label.setText(date)
        self.ui.time_label.setText(time)
        self.last_date = self.ui.date_label.text()
        
        self.ui.comboBox_cash.setCurrentText(method)
        self.ui.lineEdit_giving.setText(str(give))
        self.ui.lineEdit_name.setText(name)
        self.ui.lineEdit_address.setText(addr)
        self.ui.lineEdit_phone.setText(phone)
        for i in range(len(table)):
            for j in range(len(table[i])):
                item = QTableWidgetItem(str(table[i][j]))
                self.ui.tableWidget.setItem(i, j, item)
                if j == 3:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.setItem(i+1, 0, QTableWidgetItem(""))

        self.old_rem_value = float(self.ui.lineEdit_total.text())
        self.ui.lineEdit_id.setText(id)
        self.ui.lineEdit_remaining.setText(str(self.overall_rem_during_edit))
        self.overall_rem = self.overall_rem_during_edit - (float(self.ui.lineEdit_total.text()) - float(self.ui.lineEdit_giving.text()))
        # self.old_rem_value =  float(self.ui.lineEdit_total.text() )
    def checkBoxCode(self):
        if self.ui.checkBox_return.isChecked():
            gui = Ui_ReturnGUI()
            dialog = QDialog()
            gui.setupUi(dialog)
            # Connect the OK button signal to a custom slot
            def ok_clicked():
                if gui.radioButton_cash.isChecked():
                    self.checkBox_value = "Cash"
                elif gui.radioButton_udhar.isChecked():
                    self.checkBox_value = "Udhar"
                dialog.accept() 
            gui.buttonBox.accepted.connect(ok_clicked)
            gui.buttonBox.rejected.connect(lambda: dialog.reject())
            dialog.exec()
            if self.checkBox_value == "":
                self.ui.checkBox_return.setChecked(False)
                return
            self.checkBoxReturnArea()
        else:
            self.checkBox_value = ""
            self.ui.comboBox_cash.setItemText(0, "Cash")
            self.ui.comboBox_cash.setEnabled(True)
            for row in range(self.ui.tableWidget.rowCount()): 
                item = self.ui.tableWidget.item(row, 1)
                if item is not None and item.text() != "" and item.text()[0] == "-":
                    item.setText(item.text()[1:])
    
    def checkBoxReturnArea(self):
        self.ui.comboBox_cash.setItemText(0, "Return")
        self.ui.comboBox_cash.setEnabled(False)
        #Add -ve before the quantity
        for row in range(self.ui.tableWidget.rowCount()): 
            item = self.ui.tableWidget.item(row, 1)
            if item is not None and item.text() != "":
                item.setText("-"+item.text())
            
        
    def table_item_changed(self, item):
        if item.text() == "-":
            item.setText("-1")
        elif item.text() == ".":
            item.setText("0.")
            
    datechanged = False
    def on_date_changed(self):
        if self.datechanged == False:
            result = DialogBox.show_yes_no_dialog("Do you want to change date?")
            if result == False:
                return
            self.datechanged = True
        self.timer.start(2147483642)
        self.ui.date_label.setStyleSheet("color: red;")
        date = self.ui.dateEdit.date().toString("dd-MM-yyyy")
        self.ui.date_label.setText(date)
    
    #check record from cusotmer table when id is provided
    def new_cust_entry(self,id):
        self.cust_entry = 1
        id,name, phone,addr = self.fn.select_db(f"SELECT * FROM CUSTOMER WHERE ID = '{id}'")[0]
        
        self.default_cust_id = id
        self.ui.lineEdit_id.setText(id)
        self.ui.lineEdit_name.setText(name)
        self.ui.lineEdit_address.setText(addr)
        self.ui.lineEdit_phone.setText(phone)
        self.ui.lineEdit_id.setReadOnly(True)
    
    #This is used to store temperary data for testing  
    def edit(self):  
        fake_table = [["cement","5",5,25],["Rings",10,10,100]]
        self.ui.lineEdit_name.setText("Rahul")
        self.ui.lineEdit_address.setText("Kolkata")
        self.ui.lineEdit_phone.setText("1234567890")
        for i in range(len(fake_table)):
            for j in range(len(fake_table[i])):
                item = QTableWidgetItem(str(fake_table[i][j]))
                self.ui.tableWidget.setItem(i, j, item)
                if j == 3:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.setItem(i+1, 0, QTableWidgetItem(""))
    
    #  display popup
    def show_popup(self,msg):
        popup = QMessageBox(self)
        popup.setWindowTitle("Popup")
        popup.setText(msg)
        popup.show()

        # Automatically close the popup after 2 seconds
        timer = QTimer(self)
        timer.timeout.connect(popup.close)
        timer.start(1000)
        
    def send_image_to_telegram(self):
        name,addr,phone,id = self.cust_Details()
        fn = all_function()
        fn.send_pdf_with_text_to_telegram(r"Main_Software\Image_pdf\invoice.pdf",f"{name}_{id}_estimate.pdf",f"{id}\n{name}\n{addr}\n{phone}")
        # fn.send_image_with_caption_to_telegram(r"Main_Software\Image_pdf\invoice.png",f"{id}\n{name}\n{addr}\n{phone}")
        # print("send_image_to_telegram")
                
    def submit(self):
        if len(self.cust_Details()) == 0:
            return 
        if self.check_table() == False:
            DialogBox.show_warning_dialog("Please Enter All Details")
            return
        rem = self.ui.lineEdit_remaining
        if rem is not None and rem.text() != "":
            rem = rem.text()
            if len(rem) == 1 and (rem in ['-','+','.']):
                DialogBox.show_warning_dialog("Please Enter correct Details in Pay field")
                return
        # self.submit_btn_pressed = 1
        self.Insert_all_Record()
        self.last_date = self.ui.date_label.text()