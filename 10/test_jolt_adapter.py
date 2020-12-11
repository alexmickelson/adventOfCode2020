import jolt_adapter

# def test_count_differences():
#     jolts = jolt_adapter.read_jolts('example-jolts.txt')
#     expected_jolts = {
#         1: 7,
#         2: 0,
#         3: 5,
#     }
#     actual_jolts = jolt_adapter.count_differences(jolts)
#     assert expected_jolts == actual_jolts

# def test_count_arangements():
#     jolts = jolt_adapter.read_jolts('example-jolts.txt')
#     expected_count = 8
#     jolts.append(0)
#     jolts.append(max(jolts) + 3)
#     actual_count = jolt_adapter.count_arrangements(jolts)
#     assert actual_count == expected_count

def test_count_arangements2():
    jolts = jolt_adapter.read_jolts('example2.txt')
    expected_count = 19208
    actual_count = jolt_adapter.count_arrangements(jolts)
    assert actual_count == expected_count