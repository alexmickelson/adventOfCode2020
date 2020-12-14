import shuttles

def test_read_lines():
    actual_arrival, actual_bus_ids = shuttles.read_notes('example.txt')
    expected_arrival = 939
    expected_bus_ids = [7,13,59,31,19]
    assert actual_arrival == expected_arrival
    assert actual_bus_ids == expected_bus_ids

def test_find_earliest_depart():
    expected_depart = 944
    arrival = 939
    bus_ids = [7,13,59,31,19]
    expected_bus_id = 59
    actual_depart, actual_bus_id = shuttles.find_earliest_depart_time(arrival, bus_ids)
    assert actual_depart == expected_depart
    assert actual_bus_id == expected_bus_id

def test_timestamp_bus_ids():
    bus_ids = shuttles.read_all_bus_ids('example.txt')
    expected_time = 1068781
    actual_time = shuttles.get_time_by_bus_ids(bus_ids)
    assert actual_time == expected_time