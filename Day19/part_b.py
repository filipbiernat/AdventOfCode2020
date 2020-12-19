from re import search


def generate_regex_for_option(rule_dict, rule_option, rule_index, same_index_cnt):
    single_character_match = search(r"\"(\S)\"", rule_option)  # Check for a single character in quotation marks.
    if single_character_match is not None:
        # Some rules, like 3: "b", simply match a single character
        return single_character_match.group(1)
    else:
        # The remaining rules list the sub-rules that must be followed; for example, the rule 0: 1 2 means that to
        # match rule 0, the text being checked must match rule 1, and the text after the part that matched rule 1
        # must then match rule 2.
        rule_indices = [int(elem) for elem in rule_option.split()]

        # The rules do contain loops, and the list of messages they could hypothetically match is infinite
        same_index_cnt = same_index_cnt + 1 if rule_index in rule_indices else 0  # Calculate repetitions
        if same_index_cnt > 5:  # Stop if number of index repetitions exceeds the threshold.
            return ""

        return "".join(list(map(lambda rule_index: generate_regex(rule_dict, rule_index, same_index_cnt), rule_indices)))


def generate_regex(rule_dict, rule_index=0, same_index_cnt=0):
    # Some of the rules have multiple lists of sub-rules separated by a pipe (|).
    # This means that at least one list of sub-rules must match.
    rule_options = rule_dict[rule_index].split("|")
    regexes_for_options = list(map(lambda x: generate_regex_for_option(rule_dict, x, rule_index, same_index_cnt), rule_options))
    return "(" + "|".join(regexes_for_options) + ")" if len(regexes_for_options) > 1 else regexes_for_options[0]


def is_message_valid(valid_message_regex, message):  # Check if regex is satisfied and if the message fills the whole regex.
    return search("^" + valid_message_regex + "$", message) is not None


def run():
    print("\nDay 19 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day19/input.txt")]
    # They sent you a list of the rules valid messages should obey and a list of received messages they've collected so far.
    blank_line_index = text_input.index('')
    rule_list = text_input[:blank_line_index]  # First, there's a series of rules.
    message_list = text_input[blank_line_index + 1:]  # Then, there's a blank line and finally a series of messages.

    # The rules for valid messages are numbered and build upon each other.
    rule_dict = dict()  # Convert rules to a dictionary.
    for rule in rule_list:
        key, value = rule.split(":")
        rule_dict[int(key)] = value

    # As you look over the list of messages, you realize your matching rules aren't quite right.
    # To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:
    rule_dict[8] = "42 | 42 8"
    rule_dict[11] = "42 31 | 42 11 31"

    valid_message_regex = generate_regex(rule_dict)
    # How many messages completely match rule 0?
    print(sum(list(map(lambda x: is_message_valid(valid_message_regex, x), message_list))))

