from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QWidget, QVBoxLayout, QTabWidget
from PyQt6.QtCharts import QBarCategoryAxis, QBarSeries, QBarSet, QChart, QChartView, QValueAxis
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QDate, Qt
from PyQt6.QtGui import QPainter, QCursor
from All_function import all_function
from datetime import datetime


# Profit chart
class ChartWidget_Profit(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.tooltip_label = QLabel(self)
        self.tooltip_label.setStyleSheet(
            "QLabel { background-color: white; padding: 5px; border: 1px solid gray; }")
        self.tooltip_label.hide()

        self.series.hovered.connect(self.show_tooltip)

        # fn = all_function()
        # fn.profit_loss()
        # today_date = datetime.now().strftime("%d-%m-%Y")
        # self.profit = fn.select_db(f"select profit from profit_table where date = '{today_date}'")

    def setup_ui(self):
        self.fn = all_function()
        # date by order wise nhi krna hai isko
        self.result = self.fn.select_db(
            "select * from profit_table limit 30")
        if len(self.result) == 0:
            return
        # print(self.result)
        # self.data_fetcher = Func()
        # self.result = self.data_fetcher.data_fetch()
        # Create an empty list for each column
        self.record = [[] for _ in range(len(self.result[0]))]
        self.setup_chart_series()
        self.setup_chart()
        self.setup_axes()
        self.setup_legend()
        self.setup_layout()

    def setup_chart_series(self):
        self.cash_set = QBarSet("Profit")
        # self.udhari_set=QBarSet("Udhari")
        # self.total_set=QBarSet("Total Sale")

        for row in self.result:
            for i, value in enumerate(row):
                self.record[i].append(value)

        self.cash_set.append(self.record[1])
        # self.udhari_set.append(self.record[2])
        # self.total_set.append(self.record[3])

        self.series = QBarSeries()
        self.series.append(self.cash_set)
        # self.series.append(self.udhari_set)
        # self.series.append(self.total_set)

    def setup_chart(self):
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Profit Chart")

    def setup_axes(self):
        self.categories = self.record[0]

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 30000)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

    def setup_legend(self):
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

    def setup_layout(self):
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

    def show_tooltip(self, status, item, bar_set):
        if status:
            cursor_pos = self.chart_view.mapFromGlobal(QCursor.pos())
            pos = self.chart_view.mapToGlobal(self.chart_view.pos())
            pos.setX(cursor_pos.x())  # Use cursor's x position
            # Adjust the tooltip's vertical position
            pos.setY(cursor_pos.y() + 20)
            self.tooltip_label.move(pos)
            value = bar_set.at(item)
            self.tooltip_label.setText(f"Value: {value}")
            self.tooltip_label.show()
        else:
            self.tooltip_label.hide()

# Yearly chart


class ChartWidget_Yearly(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.tooltip_label = QLabel(self)
        self.tooltip_label.setStyleSheet(
            "QLabel { background-color: white; padding: 5px; border: 1px solid gray; }")
        self.tooltip_label.hide()

        self.series.hovered.connect(self.show_tooltip)

    def setup_ui(self):
        self.fn = all_function()
        self.result = self.fn.select_db(
            '''SELECT strftime('%m-%Y', Date) AS month,
       SUM(GIVE),
       SUM(CASE WHEN method = 'Udhar' THEN TOTAL ELSE 0 END) AS UDHARI,
       SUM(TOTAL) 
FROM MONEY 
GROUP BY strftime('%m-%Y', Date) 
LIMIT 12;
''')
        if len(self.result) == 0:
            return
        # print(self.result)
        # self.data_fetcher = Func()
        # self.result = self.data_fetcher.data_fetch()
        # Create an empty list for each column
        self.record = [[] for _ in range(len(self.result[0]))]

        self.setup_chart_series()
        self.setup_chart()
        self.setup_axes()
        self.setup_legend()
        self.setup_layout()

    def setup_chart_series(self):
        self.cash_set = QBarSet("Receievd")
        self.udhari_set = QBarSet("Udhari")
        self.total_set = QBarSet("Total Sale")

        for row in self.result:
            for i, value in enumerate(row):
                self.record[i].append(value)

        self.cash_set.append(self.record[1])
        self.udhari_set.append(self.record[2])
        self.total_set.append(self.record[3])

        self.series = QBarSeries()
        self.series.append(self.cash_set)
        self.series.append(self.udhari_set)
        self.series.append(self.total_set)

    def setup_chart(self):
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Last 12 Months Record")

    def setup_axes(self):
        self.categories = self.record[0]

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 7000000)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

    def setup_legend(self):
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

    def setup_layout(self):
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

    def show_tooltip(self, status, item, bar_set):
        if status:
            cursor_pos = self.chart_view.mapFromGlobal(QCursor.pos())
            pos = self.chart_view.mapToGlobal(self.chart_view.pos())
            pos.setX(cursor_pos.x())  # Use cursor's x position
            # Adjust the tooltip's vertical position
            pos.setY(cursor_pos.y() + 20)
            self.tooltip_label.move(pos)
            value = bar_set.at(item)
            self.tooltip_label.setText(f"Value: {int(value/100000)} lakh")
            self.tooltip_label.show()
        else:
            self.tooltip_label.hide()

# per month chart


class TestChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # fn = all_function()
        # fn.profit_loss()
        # today_date = datetime.now().strftime("%d-%m-%Y")
        # self.profit = fn.select_db(f"select profit from profit_table where date = '{today_date}'")[0]

        self.setup_ui()
        self.tooltip_label = QLabel(self)
        self.tooltip_label.setStyleSheet(
            "QLabel { background-color: white; padding: 5px; border: 1px solid gray; }")
        self.tooltip_label.hide()

        self.series.hovered.connect(self.show_tooltip)

    def setup_ui(self):
        self.fn = all_function()
        self.result = self.fn.select_db('''SELECT strftime('%d-%m-%Y', Date) as new_date,gv,UDHARI,Total  FROM (
                                                SELECT DATE,
                                                       SUM(GIVE) AS gv,
                                                       SUM(CASE when method = 'Udhar' then TOTAL else 0 end) AS UDHARI,
                                                       SUM(TOTAL) as Total
                                                FROM MONEY
                                                GROUP BY DATE
                                                ORDER BY Date DESC
                                                LIMIT 30
                                            ) AS subquery
                                            ORDER BY Date ;''')
        self.today_date = QDate.currentDate().toString("yyyy-MM-dd")
        fn = all_function()
        self.total_sale = fn.select_db(
            f"SELECT SUM(TOTAL) FROM MONEY WHERE DATE = '{self.today_date}'")[0]
        self.tot_rec = fn.select_db(
            f"SELECT SUM(GIVE) FROM MONEY WHERE DATE = '{self.today_date}'")[0]
        self.tot_udhari = fn.select_db(
            f'''select sum(tot) as new_tot from (select sum(total - give) as tot FROM Money 
                where id in (select id FROM Money where method IN ('Udhar','Jma','UPI','Cheaque') 
                and date = '{self.today_date}' and Total > 0) and date = '{self.today_date}' group by id) where tot>0''')[0]

        if len(self.result) == 0:
            return
        # print(self.result)
        # self.data_fetcher = Func()
        # self.result = self.data_fetcher.data_fetch()
        # Create an empty list for each column
        self.record = [[] for _ in range(len(self.result[0]))]
        # print(self.record)
        self.setup_chart_series()
        self.setup_chart()
        self.setup_axes()
        self.setup_legend()
        self.setup_layout()

    def setup_chart_series(self):
        self.cash_set = QBarSet("Received")
        self.udhari_set = QBarSet("Udhari")
        self.total_set = QBarSet("Total Sale")

        for row in self.result:
            for i, value in enumerate(row):
                self.record[i].append(value)

        self.cash_set.append(self.record[1])
        self.udhari_set.append(self.record[2])
        self.total_set.append(self.record[3])

        self.series = QBarSeries()
        self.series.append(self.cash_set)
        self.series.append(self.udhari_set)
        self.series.append(self.total_set)

    def setup_chart(self):
        self.chart = QChart()
        self.chart.addSeries(self.series)
        fn = all_function()
        fn.profit_loss()
        today_date = datetime.now().strftime("%Y-%m-%d")
        # self.profit = fn.select_db(
        #     f"select profit from profit_table where date = '{today_date}'")[0]

        self.total_sale = list(self.total_sale)
        self.tot_rec = list(self.tot_rec)
        self.tot_udhari = list(self.tot_udhari)
        # print(self.profit)
        # if self.profit[0] == None:
        #     self.profit[0] = 0
        if self.total_sale[0] == None:
            self.total_sale[0] = 0
        if self.tot_rec[0] == None:
            self.tot_rec[0] = 0
        if self.tot_udhari[0] == None:
            self.tot_udhari[0] = 0
        result = f'''[ <span style='color: red;'>Total:    </span>
            ₹ {int(self.total_sale[0])} 
            <span style='color: red;'>Received:    </span>
            ₹ {int(self.tot_rec[0])} 
            <span style='color: red;'>Udhari:    </span>
            ₹ {int(self.tot_udhari[0])} ]
            '''
        # self.chart.setTitle(
        #     f"Today - [Sale: ₹ {int(self.total_sale[0])}, Received: ₹ {int(self.tot_rec[0])}, Udhari: ₹ {int(self.tot_udhari[0])} ] - {int(self.profit[0])}")
        self.chart.setTitle(result)
        # Get the current title font and modify its size
        title_font = self.chart.titleFont()
        # Change the font size to your desired value
        title_font.setPointSize(16)

        # Set the modified font back to the title
        self.chart.setTitleFont(title_font)

    def setup_axes(self):
        self.categories = self.record[0]

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 600000)
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_y)

    def setup_legend(self):
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

    def setup_layout(self):
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

    def show_tooltip(self, status, item, bar_set):
        if status:
            cursor_pos = self.chart_view.mapFromGlobal(QCursor.pos())
            pos = self.chart_view.mapToGlobal(self.chart_view.pos())
            pos.setX(cursor_pos.x())  # Use cursor's x position
            # Adjust the tooltip's vertical position
            pos.setY(cursor_pos.y() + 20)
            self.tooltip_label.move(pos)
            value = bar_set.at(item)
            self.tooltip_label.setText(f"Value: {int(value/1000)} thousand")
            self.tooltip_label.show()
        else:
            self.tooltip_label.hide()
