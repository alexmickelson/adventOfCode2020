
from os import read


def read_directions(file_name):
    return [(s[0], int(s[1:])) for s in  open(file_name).read().split('\n')]


# positive: east, north
# angle 0 is east

def follow_directions(directions):
    east = 0
    north = 0
    angle = 0
    for action, value in directions:
        if(action == 'F'):
            if(angle == 0):
                east += value
            elif(angle == 90):
                north -= value
            elif(angle == 180):
                east -= value
            elif(angle == 270):
                north += value
            else:
                raise Exception('bad angle')
        elif(action == 'R'):
            angle = (angle + value) % 360
        elif(action == 'L'):
            angle = (angle - value) % 360
        elif(action == 'W'):
            east -= value
        elif(action == 'E'):
            east += value
        elif(action == 'S'):
            north -= value
        elif(action == 'N'):
            north += value
    return east, north

def follow_waypoint_directions(directions):
    waypoint_east = 10
    waypoint_north = 1
    ship_east = 0
    ship_north = 0
    for action, value in directions:
        if(action == 'F'):
            ship_east += value * waypoint_east
            ship_north += value * waypoint_north
        elif(action == 'R'):
            if(value == 90):
                tmp = waypoint_east
                waypoint_east = waypoint_north
                waypoint_north = -1 * tmp
            elif(value == 180):
                waypoint_east = -1 * waypoint_east
                waypoint_north = -1 * waypoint_north
            elif(value == 270):
                tmp = waypoint_east
                waypoint_east = -1 * waypoint_north
                waypoint_north = tmp
        elif(action == 'L'):
            if(value == 90):
                tmp = waypoint_east
                waypoint_east = -1 * waypoint_north
                waypoint_north = tmp
            elif(value == 180):
                waypoint_east = -1 * waypoint_east
                waypoint_north = -1 * waypoint_north
            elif(value == 270):
                tmp = waypoint_east
                waypoint_east = waypoint_north
                waypoint_north = -1 * tmp
        elif(action == 'W'):
            waypoint_east -= value
        elif(action == 'E'):
            waypoint_east += value
        elif(action == 'S'):
            waypoint_north -= value
        elif(action == 'N'):
            waypoint_north += value
        else:
            raise Exception('bad instruction')
    return ship_east, ship_north

def manhattan_distance(position):
    (east, north) = position
    return abs(east) + abs(north)

if __name__ == "__main__":
    directions = read_directions('input.txt')
    position = follow_directions(directions)
    manhattan = manhattan_distance(position)
    print(f'manhattan distance: {manhattan}')
    
    corrected_position = follow_waypoint_directions(directions)
    corrected_manhattan = manhattan_distance(corrected_position)
    print(f'corrected manhattan distance: {corrected_manhattan}')

