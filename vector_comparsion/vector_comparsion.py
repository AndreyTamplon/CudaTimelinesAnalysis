import vector_comparsion.myers as myers


def pairwise_comparison(v1, v2):
    """Compare two vectors and return the number of elements that are equal."""
    if len(v1) < len(v2):
        return ((sum([1 for i in range(len(v1)) if v1[i] != v2[i]]) + len(v1) - len(v2)) / len(v1)) * 100
    else:
        return ((sum([1 for i in range(len(v2)) if v1[i] != v2[i]]) + len(v2) - len(v1)) / len(v2)) * 100


def myers_diff(v1, v2):
    """Calculate the mayers similarity between two vectors."""
    return myers.myers_diff(v1, v2)


def print_diff(diff):
    """Print the diff."""
    for line in diff:
        if line[0] == myers.INSERT:
            print('\033[92m' + str(line[1]))
        elif line[0] == myers.REMOVE:
            print('\033[91m' + str(line[1]))
        elif line[0] == myers.OMIT:
            print('... ' + str(line[1]) + ' lines omitted ...')


def get_timelines_from_diff(diff):
    """Get the timelines from the diff."""
    timeline_1 = []
    timeline_2 = []
    for line in diff:
        if line[0] == myers.INSERT:
            timeline_2.append(line[1])
        elif line[0] == myers.REMOVE:
            timeline_1.append(line[1])
    return timeline_1, timeline_2
