import numpy as np


def is_in_grid_range(array, x, y):
    return 0 <= x < array.shape[0] and 0 <= y < array.shape[1]


def is_seat_occupied(array, x, y, dx, dy):  # Check the first seat in this direction.
    i = 1
    while is_in_grid_range(array, x + i * dx, y + i * dy):
        if array[x + i * dx][y + i * dy] == '#':  # Nearest seat occupied.
            return True
        elif array[x + i * dx][y + i * dy] == 'L':  # Nearest seat free.
            return False
        else:  # Floor -> carry on iterating.
            i = i + 1
    return False


def occupied_seats_arround(array, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(is_seat_occupied(array, x, y, dx, dy) for dx, dy in directions)


def generate_next_layout(layout):
    # As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they
    # care about the first seat they can see in each of those eight directions!
    next_layout = layout.copy()
    for x in range(layout.shape[0]):
        for y in range(layout.shape[1]):
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if layout[x, y] == 'L' and occupied_seats_arround(layout, x, y) == 0:
                next_layout[x, y] = '#'
            # Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats
            # for an occupied seat to become empty (rather than four or more from the previous rules).
            elif layout[x, y] == '#' and occupied_seats_arround(layout, x, y) >= 5:
                next_layout[x, y] = 'L'
    return next_layout


def run():
    print("\nDay 11 - Part B")

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
