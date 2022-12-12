#! python3

def num_tail_pos(motions: list[str], num_knots: int) -> int:
    tail_positions = [(0, 0)]  # all knots start at (0, 0) overlapped
    knots = []
    for i in range(num_knots):  # Head at index 0, knot 1..9 at index 1..9 (9 is Tail)
        knots.append((0, 0))
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}  # (x, y) -> (col, row)
    for motion in motions:
        motion = motion.split()
        direction, steps = motion[0], int(motion[1])
        for i in range(steps):
            # First move head knot, then update rest of knots from 1..(num_knots-1)
            knots[0] = (knots[0][0] + dirs[direction][0], knots[0][1] + dirs[direction][1])
            update_knots(knots, 0)
            tail_pos = knots[num_knots - 1]
            if tail_pos not in tail_positions:
                tail_positions.append(tail_pos)

    return len(tail_positions)


def update_knots(knots: list[(int, int)], pos: int):
    # Start with head knot, working backwards
    dx = knots[pos][0] - knots[pos + 1][0]
    dy = knots[pos][1] - knots[pos + 1][1]
    # ((Same row or col)  and (more than 1 apart in x or y)
    if (dx == 0 or dy == 0) and (abs(dx) > 1 or abs(dy) > 1):
        if dx != 0:
            # Moving 1 position right or left
            if dx < 0:
                knots[pos + 1] = (knots[pos + 1][0] - 1, knots[pos + 1][1])
            if dx > 0:
                knots[pos + 1] = (knots[pos + 1][0] + 1, knots[pos + 1][1])
        elif dy != 0:
            # Moving 1 position up or down
            if dy < 0:
                knots[pos + 1] = (knots[pos + 1][0], knots[pos + 1][1] - 1)
            if dy > 0:
                knots[pos + 1] = (knots[pos + 1][0], knots[pos + 1][1] + 1)
    # (Not in same row or col (diagonal))) and (more than 1 apart in x or y)
    elif (dx != 0 and dy != 0) and (abs(dx) > 1 or abs(dy) > 1):
        if dx > 0:
            add_x = 1
        else:
            add_x = -1
        if dy > 0:
            add_y = 1
        else:
            add_y = -1
        knots[pos + 1] = (knots[pos + 1][0] + add_x, knots[pos + 1][1] + add_y)
    if pos < len(knots) - 2:  # compare with up to index (num_knots - 1) in last call
        update_knots(knots, pos + 1)


# f = open('input/input.txt', 'r')  # example input
f = open('input/input09.txt', 'r')
lines = f.readlines()
print('silver: %s' % num_tail_pos(lines, 2))
print('gold: %s' % num_tail_pos(lines, 10))
