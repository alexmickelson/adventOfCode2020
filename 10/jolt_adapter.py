from multiprocessing import Pool
from math import factorial
from copy import deepcopy
from itertools import chain, combinations
from functools import lru_cache 
import sys


def read_jolts(file_name):
    return [int(j) for j in open(file_name).readlines()]

def count_differences(jolts):
    jolts.append(0)
    jolts.append(max(jolts) + 3)
    jolts.sort()
    differences = [j-i for i, j in zip(jolts[:-1], jolts[1:])]
    return {
        1: differences.count(1),
        2: differences.count(2),
        3: differences.count(3),
    }

def fibbonaci(n):
    return n if n <= 1 else fibbonaci(n-1) + fibbonaci(n-2)

def count_count_consecutive_ones(differences):
    different_arrangements = []
    count = 1 if differences[0] == 1 else 0
    for i in range(1, len(differences)):
        if(differences[i] != 1):
            if(count >= 2):
                different_arrangements.append(factorial(count) )
            count = 0
        elif(differences[i] == 1):
            count += 1
        # elif(differences[i-1] == 1 and differences[i] == 1):
        #     count = 0
    if(count >= 2):
        different_arrangements.append(factorial(count) )
    return sum(different_arrangements)
    # return reduce((lambda x, y: x * y), different_arrangements)

# def arrangement_is_valid(jolts):
#     return True if len(jolts) == 1 else (jolts[1] - jolts[0] <= 3 and arrangement_is_valid(jolts[1:]))
def arrangement_is_valid(jolts):
    return True if len(jolts) < 2 else jolts[1] - jolts[0] <= 3

# def count_arrangements(jolts):
#     jolts.sort()
#     level_count = 0
#     sub_count = 0
#     next_count = 0
#     if(len(jolts) > 2):
#         next_count = count_arrangements(jolts[1:])

#         trial_jolts_1 = deepcopy(jolts)
#         trial_jolts_1.remove(jolts[1])
#         if(arrangement_is_valid(trial_jolts_1)):
#             level_count += 1
#             sub_count += count_arrangements(trial_jolts_1)

#         if(len(jolts) > 3):
#             trial_jolts_2 = deepcopy(jolts)
#             trial_jolts_2.remove(jolts[2])
#             if(arrangement_is_valid(trial_jolts_2)):
#                 level_count += 1
#                 sub_count += count_arrangements(trial_jolts_2)

#             if(len(jolts) > 4):
#                 trial_jolts_3 = deepcopy(jolts)
#                 trial_jolts_3.remove(jolts[3])
#                 if(arrangement_is_valid(trial_jolts_3)):
#                     level_count += 1
#                     sub_count += count_arrangements(trial_jolts_3)

#                 trial_jolts_4 = deepcopy(jolts)
#                 trial_jolts_4.remove(jolts[1])
#                 trial_jolts_4.remove(jolts[2])
#                 if(arrangement_is_valid(trial_jolts_4)):
#                     level_count += 1
#                     sub_count += count_arrangements(trial_jolts_4)

#                 trial_jolts_5 = deepcopy(jolts)
#                 trial_jolts_5.remove(jolts[2])
#                 trial_jolts_5.remove(jolts[3])
#                 if(arrangement_is_valid(trial_jolts_5)):
#                     level_count += 1
#                     sub_count += count_arrangements(trial_jolts_5)

#                 trial_jolts_6 = deepcopy(jolts)
#                 trial_jolts_6.remove(jolts[1])
#                 trial_jolts_6.remove(jolts[3])
#                 if(arrangement_is_valid(trial_jolts_6)):
#                     level_count += 1
#                     sub_count += count_arrangements(trial_jolts_6)

#     return level_count + sub_count + next_count
def count_arrangements(jolts):
    jolt_min = min(jolts)
    jolt_max = max(jolts)
    jolts.sort()
    def validate_iteration(iteration_set):
        iteration = list(iteration_set)
        iteration.sort()
        if(iteration[0] == jolt_min and iteration[-1] == jolt_max):
            if(arrangement_is_valid(iteration)):
                return 1
        return 0
    all_iterations = all_combinations(jolts)
    pool = Pool(processes=4)

    count = 0
    # l = len(all_iterations)
    for i, iteration in enumerate(all_iterations):
        # print(i)
        count += validate_iteration(iteration)
        
    return count

def all_combinations(jolts):
    return chain.from_iterable(combinations(jolts, r) for r in range(1, len(jolts)+1))

def optional_jolts(jolts):
    adjacent_jolts = []
    essential_jolts = [jolts[0]]
    
    for i in range(1, len(jolts)- 1):
        if((jolts[i] - 1 == jolts[i-1]) and (jolts[i] + 1 == jolts[i+1])):
            adjacent_jolts.append(jolts[i])
        else:
            essential_jolts.append(jolts[i])
    essential_jolts.append(jolts[-1])
    return essential_jolts, adjacent_jolts
    

# def count_valid_jolt_combos(jolts, optional_jolts, position, l):
#     if(len(jolts) == 1):
#         return 0, l
#     count = 0
#     # l.append(jolts)
#     # print(jolts)
#     for i, jolt in enumerate(jolts[position:]):
#         if(jolt in optional_jolts):
#             trial = deepcopy(jolts)
#             trial.remove(jolt)
#             if(arrangement_is_valid(trial)):
#                 count += 1
#                 l.append(jolts)
#                 # l.append(trial)
#                 # print(trial)
#                 more, l = count_valid_jolt_combos(trial, optional_jolts, position + i, l)
#                 count += more

#     return count, l

# jolts = read_jolts('example-jolts.txt')
# jolts = read_jolts('example2.txt')
jolts = read_jolts('input.txt')
jolts.append(0)
jolts.append(max(jolts) + 3)

@lru_cache(maxsize=None)
def count_valid_jolt_combos(position, target):
    count = 0
    if(target >= len(jolts)):
        return 1

    print(jolts[target], jolts[target], jolts[target] - jolts[position] > 3)
    if(jolts[target] - jolts[position] > 3):
        return 0


    return count_valid_jolt_combos(position, target+1) + count_valid_jolt_combos(target, target + 1)
        

    # for i, jolt in enumerate(jolts[position:]):
    #     if(jolt in optional_jolts):
    #         if(jolts[position + i + 1] - jolts[position + i - 1] <= 3):
    #             count += 1
    #             more1 = count_valid_jolt_combos(position + i)
    #             more2 = count_valid_jolt_combos(position + i + 1)
    #             count += more1 + more2
    # return count


if __name__ == "__main__":
    jolts.sort()
    essential, optional = optional_jolts(jolts)

    print("total jolts")
    print(len(jolts))

    print('essential jolts: ')
    print(len(essential))

    print("optional jolts: ")
    print(len(optional))

    print("minimum jolts:")
    print(max(jolts) // 3)

    print('jolts')
    print(jolts)
    print('essential')
    print(essential)
    print('optional')
    print(optional)
    print()

    sys.setrecursionlimit(20000)

    optional_jolts = set(optional)
    count= count_valid_jolt_combos(0, 1)
    # l.sort()
    # print('\n'.join(', '.join(map(str,sl)) for sl in l))
    print(count//2)
    # print(factorial(len(optional)))
    # count = 0
    # feedback = 0
    # for c in all_combinations(optional):
    #     feedback +=1
    #     if(feedback % 1000000 == 0):
    #         print(feedback)
    #     trial = deepcopy(essential)
    #     trial.extend(list(c))
    #     trial.sort()
    #     if(arrangement_is_valid(trial)):
    #         count += 1
    #     # print(c)
    # print('count:' + str(count))