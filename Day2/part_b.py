from re import split


def satisfies_password_policies(input_line):
    # Each line gives the password policy and then the password.
    # 1-3 a: abcde     -> ['1', '3', 'a', 'abcde']
    # 1-3 b: cdefg     -> ['1', '3', 'b', 'cdefg']
    # 2-9 c: ccccccccc -> ['2', '9', 'c', 'ccccccccc']
    # Each policy actually describes two positions in the password, where 1 means the first character,
    # 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept
    # of "index zero"!) Exactly one of these positions must contain the given letter.
    position_1, position_2, given_letter, password = split("-|: | ", input_line)
    return (password[int(position_1) - 1] == given_letter) ^ (password[int(position_2) - 1] == given_letter)


def run():
    print("\nDay 2 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day2/input.txt")]
    # How many passwords are valid according to the new interpretation of the policies?
    print(sum(satisfies_password_policies(elem) for elem in text_input))
