import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from All_function import all_function
from PyQt6.QtGui import QFont, QColor, QLinearGradient,QBrush

import time

class TreeWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def convert_to_string_lists(self, input_list):

        result = [[str(item) for item in sublist] for sublist in input_list]

        return result

    def initUI(self):
        self.setWindowTitle("TreeWidget Example")
        self.setGeometry(100, 100, 800, 400)

        treeWidget = QTreeWidget(self)
        style = ("""
    QTreeWidget {
        font-size: 16px;
        background-color: rgb(218, 245, 255);
    }
    
    QTreeWidget::item {
        padding: 10px;
    }

    QTreeWidget::item:selected {
        background-color: #89AEF9;
        color: white;
    }
    
    QTreeWidget::item:disabled {
        background-color: #DDD;
        color: #888;
    }
    QTableWidget::item:hover {
    background-color: #E6F1FF;
}

    
    QTreeWidget QHeaderView::section {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #4876AF, stop:1 #286090);
        color: white;
        font-weight: bold;
        padding: 4px;
        border: none;
        border-bottom: 1px solid #355F8C;
        border-radius: 4px;
        border-top-right-radius: 14px;
}
QTreeWidget::item:open:has-children {
        background-color: #007ACC;
        color: white;
        }

""")


        
        treeWidget.setStyleSheet(style)
        font = QFont()
        font.setBold(True)
        font.setPointSize(11)
        
        # Set text color to white
        text_color = QColor(255, 0, 0)
        bg_color = QColor(120, 193, 243)
        # Create a gradient for the background color
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setColorAt(0, QColor(255, 255, 0))  # Start color at the left (#f2f2f2)
        gradient.setColorAt(1, QColor(255, 255, 255))  
        
        treeWidget.setHeaderLabels(["Date", "Time", "Give", "Total", "Method"])
        parent_item = None
        fn = all_function()
        id = "23080408"
        products = fn.select_db(
            f"select date,time,prod,quantity,rate,value,method from product where id = '{id}' order by date,time")
        money = fn.select_db(
            f"select date,time,give,total,method from money where id = '{id}' order by date,time")
        products = self.convert_to_string_lists(products)
        money = self.convert_to_string_lists(money)
        pro_len = len(products)
        mon_len = len(money)
        
        p, m = 0, 0
        a = 1
        while p != pro_len and m != mon_len:
            if pro_len == 0:
                break
            if (products[p][0] + products[p][1]) != (money[m][0] + money[m][1]):
                parent_item = QTreeWidgetItem(treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
                for i in range(5):
                    parent_item.setFont(i,font)
                m += 1
            else:
                parent_item = QTreeWidgetItem(treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
                parent_child = QTreeWidgetItem(parent_item, ["Product", "Quantity", "Rate", "Amount"])
                alternate_color = QColor(229, 249, 255)
                if a%2 == 0:
                    for i in range(5):
                        parent_item.setBackground(i,alternate_color)
                a+=1
                # for i in range(5):
                #     parent_item.setFont(i,font)
                    # parent_item.setBackground(i, bg_color)
                for i in range(4):
                    parent_child.setBackground(i, bg_color)
                    parent_child.setFont(i, font)
                while (p != pro_len and m != mon_len) and ((products[p][0] + products[p][1]) == (money[m][0] + money[m][1])):
                    parent_child = QTreeWidgetItem(parent_item, [products[p][2], products[p][3], products[p][4], products[p][5]])
                    p += 1
                parent_child = QTreeWidgetItem(parent_item, ["Paid:", "₹ " + money[m][2], "Total:","₹ "+ money[m][3]])
                for i in range(4):
                    if i%2==0:
                        parent_child.setForeground(i, text_color)
                    parent_child.setFont(i, font)
                parent_child = QTreeWidgetItem(parent_item, ["Method:", money[m][4], "", ""])
                gbg_color = QColor(255, 140, 140)
                for i in range(4):
                    if i%2 == 0:
                        parent_child.setForeground(i, text_color)
                    parent_child.setFont(i, font)
                    # parent_child.setBackground(i, gbg_color)
        
                m += 1

        while m != mon_len:
            parent_item = QTreeWidgetItem(
                treeWidget, [money[m][0], money[m][1], money[m][2], money[m][3], money[m][4]])
            m += 1

        # treeWidget.setAlternatingRowColors(True)
        self.setCentralWidget(treeWidget)


def main():
    app = QApplication(sys.argv)
    ex = TreeWidgetExample()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_time = time.time()
    main()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
