#! python3


def createElfSectionSets(elf_pair: str = '0-0,0-0') -> (set, set):
    elfRange1, elfRange2 = elf_pair.split(',')
    # Create sets with all sections to clean for each elf
    start1, end1 = elfRange1.split('-')
    start2, end2 = elfRange2.split('-')
    elf_sections1 = {x for x in range(int(start1), int(end1) + 1)}
    elf_sections2 = {x for x in range(int(start2), int(end2) + 1)}
    return elf_sections1, elf_sections2


if __name__ == '__main__':
    containedRanges = 0
    f = open("input/input04.txt")
    for elfPair in f.readlines():
        elfSections1, elfSections2 = createElfSectionSets(elfPair)
        # Check if one range contains the other
        if elfSections1.issubset(elfSections2) or elfSections2.issubset(elfSections1):
            containedRanges += 1

    print(containedRanges)
