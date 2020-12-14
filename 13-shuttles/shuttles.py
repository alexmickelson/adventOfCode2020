from multiprocessing import Pool
import itertools
from time import sleep
from more_itertools import grouper
import sympy
from sympy.ntheory.modular import crt 

def read_notes(file_name):
    raw_notes = open(file_name).read().split('\n')
    arrival_time = int(raw_notes[0])
    bus_ids = []
    for id in raw_notes[1].split(','):
        if(id != 'x'):
            bus_ids.append(int(id))
    return arrival_time, bus_ids

def read_all_bus_ids(file_name):
    raw_notes = open(file_name).read().split('\n')
    bus_ids = []
    for id in raw_notes[1].split(','):
        bus_ids.append(id)
    return bus_ids
    
def find_earliest_depart_time(arrival, bus_ids):
    depart_times = [find_next_bus_depart(arrival, bid) for bid in bus_ids]
    smalled_bus_time = min(depart_times)
    smallest_depart_bus_id = bus_ids[depart_times.index(smalled_bus_time)]
    return smalled_bus_time, smallest_depart_bus_id


def find_next_bus_depart(arrival, bus_id):
    difference = arrival % bus_id
    return arrival - difference + bus_id

bus_ids = read_all_bus_ids('input.txt')

# def get_time_by_bus_ids(bus_ids):
#     start_time = max([int(x) if x != 'x' else 0 for x in bus_ids])
#     start_time_offset = bus_ids.index(str(start_time))
#     # ids_to_check = []
#     # for i, bus_id in enumerate(bus_ids):
#     #     if(bus_id != 'x' and str(bus_id) != start_time):
#     #         ids_to_check.append((i, int(bus_id)))
            
#     # 100_000_000_000_000
#     #  90_699_999_999_983
#     #  90_790_699_999_983
#     # 100_000_000
#     i =   100_000_000_000
#     trial_time = (start_time * i) - start_time_offset
#     # i = 1
#     print(f'max: {start_time}')

#     pool = Pool(10)
#     pool.imap(check_time, grouper(100_000, enumerate(itertools.count(trial_time, start_time))))
#     # Parallel()(check_time(t, start_time, start_time_offset) for t in itertools.count(trial_time, start_time))

#     while(True):
#         sleep(10)
#     # while(not time_is_valid(trial_time, ids_to_check)):
#     #     i += 1
#     #     trial_time += start_time
#     #     # print(i*59)
#     #     if(i % 10_000_000 == 0):
#     #         print(f'{i}: {trial_time}')

#     # return trial_time

def get_time_by_bus_ids(bus_ids):
    # start_time = max([int(x) if x != 'x' else 0 for x in bus_ids])
    # start_time_offset = bus_ids.index(str(start_time))
    b_ids = []
    indexes = []
    for i, bus_id in enumerate(bus_ids):
        if(bus_id != 'x'):
            b_ids.append(int(bus_id))
            indexes.append(int(bus_id) - i)
    result = crt(b_ids, indexes)
    print(result)
    return result[0]

def check_time(l):
    for i, time in l:
        if(i % 100_000_000 == 0):
            print(f'{i}: {time}')
        if(time_is_valid(time, ids_to_check)):
            print(f'answer is {time}')

def time_is_valid(time, bus_ids):
    # for i, bus_id in bus_ids:
    #     if(((time + i) % bus_id) != 0):
    #         return False
    # return True

    return all(False if(((time + i) % bus_id) != 0) else True for i, bus_id in bus_ids)

if __name__ == "__main__":
    # arrival, bus_ids = read_notes('example.txt')
    arrival, bus_ids = read_notes('input.txt')
    depart, bus_id = find_earliest_depart_time(arrival, bus_ids)

    part_1 = bus_id *  (depart - arrival)
    print(f'part 1: {part_1}')
    print()
    
    bus_ids = read_all_bus_ids('input.txt')
    start_time = max([int(x) if x != 'x' else 0 for x in bus_ids])
    ids_to_check = []
    for i, bus_id in enumerate(bus_ids):
        if(bus_id != 'x' and str(bus_id) != start_time):
            ids_to_check.append((i, int(bus_id)))

    # print(f'expect 1068781')
    actual_time = get_time_by_bus_ids(bus_ids)
    