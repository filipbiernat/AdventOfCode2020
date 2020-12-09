from itertools import combinations


def is_valid_number(number, prev_numbers):
    combinations_list = list(combinations(prev_numbers, 2))
    return any(sum(elem) == number for elem in combinations_list)


def find_a_contiguous_set(text_input, first_invalid_number):  # Sliding window
    for start_pos in range(len(text_input)-1):
        sum_of_elements = text_input[start_pos]
        for end_pos in range(start_pos + 1, len(text_input)):
            sum_of_elements = sum_of_elements + text_input[end_pos]
            if sum_of_elements > first_invalid_number:
                break
            elif sum_of_elements == first_invalid_number:
                return text_input[start_pos:end_pos+1]


def run():
    print("\nDay 9 - Part B")

    text_input = [int(line.rstrip('\n')) for line in open("Day9/input.txt")]

    # XMAS starts by transmitting a preamble of 25 numbers.
    preamble_len = 25
    # After that, each number you receive should be the sum of any two of the 25 immediately previous numbers.
    # The two numbers will have different values, and there might be more than one such pair.
    # What is the first number that does not have this property?
    first_invalid_number = next(text_input[i] for i in range(preamble_len, len(text_input))
                                if not is_valid_number(text_input[i], text_input[i - preamble_len:i]))

    # You must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    contiguous_set = find_a_contiguous_set(text_input, first_invalid_number)
    # To find the encryption weakness, add together the smallest and largest number in this contiguous range.
    # What is the encryption weakness in your XMAS-encrypted list of numbers?
    print(max(contiguous_set) + min(contiguous_set))
