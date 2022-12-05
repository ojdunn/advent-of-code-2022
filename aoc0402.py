#! python3
from aoc0401 import createElfSectionSets

if __name__ == '__main__':
    overlappedRanges = 0
    f = open("input/input04.txt")
    for elfPair in f.readlines():
        elfSections1, elfSections2 = createElfSectionSets(elfPair)

        # Check if one range contains any sections of the other:
        # if intersection of two sets has any elements, there is some overlap
        if len(elfSections1.intersection(elfSections2)) != 0:
            overlappedRanges += 1

    print(overlappedRanges)
