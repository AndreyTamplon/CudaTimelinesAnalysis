from algorithm import Algorithm
from algorithms.common import create_timeline_bar_chart_from_timelines

description = "Выводит выбранные \nтаймлайны на график"

class PrintTimelines(Algorithm):
    def __init__(self, model):
        super().__init__("Вывести таймлайны", description)
        self.model = model

    def execute_algorithm(self):
        timelines = self.model.get_selected_timelines()
        if len(timelines) == 0:
            return
        self.model.unselect_timelines()
        return create_timeline_bar_chart_from_timelines(timelines)