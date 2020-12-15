from typing_extensions import get_args
import memory

# def test_get_next_number():
#     starting_numbers = memory.read_starting_numbers('example.txt')
#     actual_next_number  = memory.get_next_number(starting_numbers)
#     assert actual_next_number == 0
#     starting_numbers.append(actual_next_number)
#     actual_second_number = memory.get_next_number(starting_numbers)
#     assert actual_second_number == 1

# def test_get_next_number():
#     starting_numbers = memory.read_starting_numbers('example2.txt')
#     actual_next_number  = memory.get_next_number(starting_numbers)
#     assert actual_next_number == 0
#     starting_numbers.append(actual_next_number)
#     actual_second_number = memory.get_next_number(starting_numbers)
#     assert actual_second_number == 3
#     starting_numbers.append(actual_second_number)
#     actual_third_number = memory.get_next_number(starting_numbers)
#     assert actual_third_number == 3

# def test_extend_list_to():
#     starting_numbers = [0, 3, 6]
#     actual_numbers = memory.extend_list_to(starting_numbers, 11)
#     expected_numbers = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0, 2]
#     assert actual_numbers == expected_numbers

# def test_extend_list_to():
#     starting_numbers = [1, 3, 2]
#     actual_numbers = memory.extend_list_to(starting_numbers, 11)
#     expected_numbers = [1, 3, 2, 0, 0, 1, 5, 0, 3, 7, 0]
#     assert actual_numbers == expected_numbers


def test_2020th_number():
    starting_numbers = [1, 3, 2]
    actual_number = memory.get_number_at_count(4, starting_numbers)
    expected_number = 0
    assert actual_number == expected_number

def test_2020th_number1():
    starting_numbers = [1, 3, 2]
    actual_number = memory.get_number_at_count(2020, starting_numbers)
    expected_number = 1
    assert actual_number == expected_number

def test_2020th_number2():
    starting_numbers = [1, 2, 3]
    actual_number = memory.get_number_at_count(2020, starting_numbers)
    expected_number = 27
    assert actual_number == expected_number

def test_2020th_number3():
    starting_numbers = memory.read_starting_numbers('example3.txt')
    actual_number = memory.get_number_at_count(2020, starting_numbers)
    expected_number = 438
    assert actual_number == expected_number