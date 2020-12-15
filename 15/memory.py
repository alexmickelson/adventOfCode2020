# import sys


# sys.setrecursionlimit(30_000_002)

def read_starting_numbers(file_name):
    return [int(i) for i in open(file_name).read().replace('\n', '').split(',')]

def get_next_number(numbers, previous_number, previous_number_count):
    last_occurence_count = numbers.get(previous_number, previous_number_count)
    return previous_number_count - last_occurence_count

# def extend_list_to(previous_numbers, target_number):
#     # if len(previous_numbers) == target_number:
#     #     return previous_numbers
#     # else:
#     #     next_number = get_next_number(previous_numbers)
#     #     previous_numbers.append(next_number)
#     #     return extend_list_to(previous_numbers, target_number)
#     for i in range(target_number):
#         if i >= len(previous_numbers):
#             next = get_next_number(previous_numbers)
#             previous_numbers.append(next)
#         if i % 1000 == 0:
#             print(i)
#     return previous_numbers


# def _get_number_at_count(previous_numbers, last_number, target_index):
    # if(current_index % 1000 == 0):
    #     print(current_index)
    # if target_index == current_index:
    #     return get_next_number(previous_numbers, last_number, current_index)
    # else:
    #     current_number = get_next_number(previous_numbers, last_number)
    #     _i_two_before, i_one_before = previous_numbers.get(current_number, current_index)
    #     previous_numbers[current_number] = (i_one_before, current_index)
    #     return _get_number_at_index(previous_numbers, numbers_left - 1)


def get_number_at_count(count, previous_numbers):
    numbers = {number: i+1 for i, number in enumerate(previous_numbers)}
    previous_number = previous_numbers[-1]
    previous_number_count = len(previous_numbers)
    current_number = -1
    for i in range(len(previous_numbers) + 1, count + 1):
        if(i % 1_000_000 == 0):
            percent = i * 100 // count
            print(f'#{i}, %{percent}')
        current_number = get_next_number(numbers, previous_number, previous_number_count)
        numbers[previous_number] = previous_number_count
        previous_number_count = i
        previous_number = current_number
    return current_number

if __name__ == "__main__":
    starting_numbers = read_starting_numbers('input.txt')
    number_2020 = get_number_at_count(2020, starting_numbers)
    print(f'2020th number: {number_2020}')

    number_30000000 = get_number_at_count(30_000_000, starting_numbers)
    print(f'30000000th number: {number_30000000}')
