from functools import reduce

def read_notes(file_name):
    raw_notes = open(file_name).read().split('\n\n')
    rules = {row.split(': ')[0]: number_range(row.split(': ')[1]) for row in raw_notes[0].split('\n') }
    my_ticket = parse_number_list(raw_notes[1].split('\n')[1])
    nearby_tickets = [parse_number_list(nl) for nl in raw_notes[2].split('\n')[1:]]
    
    return {
        "rules": rules,
        "my_ticket": my_ticket,
        "nearby_tickets": nearby_tickets
    }

def parse_number_list(number_list):
    return [ int(n) for n in number_list.split(',') ]

def number_range(raw_range):
    first_range = raw_range.split(' or ')[0]
    second_range = raw_range.split(' or ')[1]
    r = list(range(int(first_range.split('-')[0]), int(first_range.split('-')[1]) + 1))
    r.extend(list(range(int(second_range.split('-')[0]), int(second_range.split('-')[1]) + 1)))
    return r

# def get_invalid_ticket_location(notes):
#     valid_numbers = [item for sublist in notes['rules'].values() for item in sublist]
#     locations = []
#     for j in notes["rules"].keys():
#         for i in range(len(notes["nearby_tickets"])):
#             if notes["nearby_tickets"][i][j] not in valid_numbers:
#                 locations.append((i, j))
#     return locations

def get_invalid_numbers(notes):
    valid_numbers = [item for sublist in notes['rules'].values() for item in sublist]
    invalid_numbers = []
    for ticket in notes["nearby_tickets"]:
        for number in ticket:
            if number not in valid_numbers:
                invalid_numbers.append(number)
    return invalid_numbers

def get_valid_tickets(notes):
    valid_numbers = [item for sublist in notes['rules'].values() for item in sublist]
    valid_tickets = []
    for ticket in notes["nearby_tickets"]:
        if all(n in valid_numbers for n in ticket):
            valid_tickets.append(ticket)
    return valid_tickets

def get_ticket_label_order(notes):
    label_options = list(notes["rules"].keys())
    valid_tickets = get_valid_tickets(notes)
    possible_label_order = {}
    for col in range(len(valid_tickets[0])):
        column_numbers = [valid_tickets[row][col] for row in range(len(valid_tickets))]
        possible_label_order[col] = []
        for label in label_options:
            if all(cn in notes["rules"][label] for cn in column_numbers):
                possible_label_order[col].append(label)

    # sort through label order until only one left in each 
    label_order = {}
    while(len(label_order.keys()) != len(possible_label_order.keys())):
        for index, label_possibilities in possible_label_order.items():
            # remove any spoken for values
            possible_label_order[index] = [l for l in possible_label_order[index] if l not in label_order.values()]
            if len(label_possibilities) == 1:
                label_order[index] = label_possibilities[0]
    return label_order

def proccess_my_ticket(notes):
    label_order = get_ticket_label_order(notes)
    return { label: notes['my_ticket'][i] for i, label in label_order.items() }


if __name__ == "__main__":
    notes = read_notes('notes.txt')
    invalid_numbers = get_invalid_numbers(notes)
    ticket_scanning_error_rate = sum(invalid_numbers)
    print(f'ticket scanning error rate: {ticket_scanning_error_rate}')

    my_ticket = proccess_my_ticket(notes)
    departure_numbers = []
    for label in my_ticket.keys():
        if 'departure' in label:
            departure_numbers.append(my_ticket[label])
    product = reduce((lambda x, y: x*y), departure_numbers)
    print(f'departure product: {product}')