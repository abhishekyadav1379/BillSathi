main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Record_v_2 = QtWidgets.QDialog()
    ui = Ui_Record_v_2()
    ui.setupUi(Record_v_2)
    Record_v_2.show()
    sys.exit(app.exec())
