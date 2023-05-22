from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFrame


class ChartFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("chart_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

    def draw_plot_widget(self, plot_widget):
        if self.verticalLayout.count() > 0:
            self.verticalLayout.itemAt(0).widget().deleteLater()
        self.verticalLayout.addWidget(plot_widget)
