from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QWidget

from pyqt5_plugins.examplebutton import QtWidgets

from frames.timeline_element_frame import TimelineElementFrame
from model.model import Model


class TimelinesFrame(QFrame):
    def __init__(self, parent, model : Model):
        super().__init__(parent)
        self.parent = parent
        self.model = model
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("timelines_frame")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("timelines_frame_layout")
        self.init_subframes(model)

    def init_subframes(self, model : Model):
        timelines_frame_content_scroll_area = QScrollArea(self)
        timelines_frame_content_scroll_area.setWidgetResizable(True)
        timelines_frame_content_scroll_area.setObjectName("timelines_list_area")

        timelines_label_frame = QtWidgets.QFrame(self)
        timelines_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        timelines_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        timelines_label_frame.setObjectName("timelines_label_frame")

        timelines_label_layout = QtWidgets.QVBoxLayout(timelines_label_frame)
        timelines_label_layout.setObjectName("timelines_label_layout")
        timelines_label = QtWidgets.QLabel(timelines_label_frame)
        timelines_label.setAlignment(QtCore.Qt.AlignCenter)
        timelines_label.setObjectName("timelines_label")
        timelines_label.setText("Timelines")
        timelines_label_layout.addWidget(timelines_label)
        self.verticalLayout.addWidget(timelines_label_frame)

        timelines_frame_content_widget = QWidget(timelines_frame_content_scroll_area)
        timelines_frame_content_widget.setGeometry(QtCore.QRect(0, 0, 139, 216))
        timelines_frame_content_widget.setObjectName("timelines_list_area_widget")

        timelines_frame_content_widget_layout = QVBoxLayout(timelines_frame_content_widget)
        timelines_frame_content_widget_layout.setObjectName("timelines_list_area_widget_layout")
        timelines = model.get_timelines()
        for timeline in timelines:
            timeline_pair_frame = TimelineElementFrame(timelines_frame_content_widget, self.model, timeline.get_name())
            timelines_frame_content_widget_layout.addWidget(timeline_pair_frame)

        timelines_frame_content_scroll_area.setWidget(timelines_frame_content_widget)
        self.verticalLayout.addWidget(timelines_frame_content_scroll_area)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        timelines_frame_content_widget_layout.addItem(spacer_item)

        add_timeline_frame = QFrame(self)
        add_timeline_frame.setFrameShape(QFrame.StyledPanel)
        add_timeline_frame.setFrameShadow(QFrame.Raised)
        add_timeline_frame.setObjectName("add_timeline_frame")

        add_timeline_layout = QVBoxLayout(add_timeline_frame)
        add_timeline_layout.setObjectName("add_timeline_layout")
        add_timeline_layout.setContentsMargins(-1, 0, -1, 0)

        timelines_frame_content_widget_layout.addWidget(add_timeline_frame)
