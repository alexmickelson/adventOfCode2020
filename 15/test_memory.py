from typing_extensions import get_args
import memory

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