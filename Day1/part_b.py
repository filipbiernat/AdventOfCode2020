from itertools import combinations


def run():
    print("\nDay 1 - Part B")

    text_input = [int(line.rstrip('\n')) for line in open("Day1/input.txt")]
    # Take all three-element combinations of the input set.
    combinations_list = list(combinations(text_input, 3))
    # They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
    entries = next(elem for elem in combinations_list if sum(elem) == 2020)
    # What is the product of the three entries that sum to 2020?
    print(entries[0] * entries[1] * entries[2])
