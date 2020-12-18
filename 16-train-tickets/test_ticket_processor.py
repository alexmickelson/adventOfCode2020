import ticket_processor


def test_read_notes():
    expected_notes = {
        "rules": {
            "class": [1, 2, 3, 5, 6, 7],
            "row": [6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
            "seat": [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50]
        },
        "my_ticket": [7, 1, 14],
        "nearby_tickets": [
            [7, 3, 47],
            [40, 4, 50],
            [55, 2, 20],
            [38, 6, 12],
        ]
    }
    actual_notes = ticket_processor.read_notes('example.txt')
    assert expected_notes == actual_notes


def test_number_range():
    raw_range = "1-3 or 5-7"
    expected_range = [1, 2, 3, 5, 6, 7]
    acutal_range = ticket_processor.number_range(raw_range)
    assert acutal_range == expected_range


def test_get_invalid_numbers():
    notes = ticket_processor.read_notes('example.txt')
    expected_invalid_nubmers = [4, 55, 12]
    actual_invalid_nubmers = ticket_processor.get_invalid_numbers(notes)
    assert actual_invalid_nubmers == expected_invalid_nubmers


def test_get_valid_tickets():
    notes = ticket_processor.read_notes('example.txt')
    expected_valid_tickets = [[7, 3, 47]]
    actual_valid_tickets = ticket_processor.get_valid_tickets(notes)
    assert actual_valid_tickets == expected_valid_tickets


def test_get_ticket_label_order():
    notes = ticket_processor.read_notes('example.txt')
    expected_ticket_label_order = {
        0: 'row',
        1: 'class',
        2: 'seat'
    }
    actual_ticket_label_order = ticket_processor.get_ticket_label_order(notes)
    assert actual_ticket_label_order == expected_ticket_label_order

def test_proccess_my_ticket():
    notes = ticket_processor.read_notes('example.txt')
    expected_ticket = {
        'row': 7,
        'class': 1,
        'seat': 14,
    }
    actual_ticket = ticket_processor.proccess_my_ticket(notes)
    assert actual_ticket == expected_ticket


