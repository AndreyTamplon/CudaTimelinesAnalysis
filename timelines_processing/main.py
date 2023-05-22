from timeline import Timeline, convert_to_timeline
from timeline_db import TimelineDB
from query import Query
from vector_comparsion import vector_comparsion as vc

query_path = "../queries/kernel_calls.sql"
database_1 = "../timelines/fock_frc_209.sqlite"
database_2 = "../timelines/fock_frc_212.sqlite"
timeline_db_1 = TimelineDB(database_1)
timeline_db_1.open()
timeline_db_2 = TimelineDB(database_2)
timeline_db_2.open()
query = Query(query_path)
query.open()
result_1 = timeline_db_1.execute(query.get_query())
result_2 = timeline_db_2.execute(query.get_query())
timeline_db_1.close()
timeline_db_2.close()
result_1 = [[(x[0] - result_1[0][0]) / 1000, (x[1] - result_1[0][0]) / 1000, x[2]] for x in result_1]
result_2 = [[(x[0] - result_2[0][0]) / 1000, (x[1] - result_2[0][0]) / 1000, x[2]] for x in result_2]

timeline_1 = Timeline("timeline_1", [x[0] for x in result_1], [x[1] for x in result_1], [x[2] for x in result_1])
timeline_2 = Timeline("timeline_2", [x[0] for x in result_2], [x[1] for x in result_2], [x[2] for x in result_2])
timeline_1.sort_by_start_time()
timeline_2.sort_by_start_time()
# save timelines to csv files
with open('../timelines/timeline5.csv', 'w') as f:
    for i in range(len(timeline_1.get_actions())):
        f.write(str(timeline_1.start_times[i]) + ',' + str(timeline_1.end_times[i]) + ',' + timeline_1.actions[i] + '\n')

with open('../timelines/timeline6.csv', 'w') as f:
    for i in range(len(timeline_2.get_actions())):
        f.write(str(timeline_2.start_times[i]) + ',' + str(timeline_2.end_times[i]) + ',' + timeline_2.actions[i] + '\n')


# diff = vc.myers_diff(timeline_1.get_tuples(), timeline_2.get_tuples())
# sorted_diff = sorted(diff, key=lambda x: x[1][0])
# vc.print_diff(sorted_diff)
# tm1, tm2 = vc.get_timelines_from_diff(sorted_diff)
# # visualizer.visualize_timelines(timeline_1, timeline_1)