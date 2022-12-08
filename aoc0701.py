#! python3

"""
Find sum of all directories in file system with less than or equal to max_size size.
Commands of cd dir_name and ls are used to build a file tree.
"""
def find_dir_less_size_sum(cmds: list[str], max_size: int) -> int:
    # tree_fs = {'/': {'d': {}, 'f': {}}}  # file system tree
    depth_fs = 0  # root is depth 0
    depth_max = 0
    # dirs stored in format:
    # 'dir_name': {'d': [<child dirs>],
    #              'f': [(size, file_name1), .., (size, file_nameN)],
    #              'depth': <int>}  # depth in file system past root (root = 0)
    dirs = {}  # keys are dirs, values are contained dirs and files
    full_path = ['/']
    i = 0
    read_next = True
    while i < len(cmds):
        if read_next:
            tokens = cmds[i].split()
        read_next = True

        # if len(tokens) == 3:
        #     print("%s %s %s" % (tokens[0], tokens[1], tokens[2]))
        # elif len(tokens) == 2:
        #     print("%s %s" % (tokens[0], tokens[1]))
        # else:
        #     print("%s" % (tokens[0]))

        if tokens[0] == '$':
            if tokens[1] == 'cd':
                # Change to root dir
                if tokens[2] == '/':
                    depth_fs = 0
                    cur_dir = '/'
                    full_path = ['/']
                # Move out one level
                elif tokens[2] == '..':
                    if cur_dir != '/':
                        depth_fs -= 1
                        cur_dir = full_path.pop()
                    else:
                        print(i)
                        print('Already at root.')
                # Move in one level to given dir
                # - assumed to be a valid child dir
                else:
                    depth_fs += 1
                    if depth_fs > depth_max:
                        depth_max = depth_fs
                    full_path.append(cur_dir)
                    cur_dir = tokens[2]
                i += 1
            # Read all dirs and files of current dir
            elif tokens[1] == 'ls':
                i += 1
                while i < len(cmds):
                    tokens = cmds[i].split()
                    if tokens[0] == '$':
                        read_next = False
                        break

                    # if len(tokens) == 3:
                    #     print("%s %s %s" % (tokens[0], tokens[1], tokens[2]))
                    # elif len(tokens) == 2:
                    #     print("%s %s" % (tokens[0], tokens[1]))
                    # else:
                    #     print("%s" % (tokens[0]))

                    # dir: add it to contained dirs of current dir
                    if tokens[0] == 'dir':
                        if tokens[1] == '/':
                            print(i)
                            print('/ is root directory. It can\'t be in another '
                                  'directory!')
                        elif cur_dir in list(dirs):
                            if tokens[1] not in dirs[cur_dir]['d']:
                                dirs[cur_dir]['d'].append(tokens[1])
                            else:
                                print(i)
                                print('%s contained in %s already' % (tokens[1], cur_dir))
                        else:
                            dirs[cur_dir] = {'d': [tokens[1]],
                                             'f': [],
                                             'depth': depth_fs}
                    # file: add it to files of current dir
                    elif tokens[0].isnumeric():
                        if cur_dir in list(dirs):
                            # add tuple to file list: (size, filename)
                            if (int(tokens[0]), tokens[1]) not in dirs[cur_dir]['f']:
                                dirs[cur_dir]['f'].append((int(tokens[0]), tokens[1]))
                            else:
                                print(i)
                                print('File: %s already in directory' % tokens[1])
                        else:
                            dirs[cur_dir] = {'d': [],
                                             'f': [(int(tokens[0]), tokens[1])],
                                             'depth': depth_fs}
                    # read next line
                    i += 1
                    # end while

    # Find total size of each dir (only files)
    for d in dirs:
        sum_files = 0
        for size, name in dirs[d]['f']:
            sum_files += size
        # print('sf: %s, size: %d' % (d, sum_files))
        dirs[d]['sf'] = sum_files
        dirs[d]['s'] = 0

    # Find sum including directories
    # print('depth max: %s' % depth_max)
    for i in reversed(range(0, depth_max + 1)):
        for d in dirs:
            if dirs[d]['depth'] == i:
                # Add all directories file sizes contained in this dir
                # print('%s: ' % d, end='')
                sum_dirs = 0
                if len(dirs[d]['d']) > 0:
                    for d_in in dirs[d]['d']:
                        # print('%s, ' % d_in, end='')
                        sum_dirs += dirs[d_in]['s']
                    dirs[d]['s'] = sum_dirs + dirs[d]['sf']
                else:
                    dirs[d]['s'] = dirs[d]['sf']
                # print()
                # print('%s, size: %d' % (d, sum_dirs))

    sum_total = 0
    # Sum all directories <= max_size
    for d in dirs:
        d_size = dirs[d]['s']
        # print("%s size: %s" % (d, d_size))
        if d_size < max_size:
            sum_total += d_size
    print(dirs)

    return sum_total


"""
Find size of all contained files in a directory, including child directories. 
Recursive solution.
"""
# def dir_size(dirs: dict(), d: str, s: int) -> int:
#     # find size of each dir files only
#     if len(dirs[d]['d']) == 0:  # this dir contains no dir(s)
#         print(dirs[d]['d'])
#         print("no dirs, c_d: %s" % d)
#         for size, name in dirs[d]['f']:
#             s += int(size)
#         return s
#     # For all contained directories
#     for contained_d in dirs[d]['d']:
#         print(dirs[d]['d'])
#         print("c_d: %s" % contained_d)
#         # Add sum of all contained files
#         contained_s = 0
#         for size, name in dirs[contained_d]['f']:
#             contained_s += int(size)
#         # Add sum of contained dirs recursively
#         s += dir_size(dirs, contained_d, contained_s)
#     return s


# f = open("input/input.txt")
f = open("input/input07.txt")
lines = f.readlines()
print('Part 1: %i' % find_dir_less_size_sum(lines, 100000))
