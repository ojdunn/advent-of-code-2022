#! python3

from pathlib import Path

p = Path('input/input01.txt')
file = open(p)
lines = file.readlines()

top3 = [0, 0, 0]
calSum = 0
for line in lines:
    if line[0] == "\n":
        if calSum > min(top3):
            top3.append(calSum)
            top3.remove(min(top3))
        calSum = 0
    else:
        calSum += int(line)

print(f'Top 3 calories sum: {sum(top3)}')
