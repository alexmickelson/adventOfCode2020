import conway_cube


# def test_get_starting_cube():
#     expected_starting_cube = [
#         [
#             [
#                 '...',
#                 '...',
#                 '...',
#             ],
#             [
#                 '.#.',
#                 '..#',
#                 '###',
#             ],
#             [
#                 '...',
#                 '...',
#                 '...',
#             ],
#         ]
#     ]
#     actual_starting_cube = conway_cube.starting_cube('example.txt')
#     assert actual_starting_cube == expected_starting_cube


# def test_get_neigbor_count():
#     cube = [
#         [
#             '.#.',
#             '..#',
#             '###',
#         ]
#     ]
#     expected_neighbor_count = 1
#     actual_neighbor_count = conway_cube.get_neigbor_count(0, 0, 0, cube)
#     assert actual_neighbor_count == expected_neighbor_count


# def test_get_neigbor_count2():
#     cube = [
#         [
#             '#..',
#             '..#',
#             '.#.',
#         ],
#         [
#             '#.#',
#             '.##',
#             '.#.',
#         ],
#         [
#             '#..',
#             '..#',
#             '.#.',
#         ],
#     ]
#     expected_neighbor_count = 10
#     actual_neighbor_count = conway_cube.get_neigbor_count(1, 1, 1, cube)
#     assert actual_neighbor_count == expected_neighbor_count


# def test_get_neigbor_count3():
#     cube = [
#         ['.....', '.....', '.....', '.....', '.....'],
#         ['.....', '.#...', '...#.', '..#..', '.....'],
#         ['.....', '.#.#.', '..##.', '..#..', '.....'],
#         ['.....', '.#...', '...#.', '..#..', '.....'],
#         ['.....', '.....', '.....', '.....', '.....'],
#     ]
#     expected_neighbor_count = 3
#     actual_neighbor_count = conway_cube.get_neigbor_count(0, 2, 2, cube)
#     assert actual_neighbor_count == expected_neighbor_count


# def test_do_cycle():
#     cube = [
#         [
#             '#..',
#             '..#',
#             '.#.',
#         ],
#         [
#             '#.#',
#             '.##',
#             '.#.',
#         ],
#         [
#             '#..',
#             '..#',
#             '.#.',
#         ],
#     ]
#     actual_cycle_1 = conway_cube.do_cycle(cube)
#     expected_cycle_1 = [
#         [
#             '.....',
#             '.....',
#             '..#..',
#             '.....',
#             '.....',
#         ],
#         [
#             '..#..',
#             '.#..#',
#             '....#',
#             '.#...',
#             '.....',
#         ],
#         [
#             '##...',
#             '##...',
#             '#....',
#             '....#',
#             '.###.',
#         ],
#         [
#             '..#..',
#             '.#..#',
#             '....#',
#             '.#...',
#             '.....',
#         ],
#         [
#             '.....',
#             '.....',
#             '..#..',
#             '.....',
#             '.....',
#         ],
#     ]
#     assert actual_cycle_1 == expected_cycle_1


# def test_count_alive():
#     cube = [
#         [
#             '.....',
#             '.....',
#             '..#..',
#             '.....',
#             '.....',
#         ],
#         [
#             '..#..',
#             '.#..#',
#             '....#',
#             '.#...',
#             '.....',
#         ],
#         [
#             '##...',
#             '##...',
#             '#....',
#             '....#',
#             '.###.',
#         ],
#         [
#             '..#..',
#             '.#..#',
#             '....#',
#             '.#...',
#             '.....',
#         ],
#         [
#             '.....',
#             '.....',
#             '..#..',
#             '.....',
#             '.....',
#         ],
#     ]
#     expected_alive = 21
#     actual_alive = conway_cube.count_alive(cube)
#     assert actual_alive == expected_alive


def test_4_dimension_cycle():
    cube = [
        [
            [
                '...',
                '...',
                '...',
            ],
            [
                '.#.',
                '..#',
                '###',
            ],
            [
                '...',
                '...',
                '...',
            ],
        ]
    ]
    expected_cycle_1 = [
        [  # w = -1
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
        ],
        [  # w = 0
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#.#.',
                '..##.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
        ],
        [  # w = 1
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
            [
                '.....',
                '.#...',
                '...#.',
                '..#..',
                '.....',
            ],
        ]
    ]
    actual_cycle_1 = conway_cube.do_cycle(cube)
    assert actual_cycle_1 == expected_cycle_1
