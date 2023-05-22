KEEP, INSERT, REMOVE, OMIT = 'kiro'

_DEFAULT_FORMATS = {
    KEEP: ' %s',
    INSERT: '+%s',
    REMOVE: '-%s',
    OMIT: '(...%s skipped...)',
}


def myers_diff(a, b):
    front = {1: (0, [])}

    for d in range(0, len(a) + len(b) + 1):
        for k in range(-d, d + 1, 2):
            go_down = k == -d or (k != d and front[k - 1][0] < front[k + 1][0])

            if go_down:
                old_x, history = front[k + 1]
                x = old_x
            else:
                old_x, history = front[k - 1]
                x = old_x + 1
            y = x - k

            history = history[:]

            if 1 <= y <= len(b) and go_down:
                history.append((INSERT, b[y - 1]))
            elif 1 <= x <= len(a):
                history.append((REMOVE, a[x - 1]))

            while x < len(a) and y < len(b) and a[x][2] == b[y][2]:
                x += 1
                y += 1
                history.append((KEEP, a[x - 1]))

            if x >= len(a) and y >= len(b):
                return history

            front[k] = x, history

    raise ValueError('Unable to compute diff')
