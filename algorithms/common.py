from typing import List

import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget
import pyqtgraph as pg

from timelines_processing.timeline import Timeline


def create_timeline_bar_chart_from_timelines(timelines: List[Timeline]):
    plot_widget = PlotWidget()
    plot_widget.setTitle("Timeline Bar Chart")
    plot_widget.setLabel("left", "Event Name")
    plot_widget.setLabel("bottom", "Time")
    label = QtWidgets.QLabel(plot_widget)
    label.setWindowFlags(QtCore.Qt.ToolTip)
    bargraphs = []
    event_colors = {}
    text_items = []
    color_index = 2
    height = 0.6
    x_left_border = 10000000
    x_right_border = 0
    i = 0
    for timeline in timelines:
        data = []
        for start_time, end_time, event_name in timeline.get_tuples():
            if event_name not in event_colors:
                event_colors[event_name] = QtGui.QColor(QtCore.Qt.GlobalColor(color_index))
                color_index += 1
            data.append([float(start_time), float(end_time), event_name])
        data.sort(key=lambda x: x[0])

        y = np.ones(len(data)) * (i + 0.8)
        width = [x[1] - x[0] for x in data]
        x = [x[0] + (width[i] / 2) for i, x in enumerate(data)]
        if x[0] < x_left_border:
            x_left_border = x[0]
        if x[-1] > x_right_border:
            x_right_border = x[-1]
        brushes = [event_colors[t[2]] for t in data]
        bargraph = pg.BarGraphItem(x=x, y=y, width=width, height=height, brushes=brushes)
        bargraphs.append(bargraph)
        plot_widget.addItem(bargraph)
        max_width = max(width)
        for j, xi in enumerate(x):
            label = pg.TextItem(text=data[j][2], rotateAxis=(0, 1))
            label.setAnchor((0.5, -0.5))
            label.setPos(xi + (width[j] / 2) + 0.15 * width[j] * (max_width / width[j]), y[j])
            text_items.append(label)
            plot_widget.addItem(label)
        i += 1
    plot_widget.invertY(True)

    def on_zoom():
        y_min, y_max = plot_widget.viewRange()[1]
        y_span = y_max - y_min
        threshold = height * 5
        for item in text_items:
            if y_span < threshold:
                item.setColor((200, 200, 200, 255))
            else:
                item.setColor((200, 200, 200, 0))

    plot_widget.sigRangeChanged.connect(on_zoom)
    plot_widget.setAspectLocked(True, ratio=0.005)
    plot_widget.setYRange(0, len(timelines) * 1.5)
    plot_widget.setXRange(x_left_border - 10, x_right_border + 10)
    return plot_widget

def create_timeline_bar_chart_from_myers_output(timelines: List[List]):
    start_times_1 = []
    end_times_1 = []
    event_names_1 = []
    for timestamp in timelines[0]:
        start_time, end_time, event_name = timestamp
        start_times_1.append(start_time)
        end_times_1.append(end_time)
        event_names_1.append(event_name)

    timeline_1 = Timeline("timeline_1", start_times_1, end_times_1, event_names_1)
    start_times_2 = []
    end_times_2 = []
    event_names_2 = []
    for timestamp in timelines[1]:
        start_time, end_time, event_name = timestamp
        start_times_2.append(start_time)
        end_times_2.append(end_time)
        event_names_2.append(event_name)

    timeline_2 = Timeline("timeline_2", start_times_2, end_times_2, event_names_2)
    return create_timeline_bar_chart_from_timelines([timeline_1, timeline_2])

