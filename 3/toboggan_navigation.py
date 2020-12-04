from functools import reduce

def read_map(file_name):
    return open(file_name).read().splitlines()

def count_trees_on_slope(map, x_delta, y_delta):
    # x_current = 0
    y_current = 0
    trees_hit = 0
    for index, row in enumerate(map):
        if((index % x_delta) == 0):
            if(row[y_current] == "#"):
                trees_hit += 1
            # x_current += x_delta
            y_current = (y_current + y_delta) % len(row)
    return trees_hit

def multiply_trees_hit_each_slope(map, slopes):
    trees_hit_each_slope = [count_trees_on_slope(map, x, y) for x, y in slopes]
    def multiply_list(l):
        return reduce(lambda x, y: x * y, l)
    return multiply_list(trees_hit_each_slope)
