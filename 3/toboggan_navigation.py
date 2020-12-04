

def read_map(file_name):
    return open(file_name).read().splitlines()

def count_trees_on_slope(map, y_delta):
    y_current = 0
    trees_hit = 0
    for row in map:
        if(row[y_current] == "#"):
            trees_hit += 1
        y_current = (y_current + y_delta) % len(row)
    return trees_hit