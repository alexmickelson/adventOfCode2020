from multiprocessing import Pool
from math import factorial
from copy import deepcopy
from itertools import chain, combinations
from more_itertools import grouper
import concurrent
import itertools

def read_jolts(file_name):
    return [int(j) for j in open(file_name).readlines()]


def arrangement_is_valid(jolts):
    return True if len(jolts) < 2 else jolts[1] - jolts[0] <= 3


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


def count_valid_jolt_combos(jolts, optional_jolts, position, c):
    if(len(jolts) == 1):
        return 0
    c += 1
    if(c % 1000000 == 0):
        print(c)
    count = 0
    for i, jolt in enumerate(jolts[position:]):
        if(jolt in optional_jolts):
            if(jolts[position + i + 1] - jolts[position + i - 1] <= 3):
                trial = list(jolts)
                trial.remove(jolt)
                count += 1
                more, c = count_valid_jolt_combos(trial, optional_jolts, position + i, c)
                count += more

    return count, c


if __name__ == "__main__":
    # jolts = read_jolts('example-jolts.txt')
    # jolts = read_jolts('example2.txt')
    jolts = read_jolts('input.txt')
    jolts.append(0)
    jolts.append(max(jolts) + 3)
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


    count, c = count_valid_jolt_combos(jolts, set(optional), 0, 0)
    print(count + 1)