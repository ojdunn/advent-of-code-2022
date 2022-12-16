#! python3


def min_steps_reach_signal(hmap: list[str]) -> int:
    # Find location of S (start loc)
    # Find location of E (best signal loc)
    foundS, foundE = False, False
    xsig, ysig, xstart, ystart = -1, -1, -1, -1
    for y in range(ymax):
        path_map.append([])
        for x in range(xmax):
            if hmap[y][x] == 'S':
                xstart, ystart = x, y
                foundS = True
                path_map[y].append('.')
            elif hmap[y][x] == 'E':
                xsig, ysig = x, y
                foundE = True
                path_map[y].append('E')
            else:
                path_map[y].append('.')
    if not foundS or not foundE:
        return -1

    # Find the least number of steps to E.
    nsteps = 0
    path = [(xstart, ystart)]
    find_paths(path, nsteps, (xsig, ysig))

    return min(steps2sig)


def find_paths(path: [(int, int)],
               nsteps: int,
               sig_pos: (int, int),
               ):
    # might have to use last position in parameters instead as path may get appended in unpredictable order
    if path[-1] == sig_pos:
        print('steps: %s' % nsteps)
        steps2sig.append(nsteps)
        path.pop()  # explore other paths
        return
    moved = False
    for d in dirs:
        dx, dy = dirs[d][0], dirs[d][1]
        pos_from = (path[-1][0], path[-1][1])
        pos_to = (path[-1][0] + dx, path[-1][1] + dy)
        if 0 <= pos_to[0] < xmax and 0 <= pos_to[1] < ymax:
            from_char = lines[pos_from[1]][pos_from[0]]
            if from_char == 'S':
                from_char = 'a'
            from_height = ord(from_char)
            to_char = lines[pos_to[1]][pos_to[0]]
            if to_char == 'E':
                to_char = 'z'
            to_height = ord(to_char)
            if to_height <= from_height + 1:
                if pos_to not in path:
                    path.append(pos_to)
                    find_paths(path, nsteps + 1, sig_pos)
                    moved = True
    path.pop()  # explore other paths


if __name__ == '__main__':
    # f = open('input/input.txt', 'r')  # example input
    f = open('input/input12.txt', 'r')
    lines = f.readlines()

    # (^, v, <, >) = (up, down, left, right)
    dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}  # (x, y) -> (col, row)
    path_map = []
    steps2sig = []
    xmax, ymax = len(lines[0]) - 1, len(lines)  # rows end with a newline

    print('silver: %s' % min_steps_reach_signal(lines))
    # print('gold: ')
