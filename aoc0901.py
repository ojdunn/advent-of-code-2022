#! python3

def num_tail_pos(motions: list[str]) -> int:
    tail_positions = [(0, 0)]  # H and T both start at (0, 0) overlapped
    head_pos = (0, 0)
    tail_pos = (0, 0)
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}  # (x, y) -> (col, row)
    for motion in motions:
        motion = motion.split()
        direction, steps = motion[0], int(motion[1])
        for i in range(steps):
            head_prev_pos = (head_pos[0], head_pos[1])  # record previous H location
            head_pos = (head_pos[0] + dirs[direction][0], head_pos[1] + dirs[direction][1])
            tail_pos = update_tail_pos(head_prev_pos, head_pos, tail_pos)
            if tail_pos not in tail_positions:
                tail_positions.append(tail_pos)

    return len(tail_positions)


def update_tail_pos(head_prev_pos: (int, int),
                    head_pos: (int, int),
                    tail_pos: (int, int)) -> (int, int):
    dx = head_pos[0] - tail_pos[0]
    dy = head_pos[1] - tail_pos[1]
    # ((Same row or col) or (Not in same row or col (diagonal))) and (more than 1 apart in x or y)
    if ((dx == 0 or dy == 0) or (dx != 0 and dy != 0)) and (abs(dx) > 1 or abs(dy) > 1):
        tail_pos = (head_prev_pos[0], head_prev_pos[1])

    return tail_pos


# f = open('input/input.txt', 'r')  # example input
f = open('input/input09.txt', 'r')
lines = f.readlines()
print('silver: %s' % num_tail_pos(lines))
# print('gold: %s' % )
