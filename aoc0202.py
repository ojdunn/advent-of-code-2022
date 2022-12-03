#! python3

from pathlib import Path

outcomeScore = {'X': 0, 'Y': 3, 'Z': 6}  # lose/draw/win = X/Y/Z
moveVals = {'A': 1, 'B': 2, 'C': 3}
loseChoice = {'A': 'C', 'B': 'A', 'C': 'B'}
winChoice = {'A': 'B', 'B': 'C', 'C': 'A'}
drawChoice = {'A': 'A', 'B': 'B', 'C': 'C'}
# X/Y/Z -> choose move to lose/draw/win
outcomeChoice = {'X': loseChoice,
                 'Y': drawChoice,
                 'Z': winChoice
                 }

p = Path("input/input02.txt")
f = open(p)

totalScore = 0
# one line for each round
for line in f.readlines():
    opMove, myOutcome = line.split()

    myVal = moveVals[outcomeChoice[myOutcome][opMove]]

    # total my score for round
    totalScore += myVal + outcomeScore[myOutcome]

print(f'Total score using guide: {totalScore}')
