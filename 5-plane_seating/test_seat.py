import seat

def test_read_passes():
    expected_passes = [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL',
    ]
    assert seat.read_passes('example_passes.txt') == expected_passes

def test_get_ids():
    assert seat.get_seat_id('BFFFBBFRRR') == 567

def test_get_highest_id():
    boarding_passes = [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL',
    ]
    assert seat.get_highest_id(boarding_passes) == 820