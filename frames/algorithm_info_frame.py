from time import sleep

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

from algorithm import Algorithm


class AlgorithmInfoFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("algorithm_info_frame")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("algorithm_info_frame_layout")
        self.init_subframes()

    def init_subframes(self):
        algorithm_info_label_frame = QFrame(self)
        algorithm_info_label_frame.setFrameShape(QFrame.StyledPanel)
        algorithm_info_label_frame.setFrameShadow(QFrame.Raised)
        algorithm_info_label_frame.setObjectName("algorithm_info_label_frame")
        algorithm_info_label_layout = QVBoxLayout(algorithm_info_label_frame)
        algorithm_info_label_layout.setObjectName("verticalLayout_8")
        algorithm_info_label = QLabel(algorithm_info_label_frame)
        algorithm_info_label.setAlignment(QtCore.Qt.AlignCenter)
        algorithm_info_label.setText("Algorithm info")
        algorithm_info_label_layout.addWidget(algorithm_info_label)
        self.verticalLayout.addWidget(algorithm_info_label_frame)

        algorithm_info_content_scroll_area = QtWidgets.QScrollArea(self)
        algorithm_info_content_scroll_area.setWidgetResizable(True)
        algorithm_info_content_scroll_area.setObjectName("algorithm_info_content_scroll_area")
        algorithm_info_content_widget = QtWidgets.QWidget()
        algorithm_info_content_widget.setGeometry(QtCore.QRect(0, 0, 171, 189))
        algorithm_info_content_widget.setObjectName("algorithm_info_content_widget")
        algorithm_info_content_widget_layout = QtWidgets.QVBoxLayout(algorithm_info_content_widget)
        algorithm_info_content_widget_layout.setObjectName("algorithm_info_content_widget_layout")
        algorithm_info_label = QLabel(algorithm_info_content_widget)
        algorithm_info_label.setObjectName("algorithm_info_label")
        algorithm_info_content_widget_layout.addWidget(algorithm_info_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        algorithm_info_content_widget_layout.addItem(spacerItem1)
        algorithm_info_content_scroll_area.setWidget(algorithm_info_content_widget)
        self.verticalLayout.addWidget(algorithm_info_content_scroll_area)

    def change_algorithm(self, algorithm: Algorithm):
        self.verticalLayout.itemAt(0).widget().layout().itemAt(0).widget().setText(algorithm.name)
        self.verticalLayout.itemAt(1).widget().widget().layout().itemAt(0).widget().setText(algorithm.description)