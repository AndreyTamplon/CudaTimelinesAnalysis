from algorithm import Algorithm
from algorithms.common import create_timeline_bar_chart_from_timelines, create_timeline_bar_chart_from_myers_output
from vector_comparsion.myers import myers_diff
from vector_comparsion.vector_comparsion import get_timelines_from_diff

description = "Алгоритм Майерса - это алгоритм сравнения \nфайлов, который находит наибольшую общую \n" \
              "подпоследовательность (LCS) между двумя\n последовательностями элементов.\n Алгоритм Майерса использует \n" \
              "жадный подход, который строит график\n редактирования из так \nназываемых змеек - последовательностей \n" \
              "совпадающих элементов. \nАлгоритм Майерса имеет сложность O(ND),\n где N - это сумма длин двух \n" \
              "последовательностей,\n а D - это количество различий между ними.\n Алгоритм Майерса применяется в утилите \n" \
              "diff, которая выводит разницу\n между двумя текстовыми файлами\n в виде патча. Патч показывает, \n" \
              "какие строки нужно добавить\n или удалить из одного файла,\n чтобы получить другой.\n Алгоритм Майерса также \n" \
              "может использоваться\n для других типов данных,\n которые имеют оператор равенства.\n"
class Myers(Algorithm):
    def __init__(self, model):
        super().__init__("Алгоритм Майерса", description)
        self.model = model

    def execute_algorithm(self):
        timelines = self.model.get_selected_timelines()
        if len(timelines) != 2:
            return

        timeline_1 = timelines[0]
        timeline_2 = timelines[1]

        diff = myers_diff(timeline_1.get_tuples(), timeline_2.get_tuples())
        sorted_diff = sorted(diff, key=lambda x: x[1][0])
        tm1, tm2 = get_timelines_from_diff(sorted_diff)
        self.model.unselect_timelines()
        return create_timeline_bar_chart_from_myers_output([tm1, tm2])




