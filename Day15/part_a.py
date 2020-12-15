from collections import defaultdict


def run():
    print("\nDay 15 - Part A")

    text_input = next(open("Day15/input.txt")).split(',')

    last_number = text_input[-1]
    positions_dict = defaultdict(lambda: 0)  # If no such number, the defaultdict will return 0.

    # In this game, the players take turns saying numbers.
    # They begin by taking turns reading from a list of starting numbers.
    for position, elem in enumerate(text_input, 1):  # Parse input
        positions_dict[int(elem)] = position

    # Then, each turn consists of considering the most recently spoken number.
    for position in range(len(text_input), 2020):
        prev_position = positions_dict[last_number]  # If new number, the defaultdict will return prev_position = 0.
        positions_dict[last_number] = position  # First, read the previous position. Then, override it. Not before.

        if prev_position == 0:
            # If that was the first time the number has been spoken, the current player says 0.
            last_number = 0
        else:
            # Otherwise, the number had been spoken before; the current player announces how many turns apart the
            # number is from when it was previously spoken.
            last_number = position - prev_position

    # Given your starting numbers, what will be the 2020th number spoken?
    print(last_number)
