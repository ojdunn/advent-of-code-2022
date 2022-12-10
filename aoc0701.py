#! python3

def find_dir_less_size_sum(cmds: list[str], max_size: int) -> int:
    # dirs stored in format:
    # (('path', depth): {'d': [('child_path', child_depth), ..],
    #                    'f': [(file_name1, size), .., (size, file_nameN)],
    #                    }
    depth_fs = 0  # root is depth 0
    depth_max = 0  # used to move from deepest dirs backwards in sum calc
    dirs = {}  # keys are dirs, values are contained dirs and files
    path = []
    i = 0
    read_next = True
    tokens = '\n'
    cur_dir = '/'
    while i < len(cmds):
        if read_next:
            tokens = cmds[i].split()
        read_next = True

        if tokens[0] == '$':
            if tokens[1] == 'cd':
                # Change to root dir
                if tokens[2] == '/':
                    depth_fs = 0
                    path = ['/']
                # Move out one level
                elif tokens[2] == '..':
                    if cur_dir != '/':
                        depth_fs -= 1
                        path.pop()
                    else:
                        print(i)
                        print('Already at root.')
                # Move in one level to given dir
                # - assumed to be a valid child dir
                else:
                    depth_fs += 1
                    if depth_fs > depth_max:
                        depth_max = depth_fs
                    path.append(tokens[2])
                i += 1
            # Read all dirs and files of current dir
            elif tokens[1] == 'ls':
                path_key = "/".join(path)
                cur_dir = path[-1]
                i += 1
                while i < len(cmds):
                    tokens = cmds[i].split()

                    if tokens[0] == '$':
                        read_next = False
                        break

                    # dir: add it to contained dirs of current dir
                    # - can make dirs with same name as parent
                    elif tokens[0] == 'dir':
                        child_path = path.copy()
                        child_path.append(tokens[1])
                        child_path_key = "/".join(child_path)
                        if (path_key, depth_fs) not in list(dirs):
                            dirs[(path_key, depth_fs)] = \
                                {'d': [(child_path_key, depth_fs + 1)],
                                 'f': []
                                 }
                        else:
                            dirs[(path_key, depth_fs)]['d']\
                                .append((child_path_key, depth_fs + 1))
                        if (child_path_key, depth_fs + 1) not in list(dirs):
                            dirs[(child_path_key, depth_fs + 1)] = \
                                {'d': [],
                                 'f': []
                                 }
                    # file: add it to files of current dir
                    # - format: tuple(name, size)
                    elif tokens[0].isnumeric():
                        # add tuple to file list: (size, filename)
                        if (path_key, depth_fs) in list(dirs):
                            dirs[(path_key, depth_fs)]['f']\
                                .append((tokens[1], int(tokens[0])))
                        else:
                            dirs[(path_key, depth_fs)] = \
                                {'d': [],
                                 'f': [(tokens[1], int(tokens[0]))]
                                 }
                    # next line index
                    i += 1
                    # END while

    # Find total size of files for each dir
    # Non-recursive solution
    # - recursive solution as function below (both have same solutions)
    # for d, depth in dirs:
    #     sum_files = 0
    #     for name, size in dirs[(d, depth)]['f']:
    #         # print('%s\t%s' % (name, size))
    #         sum_files += size
    #     # print('sf: %s, size: %d' % (d, sum_files))
    #     dirs[(d, depth)]['sf'] = sum_files  # sum of contained files
    #     dirs[(d, depth)]['s'] = 0           # sum including contained dirs
    #
    # # Find sum including directories
    # # Starting summing from deepest dirs, summing backwards
    # # print('depth max: %s' % depth_max)
    # print(dirs)
    # for i in reversed(range(0, depth_max + 1)):
    #     for d, depth in dirs:
    #         # print('%s, %s' % (d, depth))
    #         if depth == i:
    #             # Add all directories file sizes contained in this dir
    #             # print('(%s, %s),' % (d, depth), end='\t')
    #             if len(dirs[(d, depth)]['d']) > 0:
    #                 sum_dirs = 0
    #                 for d_in, depth_d_in in dirs[(d, depth)]['d']:
    #                     # print('%s, ' % d_in, end='')
    #                     sum_dirs += dirs[(d_in, depth_d_in)]['s']
    #                 dirs[(d, depth)]['s'] = sum_dirs + dirs[(d, depth)]['sf']
    #             else:
    #                 dirs[(d, depth)]['s'] = dirs[(d, depth)]['sf']
    #             # print('%s, size: %d' % (d, sum_dirs))
    #     # print()

    silver = 0
    for path_key, depth in dirs:
        size = find_dir_size(dirs, (path_key, depth))
        if size <= max_size:
            silver += size

    # print(dirs)
    # print(list(dirs))

    return silver


"""
Find the directory size including all files and directories. A directory contained may 
have files and directories of its own. Recursion used.
"""
def find_dir_size(dirs: dict(), d: (str, int)):
    fs = 0
    for name, size in dirs[d]['f']:
        fs += size
    ds = 0
    for child_path_key, depth_child in dirs[d]['d']:
        ds += find_dir_size(dirs, (child_path_key, depth_child))
    return fs + ds


f = open("input/input07.txt", 'r')
# f = open("input/input.txt")
lines = f.readlines()
print('silver: %i' % find_dir_less_size_sum(lines, 100000))
