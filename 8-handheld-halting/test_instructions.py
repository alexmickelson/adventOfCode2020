import instructions

def test_read_instructions_from_file():
    expected_instructions = [
        { 'operation': 'nop', 'argument': +0},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': +4},
        { 'operation': 'acc', 'argument': +3},
        { 'operation': 'jmp', 'argument': -3},
        { 'operation': 'acc', 'argument': -99},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': -4},
        { 'operation': 'acc', 'argument': +6},
    ]
    actual_instructions = instructions.read_instructions_from_file('example-instructions.txt')
    assert actual_instructions == expected_instructions

def test_find_accumulator_value_at_repeat():
    instructions_list = [
        { 'operation': 'nop', 'argument': +0},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': +4},
        { 'operation': 'acc', 'argument': +3},
        { 'operation': 'jmp', 'argument': -3},
        { 'operation': 'acc', 'argument': -99},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': -4},
        { 'operation': 'acc', 'argument': +6},
    ]
    expected_accumulator = 5
    _status, acutal_accumulator = instructions.run_instructions(instructions_list)
    assert acutal_accumulator == expected_accumulator

def test_correct_broken_instruction_list():
    instructions_list = [
        { 'operation': 'nop', 'argument': +0},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': +4},
        { 'operation': 'acc', 'argument': +3},
        { 'operation': 'jmp', 'argument': -3},
        { 'operation': 'acc', 'argument': -99},
        { 'operation': 'acc', 'argument': +1},
        { 'operation': 'jmp', 'argument': -4},
        { 'operation': 'acc', 'argument': +6},
    ]
    expected_accumulator = 8
    actual_accumulator = instructions.correct_and_run_instruction_list(instructions_list)
    assert actual_accumulator == expected_accumulator