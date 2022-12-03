#! python3

from pathlib import Path

sumP = 0
f = open(Path("input/input03.txt"))
allLines = f.readlines()
totalLines = len(allLines)
totalGroups = int(totalLines / 3)

# look through 3 lines at a time: assume list is a multiple of 3
linesIndex = 0
for i in range(totalGroups):
    sacks = allLines[linesIndex: linesIndex + 3]
    linesIndex += 3
    # Find what type is common among all 3 sacks of group
    # Check for each item in first sack against all items in 2nd, 3rd sacks
    for j in range(len(sacks[0])):
        if sacks[0] == '\n' or len(sacks[0]) < 2:
            break
        itemType = sacks[0][j]
        if itemType in sacks[1] and itemType in sacks[2]:
            # use unicode value of char to calculate priority value
            # a-z = 1-26, A-Z = 27-52
            # unicode: 'A' = 65, 'a' = 97
            if itemType.islower():  # lowercase
                sumP += ord(itemType) - 96
            else:  # uppercase
                sumP += ord(itemType) - 38
            break

print(sumP)
