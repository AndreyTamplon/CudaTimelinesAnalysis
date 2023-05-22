from PyQt5 import QtCore, QtWidgets

from algorithms.myers import Myers
from algorithms.print_timelines import PrintTimelines
from frames.algorithm_info_frame import AlgorithmInfoFrame
from frames.algorithms_frame import AlgorithmsFrame
from frames.central_frame import CentralFrame
from frames.chart_frame import ChartFrame
from frames.control_frame import ControlFrame
from frames.timelines_frame import TimelinesFrame
from frames.top_frame import TopFrame
from model.model import Model


class Ui_MainWindow(object):
    def __init__(self, model):
        self.model = model

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 587)
        MainWindow.setStyleSheet(" background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        style = open('style.css', 'r')
        self.centralwidget.setStyleSheet(style.read())
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        top_frame = TopFrame(self.centralwidget)
        self.verticalLayout.addWidget(top_frame)
        central_frame = CentralFrame(self.centralwidget)
        control_frame = ControlFrame(central_frame)
        timelines_frame = TimelinesFrame(control_frame, model)
        control_frame.verticalLayout.addWidget(timelines_frame)
        chart_frame = ChartFrame(central_frame)
        algorithm_info_frame = AlgorithmInfoFrame(central_frame)
        algorithms_frame = AlgorithmsFrame(control_frame, [Myers(model), PrintTimelines(model)],
                                           chart_frame, algorithm_info_frame)
        control_frame.verticalLayout.addWidget(algorithms_frame)
        central_frame.horizontalLayout.addWidget(control_frame)
        central_frame.horizontalLayout.addWidget(chart_frame)

        central_frame.horizontalLayout.addWidget(algorithm_info_frame)
        central_frame.horizontalLayout.setStretch(0, 1)
        central_frame.horizontalLayout.setStretch(1, 3)
        central_frame.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addWidget(central_frame)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    model = Model("timelines")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(model)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
