import encoding_error as encoding

def test_read_numbers():
    expected_nubmers = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
    ]
    actual_numbers = encoding.read_numbers('example_numbers.txt')
    assert actual_numbers == expected_nubmers

def test_find_pattern_breaking_pattern():
    expected_number = 127
    numbers = encoding.read_numbers('example_numbers.txt')
    actual_number = encoding.find_pattern_breaking_number(numbers, 5)
    assert actual_number == expected_number

def test_find_congruent_numbers_summing():
    expected_numbers = [15, 25, 47, 40]
    numbers = encoding.read_numbers('example_numbers.txt')
    actual_numbers = encoding.find_congurent_numbers_summing(127, numbers)
    assert expected_numbers == actual_numbers

def test_sum_smallest_largest():
    assert encoding.sum_smallest_largest([15, 25, 47, 40]) == 62