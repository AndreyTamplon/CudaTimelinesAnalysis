from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel
from functools import partial


class TimelineElementFrame(QFrame):
    def __init__(self, parent, model, timeline_label):
        super().__init__(parent)
        self.radio_button = None
        self.parent = parent
        self.model = model
        self.model.add_subscriber(self)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("timeline_element_frame")
        self._layout = QHBoxLayout(self)
        self._layout.setObjectName("timeline_element_frame_layout")
        self.timeline_label = timeline_label
        self.init_subframes()
        self._layout.setStretch(0, 1)
        self._layout.setStretch(1, 3)

    def init_subframes(self):
        self.radio_button_frame = QFrame(self)
        self.radio_button_frame.setFrameShape(QFrame.StyledPanel)
        self.radio_button_frame.setFrameShadow(QFrame.Raised)
        self.radio_button_frame.setObjectName("radio_button_frame")

        self.radio_button_layout = QVBoxLayout(self.radio_button_frame)
        self.radio_button_layout.setContentsMargins(-1, 0, 0, 0)
        self.radio_button_layout.setObjectName("radio_button_layout")

        self.radio_button = QRadioButton(self.radio_button_frame)
        self.radio_button.setText("")
        self.radio_button.setObjectName("radio_button")
        self.radio_button.clicked.connect(partial(self.process_click, self.radio_button))

        self.radio_button_layout.addWidget(self.radio_button)
        self.add_frame(self.radio_button_frame)

        self.timelines_list_frame = QFrame(self)
        self.timelines_list_frame.setFrameShape(QFrame.StyledPanel)
        self.timelines_list_frame.setFrameShadow(QFrame.Raised)
        self.timelines_list_frame.setObjectName("timelines_list_frame")

        self.timelines_list_layout = QVBoxLayout(self.timelines_list_frame)
        self.timelines_list_layout.setContentsMargins(0, 0, -1, 0)
        self.timelines_list_layout.setObjectName("timelines_list_layout")

        timeline_label = QLabel(self.timelines_list_frame)
        timeline_label.setText(self.timeline_label)
        timeline_label.setObjectName("timeline_label_" + self.timeline_label)
        self.timelines_list_layout.addWidget(timeline_label)

        self.add_frame(self.timelines_list_frame)

    def process_click(self, button):
        if button.isChecked():
            self.model.select_timelines(self.timeline_label)
        else:
            self.model.unselect_timeline(self.timeline_label)

    def add_frame(self, frame):
        self._layout.addWidget(frame)

    def update(self) -> None:
        if self.model.is_timeline_selected(self.timeline_label):
            self.radio_button.setChecked(True)
        else:
            self.radio_button.setChecked(False)
