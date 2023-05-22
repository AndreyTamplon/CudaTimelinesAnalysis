from PyQt5.QtWidgets import QFrame, QVBoxLayout


class ControlFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setMidLineWidth(0)
        self.setObjectName("control_frame")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("control_frame_layout")

    def init_subframes(self):
        pass

    def add_frame(self, frame):
        self._layout.addWidget(frame)