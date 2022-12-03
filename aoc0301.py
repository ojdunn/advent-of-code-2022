#! python3

from pathlib import Path

sumP = 0
f = open(Path("input/input03.txt"))
for sack in f.readlines():
    if sack[0] == '\n' or len(sack) < 2:
        continue
    halfSize = int(len(sack) / 2)  # assume even length
    sec1 = sack[:halfSize]
    sec2 = sack[halfSize:]
    for i in range(halfSize):
        if sec1[i] in sec2:
            errorType = sec1[i]
            # use unicode value of char to calculate priority value
            # a-z = 1-26, A-Z = 27-52
            # unicode: 'A' = 65, 'a' = 97
            if errorType.islower():  # lowercase
                sumP += ord(errorType) - 96
            else:  # uppercase
                sumP += ord(errorType) - 38
            break

print(sumP)
