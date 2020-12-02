from re import split


def satisfies_password_policies(input_line):
    # Each line gives the password policy and then the password.
    # 1-3 a: abcde     -> ['1', '3', 'a', 'abcde']
    # 1-3 b: cdefg     -> ['1', '3', 'b', 'cdefg']
    # 2-9 c: ccccccccc -> ['2', '9', 'c', 'ccccccccc']
    # The password policy indicates the lowest and highest number of times a given letter
    # must appear for the password to be valid. For example, 1-3 a means that the password
    # must contain a at least 1 time and at most 3 times.
    min_occurrences, max_occurrences, given_letter, password = split("-|: | ", input_line)
    return int(min_occurrences) <= password.count(given_letter) <= int(max_occurrences)


def run():
    print("\nDay 2 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day2/input.txt")]
    # How many passwords are valid according to their policies?
    print(sum(satisfies_password_policies(elem) for elem in text_input))
