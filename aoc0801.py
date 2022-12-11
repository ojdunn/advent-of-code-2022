#! python3

def find_total_visible(grid: list[str]) -> (int, int):
    # Add all edge trees to count of visible trees
    # - grid lines end with \n, last line has no newline
    total_visible = ((len(grid[0]) - 2 - 1) * 2) + (len(grid) * 2)

    # Check if each tree within grid is visible and not on edge
    rows = len(grid)
    cols = len(grid[0]) - 1
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # For each tree, check up, down, left, right of grid to see if visible
            height = int(grid[r][c])
            visible = True
            for direction in 'udlr':  # up, down, left, right
                if direction == 'u':
                    for i in range(r - 1, -1, -1):
                        if int(grid[i][c]) >= height:
                            visible = False
                            break
                        visible = True
                elif direction == 'd':
                    for i in range(r + 1, rows, 1):
                        if int(grid[i][c]) >= height:
                            visible = False
                            break
                        visible = True
                elif direction == 'l':
                    for i in range(c - 1, -1, -1):
                        if int(grid[r][i]) >= height:
                            visible = False
                            break
                        visible = True
                elif direction == 'r':
                    for i in range(c + 1, cols, 1):
                        if int(grid[r][i]) >= height:
                            visible = False
                            break
                        visible = True
                if visible:
                    total_visible += 1
                    break

    return total_visible


def find_max_scenic_score(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0]) - 1
    max_scenic_score = 0
    vd_up, vd_down, vd_left, vd_right = 0, 0, 0, 0
    i = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # For each tree, check up, down, left, right of grid to see if visible
            height = int(grid[r][c])
            for direction in 'udlr':  # up, down, left, right
                if direction == 'u':
                    vd_up = 1
                    for i in range(r - 1, -1, -1):
                        if int(grid[i][c]) >= height or i == 0:
                            break
                        vd_up += 1
                elif direction == 'd':
                    vd_down = 1
                    for i in range(r + 1, rows, 1):
                        if int(grid[i][c]) >= height or i == rows - 1:
                            break
                        vd_down += 1
                elif direction == 'l':
                    vd_left = 1
                    for i in range(c - 1, -1, -1):
                        if int(grid[r][i]) >= height or i == 0:
                            break
                        vd_left += 1
                elif direction == 'r':
                    vd_right = 1
                    for i in range(c + 1, cols, 1) or i == cols - 1:
                        if int(grid[r][i]) >= height:
                            break
                        vd_right += 1

            scenic_score = vd_up * vd_down * vd_left * vd_right
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


# f = open('input/input.txt', 'r')  # example input
f = open('input/input08.txt', 'r')
lines = f.readlines()
print('silver: %s' % find_total_visible(lines))
print('gold: %s' % find_max_scenic_score(lines))
