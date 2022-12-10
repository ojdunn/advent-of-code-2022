#! python3

"""
Find sum of all directories in file system with less than or equal to max_size size.
Commands of cd dir_name and ls are used to build a file tree.
"""
def find_dir_less_size_sum(cmds: list[str], max_size: int) -> int:
    # dirs stored in format:
    # (('dir_name', depth): {'d': [('child_dir_name', child_depth), ..],
    #                        'f': [(file_name1, size), .., (size, file_nameN)],
    #                        }
    depth_fs = 0  # root is depth 0
    depth_max = 0  # used to move from deepest dirs backwards in sum calc
    dirs = {}  # keys are dirs, values are contained dirs and files
    full_path = []
    i = 0
    read_next = True
    tokens = '\n'
    cur_dir = '/'
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
                # print(cmds[i])
                # Change to root dir
                if tokens[2] == '/':
                    depth_fs = 0
                    cur_dir = '/'
                    full_path = ['/']
                # Move out one level
                elif tokens[2] == '..':
                    if cur_dir != '/':
                        depth_fs -= 1
                        full_path.pop()
                        # print('cur_dir: %s' % cur_dir)
                    else:
                        print(i)
                        print('Already at root.')
                # Move in one level to given dir
                # - assumed to be a valid child dir
                else:
                    depth_fs += 1
                    if depth_fs > depth_max:
                        depth_max = depth_fs
                    if cur_dir != '/':
                        full_path.append(cur_dir)
                    if len(full_path) == 0 and cur_dir == '/':
                        full_path.append('/')
                    cur_dir = tokens[2]
                    # print('cur_dir: %s' % cur_dir)
                i += 1
            # Read all dirs and files of current dir
            elif tokens[1] == 'ls':
                i += 1
                while i < len(cmds):
                    tokens = cmds[i].split()
                    if tokens[0] == '$':
                        read_next = False
                        break

                    # dir: add it to contained dirs of current dir
                    # - can make dirs with same name as parent
                    elif tokens[0] == 'dir':
                        if (cur_dir, depth_fs) not in list(dirs):
                            dirs[(cur_dir, depth_fs)] = \
                                {'d': [(tokens[1], depth_fs + 1)],
                                 'f': []
                                 }
                        else:
                            dirs[(cur_dir, depth_fs)]['d']\
                                .append((tokens[1], depth_fs + 1))
                        if (tokens[1], depth_fs + 1) not in list(dirs):
                            dirs[(tokens[1], depth_fs + 1)] = \
                                {'d': [],
                                 'f': []
                                 }
                    # file: add it to files of current dir
                    # - format: tuple(name, size)
                    elif tokens[0].isnumeric():
                        if (cur_dir, depth_fs) in list(dirs):
                            # add tuple to file list: (size, filename)
                            if (tokens[1], int(tokens[0])) not in \
                                    dirs[(cur_dir, depth_fs)]['f']:
                                dirs[(cur_dir, depth_fs)]['f']\
                                    .append((tokens[1], int(tokens[0])))
                            else:
                                print(i)
                                print('File: %s already in directory %s' %
                                      (tokens[1], cur_dir))
                        else:
                            dirs[(cur_dir, depth_fs)] = \
                                {'d': [],
                                 'f': [(tokens[1], int(tokens[0]))]
                                 }
                    # next line index
                    i += 1
                    # END while

    # Find total size of files for each dir
    for d, depth in dirs:
        sum_files = 0
        for name, size in dirs[(d, depth)]['f']:
            # print('%s\t%s' % (name, size))
            sum_files += size
        # print('sf: %s, size: %d' % (d, sum_files))
        dirs[(d, depth)]['sf'] = sum_files  # sum of contained files
        dirs[(d, depth)]['s'] = 0           # sum including contained dirs

    # Find sum including directories
    # Starting summing from deepest dirs, summing backwards
    # print('depth max: %s' % depth_max)
    print(dirs)
    for i in reversed(range(0, depth_max + 1)):
        for d, depth in dirs:
            # print('%s, %s' % (d, depth))
            if depth == i:
                # Add all directories file sizes contained in this dir
                # print('(%s, %s),' % (d, depth), end='\t')
                if len(dirs[(d, depth)]['d']) > 0:
                    sum_dirs = 0
                    for d_in, depth_d_in in dirs[(d, depth)]['d']:
                        # print('%s, ' % d_in, end='')
                        sum_dirs += dirs[(d_in, depth_d_in)]['s']
                    dirs[(d, depth)]['s'] = sum_dirs + dirs[(d, depth)]['sf']
                else:
                    dirs[(d, depth)]['s'] = dirs[(d, depth)]['sf']
                # print('%s, size: %d' % (d, sum_dirs))
        # print()

    # Sum all directories <= max_size
    silver = 0
    for d, depth in dirs:
        # print('%s\t%s' % (d, depth))
        d_size = dirs[(d, depth)]['s']
        # print(d_size)
        # print("%s size: %s" % (d, d_size))
        if d_size <= max_size:
            silver += d_size

    # print(dirs)
    # print(list(dirs))
    # if len(list(dirs)) != len(set(dirs)):
    #     print('repeats')

    return silver


# f = open("input/input.txt")
f = open("input/input07.txt")
lines = f.readlines()
print('silver: %i' % find_dir_less_size_sum(lines, 100000))
