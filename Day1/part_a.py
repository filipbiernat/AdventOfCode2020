from itertools import combinations


def run():
    print("\nDay 1 - Part A")

    text_input = [int(line.rstrip('\n')) for line in open("Day1/input.txt")]
    # Take all two-element combinations of the input set.
    combinations_list = list(combinations(text_input, 2))
    # Find the two entries that sum to 2020.
    entries = next(elem for elem in combinations_list if sum(elem) == 2020)
    # What do you get if you multiply them together?
    print(entries[0] * entries[1])
