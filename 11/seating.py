

from os import read


def read_seats(file_name):
    return open(file_name).read().split('\n')

def count_neighbors(x, y, seats):
    x_min = x-1 if x != 0 else 0
    y_min = y-1 if y != 0 else 0
    x_max = x+1 if x != len(seats)-1 else len(seats)-1
    y_max = y+1 if y != len(seats[0])-1 else len(seats[0])-1
    count = 0
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if(seats[i][j] == "#"):
                count += 1
    if(seats[x][y] == "#"):
        count -= 1
    return count

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
                if(count_neighbors(i, j, seats) >= 4):
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
    