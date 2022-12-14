#! python3

def sum_signal_strengths(instructs: list[str], max_num: int) -> int:
    X = 1           # X register value
    cycle = 1       # cycle CPU is at
    num = 0         # number of signal strengths measured so far
    sig_strs = []   # recorded signal strengths
    pos = 0         # horizontal position CRT is drawing now
    for instruct in instructs:
        instruct = instruct.split()
        if len(instruct) > 1:  # addx, takes effect after 2 cycles
            icycles = 2  # num cycles for the instruction to run
            sval = int(instruct[1])
        else:  # noop, 1 cycle
            icycles = 1
        for c in range(icycles):
            # signal strength = cycle * X register value
            # - measure at: f(c) = 20 + 40 * c, c = 0, 1, .., max_num - 1
            if cycle == 20 + 40 * num and num < max_num:
                sig_strs.append(cycle * X)
                num += 1
            if X - 1 <= pos <= X + 1:
                print('#', end='')
            else:
                print('.', end='')
            if cycle % 40 == 0:
                print()
                pos = 0
            else:
                pos += 1
            cycle += 1

        if instruct[0] == 'addx':
            X += sval

    print()
    return sum(sig_strs)


# f = open('input/input.txt', 'r')  # example input
f = open('input/input10.txt', 'r')
lines = f.readlines()
print('silver: %s' % sum_signal_strengths(lines, 6))
print('gold: see what capital letters are printed!')
