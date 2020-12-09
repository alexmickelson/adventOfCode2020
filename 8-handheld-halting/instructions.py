from os import read, stat
from copy import deepcopy


def read_instructions_from_file(file_name):
    raw_instructions = open(file_name).readlines()
    instructions = [
        {
            'operation': i.split(" ")[0], 
            'argument': int(i.split(" ")[1].replace("\n", ""))
        }
        for i
        in raw_instructions
    ]
    return instructions

def run_instructions(instructions):
    history = []
    next_position = 0
    accumulator = 0
    while next_position not in history:
        if(next_position == len(instructions)):
            return ('program_finished', accumulator)
        history.append(next_position)
        if(instructions[next_position]['operation'] == 'nop'):
            next_position += 1
        elif(instructions[next_position]['operation'] == 'acc'):
            accumulator += instructions[next_position]['argument']
            next_position += 1
        elif(instructions[next_position]['operation'] == 'jmp'):
            next_position = next_position + instructions[next_position]['argument']
    return ('repeat', accumulator)

def correct_and_run_instruction_list(instructions):
    #first see if swaping any jmp to a nop fixes
    #then try swapping any nop to jmp
    for index, instruction in enumerate(instructions):
        if(instruction['operation'] == 'nop'):
            trial_instructions = deepcopy(instructions)
            trial_instructions[index]['operation'] = 'jmp'
            status, accumulator = run_instructions(trial_instructions)
            if(status == 'program_finished'):
                return accumulator
        elif(instruction['operation'] == 'jmp'):
            trial_instructions = deepcopy(instructions)
            trial_instructions[index]['operation'] = 'nop'
            status, accumulator = run_instructions(trial_instructions)
            if(status == 'program_finished'):
                return accumulator

if __name__ == "__main__":
    instruction_list = read_instructions_from_file('instructions.txt')
    _status, accumulator = run_instructions(instruction_list)
    print("accumulator before repeat: " + str(accumulator))

    correct_accumulator = correct_and_run_instruction_list(instruction_list)
    print("corrected accumulator is: " + str(correct_accumulator))
