from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class Ui_ReturnGUI(object):
    def setupUi(self, ReturnGUI):
        # ReturnGUI.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ReturnGUI.setObjectName("ReturnGUI")
        ReturnGUI.resize(304, 151)
        self.gridLayout = QtWidgets.QGridLayout(ReturnGUI)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_cash = QtWidgets.QRadioButton(parent=ReturnGUI)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_cash.setFont(font)
        self.radioButton_cash.setObjectName("radioButton_cash")
        self.gridLayout.addWidget(self.radioButton_cash, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=ReturnGUI)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        self.radioButton_udhar = QtWidgets.QRadioButton(parent=ReturnGUI)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_udhar.setFont(font)
        self.radioButton_udhar.setObjectName("radioButton_udhar")
        self.gridLayout.addWidget(self.radioButton_udhar, 17, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ReturnGUI)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 18, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(ReturnGUI)
        QtCore.QMetaObject.connectSlotsByName(ReturnGUI)

################################################################
        self.radioButton_cash.setChecked(True)  # Set default selection to "Yes"
        # Connect buttonBox signals to slots
        # self.buttonBox.accepted.connect(self.ok_clicked)
        # self.buttonBox.rejected.connect(self.cancel_clicked)

    def retranslateUi(self, ReturnGUI):
        _translate = QtCore.QCoreApplication.translate
        ReturnGUI.setWindowTitle(_translate("ReturnGUI", "Return"))
        self.radioButton_cash.setText(_translate("ReturnGUI", "Cash"))
        self.label.setText(_translate("ReturnGUI", "Please Select Return Type. \nपैसे वापसी का प्रकार चुने| "))
        self.radioButton_udhar.setText(_translate("ReturnGUI", "Udhar"))

    
