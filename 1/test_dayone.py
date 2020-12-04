from day_one import find_numbers_summing_to, mutiply_numbers_with_sum_2020

def test_find_numbers_summing():
    example_list = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    expected_numbers = (1721, 299)
    assert find_numbers_summing_to(example_list, 2020, 2) == expected_numbers

def test_mutiple_of_numbers_summing_2020():
    example_list = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    assert mutiply_numbers_with_sum_2020(example_list, 2) == 514579
    assert mutiply_numbers_with_sum_2020(example_list, 3) == 241861950
