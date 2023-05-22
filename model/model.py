import os

from timelines_processing.timeline import parse_csv_to_timeline


class Model:
    def __init__(self, timelines_folder):
        self.timelines_folder = timelines_folder
        self.timelines = []
        self.selected_timelines = []
        self.subscribers = []
        self.load_timelines()

    def load_timelines(self) -> None:
        self.timelines = []
        for file in os.listdir(self.timelines_folder):
            if file.endswith(".csv"):
                timeline_path = os.path.join(self.timelines_folder, file)
                timeline = parse_csv_to_timeline(timeline_path)
                self.timelines.append(timeline)

    def select_timelines(self, timelines_names):
        for timeline in self.timelines:
            if timeline.get_name() in timelines_names:
                self.selected_timelines.append(timeline)

    def get_selected_timelines(self):
        return self.selected_timelines

    def unselect_timeline(self, timeline_name):
        for timeline in self.selected_timelines:
            if timeline.get_name() == timeline_name:
                self.selected_timelines.remove(timeline)

    def unselect_timelines(self):
        self.selected_timelines = []
        self.notify_subscribers()

    def get_timelines(self):
        return self.timelines

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def is_timeline_selected(self, timeline_name):
        for timeline in self.selected_timelines:
            if timeline.get_name() == timeline_name:
                return True
        return False
