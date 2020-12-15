import initialization_program as program

def test_read_instructions():
    expected_instructions = [
        {
            'mask': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'writes':  [
                {
                    'address': 8,
                    'decimal': 11
                },
                {
                    'address': 7,
                    'decimal': 101
                },
                {
                    'address': 8,
                    'decimal': 0
                }
            ]
        }
    ]
    acutal_instructions = program.read_instructions('example.txt')
    assert acutal_instructions == expected_instructions

def test_decimal_to_binary():
    expected_binary = '000000000000000000000000000001100101'
    assert program.decimal_to_binary(101) == expected_binary

def test_binary_to_decimal():
    binary = '000000000000000000000000000001100101'
    assert program.binary_to_decimal(binary) == 101

def test_apply_mask():
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
    decimal = 11
    expectes_result = 73
    actual_result = program.apply_mask(decimal, mask)
    assert actual_result == expectes_result

def test_run_instruction():
    starting_memory = {}
    instructions = program.read_instructions('example.txt')
    expected_memory = {
        7: 101,
        8: 64
    }
    actual_memory = program.run_instruction(instructions[0], starting_memory)
    assert actual_memory == expected_memory

def test_run_instructions():
    starting_memory = {}
    instructions = program.read_instructions('example.txt')
    expected_memory = {
        7: 101,
        8: 64
    }
    actual_memory = program.run_instructions(instructions, starting_memory)
    assert actual_memory == expected_memory

def test_sum_memory():
    instructions = program.read_instructions('example.txt')
    memory = program.run_instructions(instructions, {})
    expected_memory_sum = program.sum_memory(memory)
    assert expected_memory_sum == 165

def test_decode_memory_addresses():
    mask = '000000000000000000000000000000X1001X'
    decimal = 42
    expected_memory_addresses = [26, 27, 58, 59]
    actual_memory_addresses = program.decode_memory_addresses(decimal, mask)
    assert actual_memory_addresses == expected_memory_addresses


def test_sum_program_2():
    instructions = program.read_instructions('example2.txt')
    memory = program.run_instructions2(instructions, {})
    expected_memory_sum = program.sum_memory(memory)
    assert expected_memory_sum == 208
