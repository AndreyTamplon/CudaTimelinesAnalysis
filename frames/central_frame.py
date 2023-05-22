from PyQt5.QtWidgets import QFrame
from PyQt5 import QtCore, QtGui, QtWidgets

class CentralFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    main_frame = CentralFrame(None)
    main_frame.show()
    app.exec_()