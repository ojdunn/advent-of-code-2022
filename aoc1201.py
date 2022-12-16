#! python3

def steps_reach_best_signal(hmap: list[str]) -> int:
    # Find location of S (start loc)
    # Find location of E (best signal loc)
    xmax, ymax = len(hmap[0]) - 1, len(hmap)  # rows end with a newline
    foundS, foundE = False, False
    xsig, ysig, xstart, ystart = -1, -1, -1, -1
    steps = []
    for y in range(ymax):
        steps.append([])
        for x in range(xmax):
            if hmap[y][x] == 'S':
                xstart, ystart = x, y
                foundS = True
                steps[y].append('.')
            elif hmap[y][x] == 'E':
                xsig, ysig = x, y
                foundE = True
                steps[y].append('E')
            else:
                steps[y].append('.')
    if not foundS or not foundE:
        return -1

    # Find the least number of steps to E.
    # (^, v, <, >) = (up, down, left, right)
    dirs = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}  # (x, y) -> (col, row)
    nsteps = 0
    path = []
    for y in range(ymax):
        for x in range(xmax):
            for d in dirs:
                dx, dy = dirs[d][0], dirs[d][1]

    return steps


f = open('input/input.txt', 'r')  # example input
# f = open('input/input12.txt', 'r')
lines = f.readlines()
print('silver: %s' % steps_reach_best_signal(lines))
# print('gold: ')
