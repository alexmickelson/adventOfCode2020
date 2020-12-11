import seating

def test_one_round():
    start = seating.read_seats('example.txt')
    expected_step1 = seating.read_seats('step1.txt')
    actual_step1 = seating.one_round(start)
    assert actual_step1 == expected_step1
    
def test_multiple_rounds():
    start = seating.read_seats('example.txt')
    expected_step1 = seating.read_seats('step1.txt')
    actual_step1 = seating.iterate_multiple_rounds(start, 1)
    assert actual_step1 == expected_step1
def test_multiple_rounds2():
    start = seating.read_seats('example.txt')
    expected_step2 = seating.read_seats('step2.txt')
    actual_step2 = seating.iterate_multiple_rounds(start, 2)
    assert actual_step2 == expected_step2

def test_run_until_stable():
    start = seating.read_seats('example.txt')
    final_seats = seating.iterate_until_stable(start)
    actual_filled_seats = seating.count_occupied_seats(final_seats)
    assert actual_filled_seats == 26

