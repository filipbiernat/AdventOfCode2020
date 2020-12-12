def run():
    print("\nDay 12 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day12/input.txt")]
    # The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with
    # integer input values.
    instructions = list(map(lambda x: (x[:1], int(x[1:])), text_input))

    directions = ["N", "E", "S", "W"]

    # The ship starts by facing east.
    ship_direction = "E"
    ship_position_east = 0
    ship_position_north = 0

    for action, value in instructions:
        if action == "F":
            # Action F means to move forward by the given value in the direction the ship is currently facing.
            action = ship_direction

        if action == "N":
            # Action N means to move north by the given value.
            ship_position_north += value
        elif action == "S":
            # Action S means to move south by the given value.
            ship_position_north -= value
        elif action == "E":
            # Action E means to move east by the given value.
            ship_position_east += value
        elif action == "W":
            # Action W means to move west by the given value.
            ship_position_east -= value
        elif action == "L":
            # Action L means to turn left the given number of degrees.
            current_index_in_directions_list = directions.index(ship_direction)
            next_index_in_directions_list = (current_index_in_directions_list - int(value/90)) % len(directions)
            ship_direction = directions[next_index_in_directions_list]
        elif action == "R":
            # Action R means to turn right the given number of degrees.
            current_index_in_directions_list = directions.index(ship_direction)
            next_index_in_directions_list = (current_index_in_directions_list + int(value/90)) % len(directions)
            ship_direction = directions[next_index_in_directions_list]

    # What is the Manhattan distance between that location and the ship's starting position?
    print(abs(ship_position_east) + abs(ship_position_north))




