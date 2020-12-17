from collections import defaultdict


def active_neighbors(dimension, x, y, z):
    result = 0
    for x_ in [x-1, x, x+1]:
        for y_ in [y-1, y, y+1]:
            for z_ in [z-1, z, z+1]:
                result += dimension[(x_, y_, z_)] if (x_, y_, z_) != (x, y, z) else 0
    return result


def run():
    print("\nDay 17 - Part A")

    text_input = [list(line.rstrip('\n')) for line in open("Day17/input.txt")]

    # The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z),
    # there exists a single cube which is either active or inactive.
    # In the initial state of the pocket dimension, almost all cubes start inactive.
    pocket_dimension = defaultdict(lambda: False)  # By default - false - inactive.
    # The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start
    # in the specified active (#) or inactive (.) state.
    for start_row in range(len(text_input)):
        for start_col in range(len(text_input[0])):
            pocket_dimension[(start_col, start_row, 0)] = text_input[start_col][start_row] == '#'

    # Starting with your given initial configuration, simulate six cycles.
    for cycle_id in range(6):
        active_mass_delta = cycle_id + 1  # Take into account that the active mass grows.
        # During a cycle, all cubes simultaneously change their state
        pocket_dimension_after_cycle = defaultdict(lambda: False)

        for x in range(-active_mass_delta, start_col + 1 + active_mass_delta):
            for y in range(-active_mass_delta, start_row + 1 + active_mass_delta):
                for z in range(-active_mass_delta, 1 + active_mass_delta):
                    if pocket_dimension[(x, y, z)]:
                        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
                        # Otherwise, the cube becomes inactive.
                        pocket_dimension_after_cycle[(x, y, z)] = active_neighbors(pocket_dimension, x, y, z) in [2, 3]
                    else:
                        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
                        # Otherwise, the cube remains inactive.
                        pocket_dimension_after_cycle[(x, y, z)] = active_neighbors(pocket_dimension, x, y, z) == 3

        pocket_dimension = pocket_dimension_after_cycle

    # How many cubes are left in the active state after the sixth cycle?
    print(sum(pocket_dimension.values()))
