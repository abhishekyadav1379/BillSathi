import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMenu
from PyQt6.QtCore import Qt
import configparser
from datetime import datetime
from googletrans import Translator
import os
import shutil
from datetime import datetime, timedelta
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import QTimer
import fitz
import toml

class all_function():
    def __init__(self):
        # self.database_path = "./Main_Software/Database/mahendra.db"
        self.database_path = self.read_toml_section_value("Database","path")
        # path_temp = 0
        # if path_changed == 1:
        #     self.copy_file("./Main_Software/Database/mahendra.db","./Main_Software/Database/","mahendra_temp.db")
        #     self.database_path = "./Main_Software/Database/mahendra.db"
        #     path_temp = 1
            
        #     self.write_toml_section_value("Database","temp", 0)
        
        # if path_temp == 1:
            
    def select_db(self,query):
        try:
            mydb = sqlite3.connect(self.database_path)
            cur = mydb.cursor()
            # Customer product purchase details
            query1 = query
            cur.execute(query1)
            result = cur.fetchall()
            cur.close()
            # print(result)
            return result
        except sqlite3.Error as e:
            print("Error: " + str(e))
            return "Error"
        
    def insert_db(self,query,value):
        try:
            mydb = sqlite3.connect(self.database_path)
            mycursor = mydb.cursor()
            # Fill customer details
            query1 = query
            val = value
            # print("Insert Query: ",query1,val)
            mycursor.execute(query1, val)
            mydb.commit()
            mydb.close()
            return "Success"
        except sqlite3.Error as e:
            print(f"Insert_db error on all funciton \n{e}")
            return "Error"
    
    def delete_db(self,id,table):
        query = f"DELETE FROM {table} WHERE id = '{id}'"
        print(query)
        self.insert_db(query,())
    
    # it read value from  ini file  
    def read_config_value(self,section, key):
        file_path = "./Main_Software/settings.ini"
        config = configparser.ConfigParser()
        config.read(file_path)

        try:
            value = config.get(section, key)
            return value
        except configparser.NoSectionError:
            print(f"Section '{section}' does not exist in the config file.")
        except configparser.NoOptionError:
            print(f"Key '{key}' does not exist in the section '{section}'.")

    def store_config_value(self, section, key, value):
        file_path = "./Main_Software/settings.ini"
        config = configparser.ConfigParser()
        config.read(file_path)

        if not config.has_section(section):
            config.add_section(section)

        config.set(section, key, value)

        with open(file_path, 'w') as config_file:
            config.write(config_file)
            print(f"Value '{value}' stored successfully for key '{key}' in section '{section}'.")

    def translate_text(self, text, source_language='en', target_language='hi'):
        try:
            if text == "":
                return
            translator = Translator()
            translated_text = translator.translate(text, src=source_language, dest=target_language).text
            return translated_text
        except Exception as e:
            return f"Translation Error: {e}"
            
    @staticmethod
    def convert_date_format(date_str):
        # Parse the input date string using the specified format
        input_format = "%d-%m-%Y"
        date_obj = datetime.strptime(date_str, input_format)

        # Convert the date object to the desired output format
        output_format = "%Y-%m-%d"
        formatted_date = date_obj.strftime(output_format)

        return formatted_date
    
    def copy_file(self, source_path, destination_path, new_filename=None):
        try:
            # Check if the source file exists
            if not os.path.isfile(source_path):
                print(f"Error: Source file '{source_path}' does not exist.")
                return

            # Check if the destination folder exists
            if not os.path.exists(destination_path):
                print(f"Error: Destination folder '{destination_path}' does not exist.")
                return

            # Get the filename from the source path
            filename = os.path.basename(source_path)

            # Use the new filename if provided, otherwise, use the original filename
            if new_filename:
                destination_file_path = os.path.join(destination_path, new_filename)
            else:
                destination_file_path = os.path.join(destination_path, filename)

            # Check if the destination file exists, and if it does, remove it
            if os.path.exists(destination_file_path):
                os.remove(destination_file_path)

            # Copy the file from source to destination
            shutil.copy2(source_path, destination_file_path)
            print(f"File '{filename}' copied successfully to '{destination_path}' as '{os.path.basename(destination_file_path)}'.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def time_convert(self,time):
        return datetime.strptime(time, "%I:%M:%S %p").strftime("%H:%M:%S")
    
    def date_convert_format(self,date_str):
        try:
            # Split the date into day, month, and year
            day, month, year = date_str.split('-')
            # Create the new date format
            new_date = f"{year}-{month}-{day}"
            return new_date
        except ValueError:
            return "Invalid date format. Please use dd-mm-yyyy."
    
    def convert_date_format_ddmmyyyy(self,date_yyyy_mm_dd):
        parts = date_yyyy_mm_dd.split('-')
        if len(parts) != 3:
            return "Invalid date format"
        
        year = parts[0]
        month = parts[1]
        day = parts[2]
        
        formatted_date = f"{day}-{month}-{year}"
        return formatted_date


    # *date must be in yyyy-mm-dd format 
    def add_days_to_date(self,days):
        try:
            # Get the current date
            current_date = datetime.now()
    
            # Add the specified number of days to the current date
            new_date = current_date + timedelta(days=days)
    
            return new_date.strftime('%Y-%m-%d')
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
    
    def compare_dates(self,date_str1, date_str2):
        try:
            # Convert date strings to datetime objects
            date1 = datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.strptime(date_str2, '%Y-%m-%d')

            if date1 < date2:
                return -1
            elif date1 > date2:
                return 1
            else:
                return 0

        except ValueError as ve:
            print(f"Error occurred: {ve}")
            return None
        
    def convert_pdf_to_image(self,pdf_path):
        doc = fitz.open(pdf_path)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap()  # render page to an image
            zoom_x = 16.0  # horizontal zoom
            zoom_y = 16.0  # vertical zoom
            mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
            pix = page.get_pixmap(matrix=mat)
            pix.save("invoice.png")  # store image as a PNG
            break
    
    def today_sale(self):
        self.today_date = datetime.now().strftime("%Y-%m-%d")
        # sale order return as [gitti, cement, maurang, sariya]
        today_sale = self.select_db(f"""SELECT
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
        self.today_date = datetime.now().strftime("%Y-%m-%d")
        #per unit price order [cement, gitti, maurang, sariya]
        per_unit_price = self.select_db(f"select sum(Rate)/sum(quantity) from stock_table group by product_desc")
        sale_price_today = self.select_db(f'''SELECT
                        SUM(CASE WHEN prod LIKE '%gitti%' THEN Value ELSE 0 END) AS gitti_sum,
                        SUM(CASE WHEN prod LIKE '%cement%' THEN Value ELSE 0 END) AS cement_sum,
                        SUM(CASE WHEN prod LIKE '%maurang%' THEN Value ELSE 0 END) AS maurang_sum,
                        SUM(CASE WHEN prod LIKE '%sariya%' THEN Value ELSE 0 END) AS sariya_sum
                        FROM product
                        WHERE (prod LIKE '%gitti%' OR prod LIKE '%cement%' OR prod LIKE '%maurang%' OR prod LIKE '%sariya%')
                        and date = '{self.today_date}' ''')[0]
        today_sale = list(self.today_sale()[0])
        sale_price_today = list(sale_price_today)
        
        for i in range(4):
            if today_sale[i] == None:
                today_sale[i] = 0
            if sale_price_today[i] == None:
                sale_price_today[i] = 0
        cement_profit =  sale_price_today[0] - per_unit_price[0][0] * today_sale[1] 
        sariya_profit = sale_price_today[3] - per_unit_price[3][0] * today_sale[3]
        gitti_profit = sale_price_today[1] - per_unit_price[1][0] * today_sale[0]
        maurang_profit = sale_price_today[2] - per_unit_price[2][0] * today_sale[2]
        total_profit = cement_profit + sariya_profit + gitti_profit + maurang_profit
        check_profit_date = self.select_db(f"select profit from Profit_table where date = '{self.today_date}'")
        if  len(check_profit_date) == 0:
            self.insert_db(f"insert into Profit_table values(?,?)",(self.today_date, total_profit))
        else:
            self.insert_db(f"update Profit_table set profit = ? where date = ?",(total_profit, self.today_date))
        # print(check_profit_date) 

    def read_toml_section_value(self, section_name, value_key):
        file_path = r'Main_Software\setting.toml'
        try:
            with open(file_path, 'r') as toml_file:
                toml_data = toml.load(toml_file)

                # Check if the specified section exists in the TOML file
                if section_name in toml_data:
                    section_info = toml_data[section_name]

                    # Check if the specified value key exists in the section
                    if value_key in section_info:
                        value = section_info[value_key]
                        return value
                    else:
                        return f"'{value_key}' not found in the '{section_name}' section."
                else:
                    return f"'{section_name}' section not found in the TOML file."
        except FileNotFoundError:
            return "File not found."
        except toml.TomlDecodeError:
            return "Error decoding the TOML file."

    def write_toml_section_value(self, section_name, value_key, value):
        file_path = r"Main_Software\setting.toml"
        try:
            # Load existing TOML data if it exists, or create an empty dictionary
            try:
                with open(file_path, 'r') as toml_file:
                    toml_data = toml.load(toml_file)
            except FileNotFoundError:
                toml_data = {}

            # Create or update the specified section and value key
            if section_name not in toml_data:
                toml_data[section_name] = {}
            toml_data[section_name][value_key] = value

            # Write the updated data back to the TOML file
            with open(file_path, 'w') as toml_file:
                toml.dump(toml_data, toml_file)

            return "Value updated successfully."
        except Exception as e:
            return f"Error: {str(e)}" 
        
        
        
######### ToolTip class #############           
class TooltipDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def helpEvent(self, event, view, option, index):
        if event.type() == QtCore.QEvent.Type.ToolTip:
            item = view.model().data(index, QtCore.Qt.ItemDataRole.DisplayRole)
            QtWidgets.QToolTip.showText(event.globalPos(), item)
            return True
        return super().helpEvent(event, view, option, index)

    
        
# fn = all_function()
# te = fn.translate_text("Hello")
# print(te)