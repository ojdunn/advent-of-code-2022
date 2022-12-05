#! python3

f = open("input/input05.txt")
lines = f.readlines()
numStacks = len(lines[0]) // 4
stacks = []
for s in range(numStacks):
    stacks.append([])

# Parse init stack config
for i in range(len(lines)):
    pos = 0   # index/position of line string
    for n in range(numStacks):
        # Slice crate if present
        if n == numStacks - 1:
            # Last crate in input is 3 chars long: '[A]'
            crate = lines[i][pos:]
            # print(crate)
        else:
            crate = lines[i][pos: pos + 4]
        # print(crate, end='')
        # All but last crate in input is 4 chars long: '[A] '
        pos += 4
        # crate.isspace() is not True and
        if crate[1].isalpha():
            stacks[n].append(crate[1])
        # numeric and 1 blank line before instructions
        elif crate[1].isnumeric():
            # Do nothing with num line and skip blank line
            i += 2
            # Reverse lists to make stacks from input
            for j in range(numStacks):
                stacks[j].reverse()

            # print(stacks)

            # Parse and follow instructions for stacks
            for k in range(i, len(lines)):
                instruct = lines[k].split()
                # Assign instruction values for stacks
                # - remove 1 to match 0 start index
                quantity, source, dest = \
                    (int(instruct[1]), int(instruct[3]) - 1, int(instruct[5]) - 1)
                # print("%s %s %s" % (quantity, source, dest))

                # PART 1 - stack one at a time
                # for c in range(quantity):
                #     # print(stacks[source])
                #     if len(stacks[source]) != 0:
                #         stacks[dest].append(stacks[source].pop())
                #     else:
                #         print("No more crates in stack %s" % source)
                #         break
                # END PART 1
                # PART 2 - stack whole quantity at once in same order
                if len(stacks[source]) >= quantity:
                    stacks[dest] += stacks[source][-quantity:]
                    del stacks[source][-quantity:]
                else:
                    print("Not enough crates in stack %s" % source)
                # END PART 2

                if k == len(lines) - 1:
                    # Print top of stack
                    topStack = ''
                    for num in range(numStacks):
                        if len(stacks[num]) != 0:
                            topStack += stacks[num].pop()
                        else:
                            print("No crates in stack %i" % (num + 1))
                    print(topStack)
                    exit()
