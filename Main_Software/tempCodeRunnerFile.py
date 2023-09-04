__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Stock = QtWidgets.QDialog()
    ui = Ui_Stock()
    ui.setupUi(Stock)
    Stock.show()
    sys.exi