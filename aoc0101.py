#! python3

from pathlib import Path

p = Path('input/input01.txt')
file = open(p)
lines = file.readlines()

calSum = 0
calMax = 0
for line in lines:
    if line[0] == "\n":
        if calSum > calMax:
            calMax = calSum
        calSum = 0
    else:
        calSum += int(line)

print(f'Most calories: {calMax}')
