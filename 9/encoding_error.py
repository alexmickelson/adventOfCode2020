import itertools
from os import read

def read_numbers(file_name):
    return [int(l) for l in open(file_name).readlines()]

def find_pattern_breaking_number(numbers, preamble_size):
    for index, number in enumerate(numbers[preamble_size:]):
        preceding_numbers = numbers[index:index + preamble_size]

        couples_of_possible_numbers = itertools.combinations(preceding_numbers, 2)
        possible_outcoms = [n1 + n2 for n1, n2 in couples_of_possible_numbers]
        if(number not in possible_outcoms):
            return number
    return -1


def find_congurent_numbers_summing(sum, numbers):
    for i in range(len(numbers)):
        local_sum = numbers[i]
        j = i + 1
        while(local_sum <+ sum):
            local_sum += numbers[j]
            j += 1
            if(local_sum == sum):
                return numbers[i:j]

def sum_smallest_largest(numbers):
    return min(numbers) + max(numbers)
            

if __name__ == "__main__":
    numbers = read_numbers('numbers.txt')
    culprit = find_pattern_breaking_number(numbers, 25)
    print("guilty number is: " + str(culprit))

    congruent_numbers = find_congurent_numbers_summing(culprit, numbers)
    sum = sum_smallest_largest(congruent_numbers)
    print("sum of smallest and largest congruent numbers: " + str(sum))
