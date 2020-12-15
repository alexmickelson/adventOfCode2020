# import sys


# sys.setrecursionlimit(30_000_002)

def read_starting_numbers(file_name):
    return [int(i) for i in open(file_name).read().replace('\n', '').split(',')]

def get_next_number(numbers, previous_number, previous_number_count):
    last_occurence_count = numbers.get(previous_number, previous_number_count)
    return previous_number_count - last_occurence_count


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
