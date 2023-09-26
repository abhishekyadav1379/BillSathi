import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget, QRadioButton

class TreeWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expand/Collapse All Items in QTreeWidget")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Items"])
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.tree_widget)

        self.expand_button = QRadioButton("Expand All")
        self.collapse_button = QRadioButton("Collapse All")
        self.central_layout.addWidget(self.expand_button)
        self.central_layout.addWidget(self.collapse_button)

        # Connect the radio button signals to the corresponding methods
        self.expand_button.toggled.connect(self.expand_all_items)
        self.collapse_button.toggled.connect(self.collapse_all_items)

        # Populate the QTreeWidget with sample data
        parent1 = QTreeWidgetItem(self.tree_widget, ["Parent 1"])
        child1 = QTreeWidgetItem(parent1, ["Child 1"])
        child2 = QTreeWidgetItem(parent1, ["Child 2"])
        parent2 = QTreeWidgetItem(self.tree_widget, ["Parent 2"])
        child3 = QTreeWidgetItem(parent2, ["Child 3"])

    def expand_all_items(self):
        if self.expand_button.isChecked():
            # Iterate through all items in the QTreeWidget and expand them
            for item_index in range(self.tree_widget.topLevelItemCount()):
                item = self.tree_widget.topLevelItem(item_index)
                self.expand_item(item)

    def collapse_all_items(self):
        if self.collapse_button.isChecked():
            # Iterate through all items in the QTreeWidget and collapse them
            for item_index in range(self.tree_widget.topLevelItemCount()):
                item = self.tree_widget.topLevelItem(item_index)
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

def main():
    app = QApplication(sys.argv)
    window = TreeWidgetDemo()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()