from itertools import combinations


def is_valid_number(number, prev_numbers):
    combinations_list = list(combinations(prev_numbers, 2))
    return any(sum(elem) == number for elem in combinations_list)


def run():
    print("\nDay 9 - Part A")

    text_input = [int(line.rstrip('\n')) for line in open("Day9/input.txt")]

    # XMAS starts by transmitting a preamble of 25 numbers.
    preamble_len = 25
    # After that, each number you receive should be the sum of any two of the 25 immediately previous numbers.
    # The two numbers will have different values, and there might be more than one such pair.
    # What is the first number that does not have this property?
    first_invalid_number = next(text_input[i] for i in range(preamble_len, len(text_input))
                                if not is_valid_number(text_input[i], text_input[i - preamble_len:i]))
    print(first_invalid_number)
