from typing import List

from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtWidgets

from algorithm import Algorithm


class AlgorithmsFrame(QFrame):
    def __init__(self, parent, algorithms: List[Algorithm], chart_frame: QFrame, algorithms_info):
        super().__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.chart_frame = chart_frame
        self.algorithms_info = algorithms_info
        self.setObjectName("algorithms_frame")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("algorithms_frame_layout")
        self.init_subframes(algorithms)

    def init_subframes(self, algorithms: List[Algorithm]):
        algorithms_label_frame = QFrame(self)
        algorithms_label_frame.setFrameShape(QFrame.StyledPanel)
        algorithms_label_frame.setFrameShadow(QFrame.Raised)
        algorithms_label_frame.setObjectName("algorithms_label_frame")
        algorithms_label_layout = QVBoxLayout(algorithms_label_frame)
        algorithms_label_layout.setObjectName("verticalLayout_8")
        algorithms_label = QLabel(algorithms_label_frame)
        algorithms_label.setAlignment(QtCore.Qt.AlignCenter)
        algorithms_label.setObjectName("algorithms_label")
        algorithms_label.setText("Algorithms")
        algorithms_label_layout.addWidget(algorithms_label)
        self.verticalLayout.addWidget(algorithms_label_frame)

        algorithms_content_scroll_area = QtWidgets.QScrollArea(self)
        algorithms_content_scroll_area.setWidgetResizable(True)
        algorithms_content_scroll_area.setObjectName("algorithms_content_scroll_area")
        algorithms_content_widget = QtWidgets.QWidget()
        algorithms_content_widget.setGeometry(QtCore.QRect(0, 0, 171, 189))
        algorithms_content_widget.setObjectName("algorithms_content_widget")
        algorithms_content_widget_layout = QtWidgets.QVBoxLayout(algorithms_content_widget)
        algorithms_content_widget_layout.setObjectName("algorithms_content_widget_layout")
        for algorithm in algorithms:
            algorithm_button = QtWidgets.QPushButton(algorithms_content_widget)
            algorithm_button.setObjectName("algorithm_button_" + algorithm.name)
            algorithm_button.setText(algorithm.name)
            algorithm_button.clicked.connect(lambda checked, alg=algorithm: self.execute_algorithm(alg))
            algorithms_content_widget_layout.addWidget(algorithm_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        algorithms_content_widget_layout.addItem(spacerItem1)
        algorithms_content_scroll_area.setWidget(algorithms_content_widget)
        self.verticalLayout.addWidget(algorithms_content_scroll_area)

    def execute_algorithm(self, algorithm: Algorithm):
        self.algorithms_info.change_algorithm(algorithm)
        self.chart_frame.draw_plot_widget(algorithm.execute_algorithm())
