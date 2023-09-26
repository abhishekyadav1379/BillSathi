from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class QToaster(QtWidgets.QFrame):
    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        layout = QtWidgets.QHBoxLayout(self)

        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, 
                           QtWidgets.QSizePolicy.Policy.Maximum)

        self.setStyleSheet('''
            QToaster {
                border: 1px solid black;
                border-radius: 4px; 
                background: palette(window);
                background-color: #EF8181;
                
            }
            
        ''')

        self.timer = QtCore.QTimer(singleShot=True, timeout=self.hide)

        self.opacityAni = QtCore.QPropertyAnimation(self, b'windowOpacity')
        self.opacityAni.setStartValue(0.)
        self.opacityAni.setEndValue(1.)
        self.opacityAni.setDuration(100)

        self.corner = QtCore.Qt.Corner.TopLeftCorner
        self.margin = 10

    def restore(self):
        self.timer.stop()
        self.opacityAni.stop()
        self.setWindowOpacity(1)

    def hide(self):
        self.opacityAni.setDirection(QtCore.QAbstractAnimation.Direction.Backward)
        self.opacityAni.setDuration(500)
        self.opacityAni.start()

    def enterEvent(self, event):
        self.restore()

    def leaveEvent(self, event):
        self.timer.start()

    def closeEvent(self, event):
        self.deleteLater()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.clearMask()

    @staticmethod
    @staticmethod
    def showMessage(message, 
                    icon=QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation, 
                    corner=QtCore.Qt.Corner.TopLeftCorner, margin=10, closable=True, 
                    timeout=5000, parent=None):

        toaster = QToaster(parent)
        toaster.timer.setInterval(timeout)

        if isinstance(icon, QtWidgets.QStyle.StandardPixmap):
            labelIcon = QtWidgets.QLabel()
            toaster.layout().addWidget(labelIcon)
            icon = toaster.style().standardIcon(icon)
            labelIcon.setPixmap(icon.pixmap(QtCore.QSize(24, 24)))  # Set the icon size here

        toaster.label = QtWidgets.QLabel(message)
        # Set the font to Arial with a font size of 8px
        font = QtGui.QFont("Arial", 8)
        toaster.label.setFont(font)
        toaster.layout().addWidget(toaster.label)

        if closable:
            toaster.closeButton = QtWidgets.QToolButton()
            toaster.layout().addWidget(toaster.closeButton)
            closeIcon = toaster.style().standardIcon(
                QtWidgets.QStyle.StandardPixmap.SP_TitleBarCloseButton)
            toaster.closeButton.setIcon(closeIcon)
            toaster.closeButton.setAutoRaise(True)
            toaster.closeButton.clicked.connect(toaster.close)

        toaster.timer.timeout.connect(toaster.close)
        toaster.timer.start()

        toaster.raise_()
        toaster.adjustSize()

        toaster.corner = corner
        toaster.margin = margin

        geo = toaster.geometry()
        if corner == QtCore.Qt.Corner.TopLeftCorner:
            geo.moveTopLeft(QtCore.QPoint(margin, margin))
        elif corner == QtCore.Qt.Corner.TopRightCorner:
            geo.moveTopRight(QtCore.QPoint(parent.width() - toaster.width() - margin, margin))
        elif corner == QtCore.Qt.Corner.BottomRightCorner:
            geo.moveBottomRight(QtCore.QPoint(parent.width() - toaster.width() - margin,
                                            parent.height() - toaster.height() - margin))
        else:
            geo.moveBottomLeft(QtCore.QPoint(margin, parent.height() - toaster.height() - margin))

        toaster.setGeometry(geo)
        toaster.show()
        toaster.opacityAni.start()


def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle("Dialog with Toaster")
    layout = QtWidgets.QVBoxLayout(dialog)

    button = QtWidgets.QPushButton("Show Toaster")
    layout.addWidget(button)

    def show_toaster():
        QToaster.showMessage("This is a toaster message.", parent=None, timeout=2000)

    button.clicked.connect(show_toaster)

    dialog.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()