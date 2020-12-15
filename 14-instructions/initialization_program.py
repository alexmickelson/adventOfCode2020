

def read_instructions(file_name):
    raw_mask_sets = open(file_name).read().split('mask = ')
    mask_sets = []
    for rms in raw_mask_sets[1:]:
        raw_mask_sets = rms.split('\n')
        mask_set = {
            'mask': raw_mask_sets[0],
            'writes': []
        }
        for instruction in raw_mask_sets[1:-1]:
            memory_address = instruction.split('[')[1].split(']')[0]
            decimal_number = instruction.split('= ')[1].replace('\n', '')
            mask_set['writes'].append({
                'address': int(memory_address),
                'decimal': int(decimal_number)
            })
        mask_sets.append(mask_set)
    return mask_sets

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary.rjust(36, '0')

def binary_to_decimal(binary):
    length = len(binary)
    decimal = 0
    for i in range(len(binary)):
        if(binary[length - i - 1] == '1'):
            decimal += pow(2, i)
    return decimal


def apply_mask(decimal, mask):
    binary = decimal_to_binary(decimal)
    result = ''
    for mask_bit, binary_bit in zip(mask, binary):
        if mask_bit == 'X':
            result += binary_bit
        else:
            result += mask_bit
    return binary_to_decimal(result)

def run_instruction(instruction, memory):
    for write in instruction['writes']:
        memory_value = apply_mask(write['decimal'], instruction['mask'])
        memory[write['address']] = memory_value
    return memory

def run_instructions(instructions, memory):
    for instruction in instructions:
        memory = run_instruction(instruction, memory)
    return memory

def sum_memory(memory):
    return sum(memory.values())

# part 2 code
def decode_memory_addresses(memory_address, mask):
    binary = decimal_to_binary(memory_address)

    results = ['']
    for mask_bit, binary_bit in zip(mask, binary):
        if mask_bit == 'X':
            # duplicate each element in results
            results = [r for r in results for _ in (0, 1)] 
            results = [r + str(i % 2) for i, r in enumerate(results)]
        elif mask_bit == '1':
            results = [r + '1' for r in results]
        else:
            results = [r + binary_bit for r in results]
    decimal_results = [binary_to_decimal(r) for r in results]
    return decimal_results

def run_instruction2(instruction, memory):
    for write in instruction['writes']:
        memory_addresses = decode_memory_addresses(write['address'], instruction['mask'])
        for memory_address in memory_addresses:
            memory[memory_address] = write['decimal']
    return memory

def run_instructions2(instructions, memory):
    for instruction in instructions:
        memory = run_instruction2(instruction, memory)
    return memory

if __name__ == "__main__":
    instructions = read_instructions('input.txt')
    starting_memory = {}
    ending_memory = run_instructions(instructions, starting_memory)
    memory_sum = sum_memory(ending_memory)
    print(f'memory sum: {memory_sum}')

    memory_part_two = run_instructions2(instructions, {})
    memory_sum = sum_memory(memory_part_two)
    print(f'memory sum part 2: {memory_sum}')
