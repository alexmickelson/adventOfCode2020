

from os import read


def read_seats(file_name):
    return open(file_name).read().split('\n')

def y_decrease_neighbor_is_occupied(x, y, seats):
    y_target = y - 1
    while(y_target >= 0):
        if(seats[x][y_target] == "L"):
            return False
        if(seats[x][y_target] == "#"):
            return True
        y_target -= 1
    return False

def x_and_y_decrease_neighbor_is_occupied(x, y, seats):
    y_target = y - 1
    x_target = x - 1
    while(y_target >= 0 and x_target >= 0):
        if(seats[x_target][y_target] == "L"):
            return False
        if(seats[x_target][y_target] == "#"):
            return True
        y_target -= 1
        x_target -= 1
    return False

def x_increase_and_y_decrease_neighbor_is_occupied(x, y, seats):
    y_target = y - 1
    x_target = x + 1
    while(y_target >= 0 and x_target < len(seats)):
        if(seats[x_target][y_target] == "L"):
            return False
        if(seats[x_target][y_target] == "#"):
            return True
        y_target -= 1
        x_target += 1
    return False





def y_increase_neighbor_is_occupied(x, y, seats):
    y_target = y + 1
    while(y_target < len(seats[x])):
        if(seats[x][y_target] == "L"):
            return False
        if(seats[x][y_target] == "#"):
            return True
        y_target += 1
    return False

def x_and_y_increase_neighbor_is_occupied(x, y, seats):
    y_target = y + 1
    x_target = x - 1
    while(y_target < len(seats[x]) and x_target >= 0):
        if(seats[x_target][y_target] == "L"):
            return False
        if(seats[x_target][y_target] == "#"):
            return True
        y_target += 1
        x_target -= 1
    return False

def x_increase_and_y_increase_neighbor_is_occupied(x, y, seats):
    y_target = y + 1
    x_target = x + 1
    while(y_target < len(seats[x]) and x_target < len(seats)):
        if(seats[x_target][y_target] == "L"):
            return False
        if(seats[x_target][y_target] == "#"):
            return True
        y_target += 1
        x_target += 1
    return False



def x_increase_neighbor_is_occupied(x, y, seats):
    x_target = x + 1
    while(x_target < len(seats)):
        if(seats[x_target][y] == "L"):
            return False
        if(seats[x_target][y] == "#"):
            return True
        x_target += 1
    return False

def x_decrease_neighbor_is_occupied(x, y, seats):
    x_target = x - 1
    while(x_target >= 0):
        if(seats[x_target][y] == "L"):
            return False
        if(seats[x_target][y] == "#"):
            return True
        x_target -= 1
    return False

def count_neighbors(x, y, seats):
    return sum([
        y_decrease_neighbor_is_occupied(x, y, seats),
        y_increase_neighbor_is_occupied(x, y, seats),
        x_and_y_decrease_neighbor_is_occupied(x, y, seats),
        x_and_y_increase_neighbor_is_occupied(x, y, seats),
        x_increase_and_y_decrease_neighbor_is_occupied(x, y, seats),
        x_increase_and_y_increase_neighbor_is_occupied(x, y, seats),
        x_decrease_neighbor_is_occupied(x, y, seats),
        x_increase_neighbor_is_occupied(x, y, seats),
    ])

def one_round(seats):
    next_round = [ '' for row in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if(seats[i][j] == "L"):
                if(count_neighbors(i, j, seats) == 0):
                    next_round[i] += "#"
                else:
                    next_round[i] += "L"
            elif(seats[i][j] == "#"):
                if(count_neighbors(i, j, seats) >= 5):
                    next_round[i] += "L"
                else:
                    next_round[i] += "#"
            else:
                next_round[i] += "."
    return next_round

def iterate_multiple_rounds(seats, rounds):
    for i in range(rounds):
        seats = one_round(seats)
    return seats

def iterate_until_stable(seats):
    next_seats = one_round(seats)
    if(next_seats == seats):
        return seats
    else:
        return iterate_until_stable(next_seats)

def count_occupied_seats(seats):
    count = 0
    for row in seats:
        for seat in row:
            if(seat == "#"):
                count += 1
    return count

if __name__ == "__main__":
    starting_seats = read_seats("input.txt")
    final_seats = iterate_until_stable(starting_seats)
    filled_seats = count_occupied_seats(final_seats)
    print("final ocupied seats: ", filled_seats)
    # part 1: 2251
    