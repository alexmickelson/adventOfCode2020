import directions

def test_example():
    instructions = directions.read_directions('example.txt')
    expected_position = (17, -8)
    assert directions.follow_directions(instructions) == expected_position

def test_manhattan_distance():
    instructions = directions.read_directions('example.txt')
    actual_position =  directions.follow_directions(instructions)
    assert directions.manhattan_distance(actual_position) == 25

def test_part_1(): 
    instructions = directions.read_directions('input.txt')
    actual_position =  directions.follow_directions(instructions)
    assert directions.manhattan_distance(actual_position) == 2057
def test_manhattan_distance():
    instructions = directions.read_directions('example.txt')
    expected_position = (17, -8)
    actual_position =  directions.follow_directions(instructions)
    assert directions.manhattan_distance(actual_position) == 25

def test_waypoint_example():
    instructions = directions.read_directions('example.txt')
    instructions.append(('F', 11))
    instructions.append(('L', 180))
    instructions.append(('F', 11))
    expected_position = (214, -72)
    assert directions.follow_waypoint_directions(instructions) == expected_position