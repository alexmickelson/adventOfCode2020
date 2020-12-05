

def read_passes(file_name):
    return open(file_name).read().splitlines()

def get_seat_id(boarding_pass):
    row_letters = boarding_pass[:7]
    rows = list(range(128))
    for letter in row_letters:
        if(letter == "F"):
            rows = rows[:len(rows) // 2]
        else:
            rows = rows[len(rows) // 2:]
    row = rows[0]
    
    column_letters = boarding_pass[7:]
    columns = list(range(8))
    for letter in column_letters:
        if(letter == "R"):
            columns = columns[len(columns) // 2:]
        else:
            columns = columns[:len(columns) // 2]
    column = columns[0]
    return (row * 8) + column

def get_all_ids(boarding_passes):
    return [get_seat_id(bp) for bp in boarding_passes]

def get_highest_id(boarding_passes):
    return max(get_all_ids(boarding_passes))

def get_missing_ids(boarding_passes):
    all_ids = list(range(1024))
    current_ids = get_all_ids(boarding_passes)
    missing_ids = list(set(all_ids) - set(current_ids))
    return missing_ids


#part 1
passes = read_passes('passes.txt')
print("largest id: " + str(get_highest_id(passes)))

#part 2

print()
print("missing ids: " + str(get_missing_ids(passes)))
