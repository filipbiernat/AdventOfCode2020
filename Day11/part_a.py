import numpy as np


def is_in_grid_range(array, x, y):
    return 0 <= x < array.shape[0] and 0 <= y < array.shape[1]


def is_seat_occupied(array, x, y, dx, dy):  # Check an immediate neighbour.
    return array[x + dx][y + dy] == '#' if is_in_grid_range(array, x + dx, y + dy) else False


def occupied_seats_arround(array, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(is_seat_occupied(array, x, y, dx, dy) for dx, dy in directions)


def generate_next_layout(layout):
    # All decisions are based on the number of occupied seats adjacent to a given seat.
    next_layout = layout.copy()
    for x in range(layout.shape[0]):
        for y in range(layout.shape[1]):
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if layout[x, y] == 'L' and occupied_seats_arround(layout, x, y) == 0:
                next_layout[x, y] = '#'
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elif layout[x, y] == '#' and occupied_seats_arround(layout, x, y) >= 4:
                next_layout[x, y] = 'L'
    return next_layout


def run():
    print("\nDay 11 - Part A")

    text_input = [list(line.rstrip('\n')) for line in open("Day11/input.txt")]
    # The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
    current_layout = np.array(text_input)
    # Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable
    # and always follow a simple set of rules.
    while True:
        next_layout = generate_next_layout(current_layout)
        if np.array_equal(current_layout, next_layout):
            # At this point, something interesting happens: the chaos stabilizes and further applications of these
            # rules cause no seats to change state! 
            break
        current_layout = next_layout
    # How many seats end up occupied?
    print(np.count_nonzero(current_layout == '#'))
