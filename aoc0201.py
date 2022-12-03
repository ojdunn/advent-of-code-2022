#! python3

from pathlib import Path

myVals = {'X':1, 'Y':2, 'Z':3}
event = {'AX': 0, 'AY': 1, 'AZ': -1,
         'BX': -1, 'BY': 0, 'BZ': 1,
         'CX': 1, 'CY': -1, 'CZ': 0
        }
outcomeScore = {-1:0, 0:3, 1:6}  # lose/draw/win = -1/0/1

p = Path("input/input02.txt")
f = open(p)

myVal = 0
totalScore = 0
# one line for each round
for line in f.readlines():
    moves = ''.join(line.split())
    myMove = moves[1]
    myVal = myVals[myMove]

    # total my score for round
    totalScore += myVal + outcomeScore[event[moves]]

print(f'Total score using guide: {totalScore}')
