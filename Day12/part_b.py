import math


def rotate(position_x, position_y, angle):  # Rotate point (x,y) counter-clockwise around (0,0).
    angle_radians = math.radians(angle)
    new_position_x = int(round(math.cos(angle_radians) * position_x - math.sin(angle_radians) * position_y))
    new_position_y = int(round(math.sin(angle_radians) * position_x + math.cos(angle_radians) * position_y))
    return new_position_x, new_position_y


def run():
    print("\nDay 12 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day12/input.txt")]
    # The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with
    # integer input values.
    instructions = list(map(lambda x: (x[:1], int(x[1:])), text_input))

    # The waypoint starts 10 units east and 1 unit north relative to the ship.
    waypoint_position_east = 10
    waypoint_position_north = 1

    ship_position_east = 0
    ship_position_north = 0

    for action, value in instructions:
        if action == "N":
            # Action N means to move the waypoint north by the given value.
            waypoint_position_north += value
        elif action == "S":
            # Action S means to move the waypoint south by the given value.
            waypoint_position_north -= value
        elif action == "E":
            # Action E means to move the waypoint east by the given value.
            waypoint_position_east += value
        elif action == "W":
            # Action W means to move the waypoint west by the given value.
            waypoint_position_east -= value
        elif action == "L":
            # Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
            waypoint_position_east, waypoint_position_north = rotate(waypoint_position_east, waypoint_position_north, value)
        elif action == "R":
            # Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
            waypoint_position_east, waypoint_position_north = rotate(waypoint_position_east, waypoint_position_north, -value)
        elif action == "F":
            # Action F means to move forward to the waypoint a number of times equal to the given value.
            ship_position_north += value * waypoint_position_north
            ship_position_east += value * waypoint_position_east

    # What is the Manhattan distance between that location and the ship's starting position?
    print(abs(ship_position_east) + abs(ship_position_north))




