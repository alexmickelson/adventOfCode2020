

def starting_cube(file_name):
    start = list(open(file_name).read().split('\n'))
    width = len(start)
    return [
        [
            ['.'*width for i in range(width)],
            start,
            ['.'*width for i in range(width)]
        ]
    ]


def get_neigbor_count(i_base, j_base, k_base, l_base, cube):
    neighbor_count = 0
    for i in [i_base-1, i_base, i_base+1]:
        if i in range(len(cube)):
            for j in [j_base-1, j_base, j_base+1]:
                if j in range(len(cube[i])):
                    for k in [k_base-1, k_base, k_base+1]:
                        if k in range(len(cube[i][j])):
                            for l in [l_base-1, l_base, l_base + 1]:
                                if l in range(len(cube[i][j][k])):
                                    if((i != i_base or j != j_base or k != k_base or l != l_base) and cube[i][j][k][l] == '#'):
                                        neighbor_count += 1
    return neighbor_count


def do_cycle(cube):
    # pad cube with '.'s
    # i_width = len(cube)
    j_width = len(cube[0])
    k_width = len(cube[0][0])
    l_width = len(cube[0][0][0])
    # for i in range(len(cube)):
    #     cube[i].insert(0, ['.'*starting_width for i in range(starting_width)])
    #     cube[i].append(['.'*starting_width for i in range(starting_width)])

    cube.insert(0, [['.'*l_width for j in range(k_width)]
                    for i in range(j_width)])
    cube.append([['.'*l_width for j in range(k_width)]
                    for i in range(j_width)])

    for i in range(len(cube)):
        cube[i].insert(0, ['.'*l_width for _ in range(k_width)])
        cube[i].append(['.'*l_width for _ in range(k_width)])
        for j in range(len(cube[i])):
            cube[i][j].insert(0, '.' * l_width)
            cube[i][j].append('.' * l_width)
            for k in range(len(cube[i][j])):
                cube[i][j][k] = '.' + cube[i][j][k] + '.'

    next_cube = []
    for i in range(len(cube)):
        next_cube.append([])
        for j in range(len(cube[0])):
            next_cube[i].append([])
            for k in range(len(cube[0][0])):
                next_cube[i][j].append('')
                for l in range(len(cube[0][0][0])):
                    neighbor_count = get_neigbor_count(i, j, k, l, cube)
                    if cube[i][j][k][l] == '#' and neighbor_count in [2, 3]:
                        next_cube[i][j][k] = next_cube[i][j][k] + '#'
                    elif neighbor_count == 3:
                        next_cube[i][j][k] = next_cube[i][j][k] + '#'
                    else:
                        next_cube[i][j][k] = next_cube[i][j][k] + '.'
    return next_cube


def count_alive(cube):
    count = 0
    for plane in cube:
        for row in plane:
            for dot in row:
                for d in dot:
                    if d == '#':
                        count += 1
    return count


if __name__ == "__main__":
    cube = starting_cube('input.txt')
    for _ in range(6):
        cube = do_cycle(cube)
    alive = count_alive(cube)
    print(f'# of active cubes: {alive}')
