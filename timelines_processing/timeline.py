import csv

class Timeline:
    def __init__(self, timeline_name, start_times_list, end_times_list, actions_list):
        self.timeline_name = timeline_name
        self.start_times = start_times_list
        self.end_times = end_times_list
        self.actions = actions_list

    def sort_by_start_time(self):
        self.start_times, self.end_times, self.actions = zip(
            *sorted(zip(self.start_times, self.end_times, self.actions)))

    def get_name(self):
        return self.timeline_name

    def get_actions(self):
        return list(self.actions)

    def get_pairs(self):
        return list(zip(self.start_times, self.actions))

    def get_tuples(self):
        return list(zip(self.start_times, self.end_times, self.actions))


def convert_to_timeline(result):
    return Timeline([x[0] for x in result], [x[1] for x in result], [x[2] for x in result])


def parse_csv_to_timeline(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        start_times = []
        end_times = []
        actions = []
        for row in reader:
            start_times.append(float(row[0]))
            end_times.append(float(row[1]))
            actions.append(''.join(row[2:]))

        name = filename.split('\\')[-1].split('.')[0]

    return Timeline(name, start_times, end_times, actions)
