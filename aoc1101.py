#! python3

def find_monkey_business(info: list[str], rounds: int) -> int:
    num_monkeys = (len(info) + 1) // 7  # a monkey data list is 7 lines long (last line is space)
    # Parse the input and store data in dict
    monkeys = {}
    for n in range(num_monkeys):
        monkey_data = info[(n * 7):(n * 7 + 7)]
        monkeys[n] = {'i': [],       # items (worry value)
                      'o': tuple(),  # operation (operator, right operand)
                      't': tuple(),  # test [divisible by, if true give to monkey, if false]
                      'c': 0         # item inspection count
                      }
        # Parse starting items and add to list in order
        start_items = monkey_data[1]
        start_items = start_items[(start_items.index(':') + 2):-1].split(', ')
        for item in start_items:
            monkeys[n]['i'].append(int(item))
        monkey_op = monkey_data[2].split()[-2:]
        if monkey_op[1] == 'old':
            monkeys[n]['o'] = (monkey_op[0], monkey_op[1])
        else:
            monkeys[n]['o'] = (monkey_op[0], int(monkey_op[1]))
        monkeys[n]['t'] = [int(monkey_data[3].split()[-1]),  # Divisible by int
                           int(monkey_data[4].split()[-1]),  # if true, give to monkey int
                           int(monkey_data[5].split()[-1])  # if false, give to monkey int
                           ]

    # Play monkey in the middle for "rounds" rounds
    for r in range(rounds):
        # For each monkey: 0 .. num_monkeys-1
        for m in monkeys:
            # Inspect items in order
            for i in monkeys[m]['i']:  # item is int worry value
                if monkeys[m]['o'][1] == 'old':  # right operand is the old item value
                    if monkeys[m]['o'][0] == '*':
                        i *= i
                    else:
                        i += i
                else:  # right operand is an int
                    if monkeys[m]['o'][0] == '*':
                        i *= monkeys[m]['o'][1]
                    else:
                        i += monkeys[m]['o'][1]

                i //= 3  # Assign i to floor of divide by 3
                monkeys[m]['c'] += 1  # Increment item inspection count

                # Test item
                if i % monkeys[m]['t'][0] == 0:
                    monkeys[monkeys[m]['t'][1]]['i'].append(i)
                else:
                    monkeys[monkeys[m]['t'][2]]['i'].append(i)
            monkeys[m]['i'].clear()  # all items passed to other monkeys, so clear list

    # Find monkey business value and return it
    inspect_count = []
    for m in monkeys:
        inspect_count.append(monkeys[m]['c'])
    inspect_count.sort()  # ascending order sort

    return inspect_count[-1] * inspect_count[-2]


# f = open('input/input.txt', 'r')  # example input
f = open('input/input11.txt', 'r')
lines = f.readlines()
print('silver: %s' % find_monkey_business(lines, 20))
# print('gold:')
