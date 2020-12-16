from re import finditer


def run():
    print("\nDay 16 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day16/input.txt")]
    # You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for
    # the same train service (via the airport security cameras) together into a single document you can reference
    first_blank_line_index = text_input.index('')
    # class: 1-3 or 5-7
    # row: 6-11 or 33-44
    # seat: 13-40 or 45-50
    #
    # your ticket:
    # 7,1,14
    #
    # nearby tickets:
    # 7,3,47
    # 40,4,50
    # 55,2,20
    # 38,6,12
    rules_for_ticket_fields = text_input[:first_blank_line_index]
    numbers_on_your_ticket = text_input[first_blank_line_index + 2]
    numbers_on_other_nearby_tickets = text_input[first_blank_line_index + 5:]

    # Start by determining which tickets are completely invalid; these are tickets that contain values which aren't
    # valid for any field. Ignore your ticket for now.
    set_of_valid_numbers = set()
    for rule in rules_for_ticket_fields:
        match = next(finditer(r"\w+: (\d+)-(\d+) or (\d+)-(\d+)", rule))
        #         1  2     3  4 <- match group
        # class:  1- 3 or  5- 7
        #   row:  6-11 or 33-44
        lower_bounds = int(match.group(1))
        upper_bounds = int(match.group(2)) + 1
        set_of_valid_numbers.update(range(lower_bounds, upper_bounds))
        lower_bounds = int(match.group(3))
        upper_bounds = int(match.group(4)) + 1
        set_of_valid_numbers.update(range(lower_bounds, upper_bounds))

    # Adding together all of the invalid values produces your ticket scanning error rate
    scanning_error_rate = 0
    for numbers_on_a_nearby_ticket in numbers_on_other_nearby_tickets:
        set_of_numbers_on_a_nearby_ticket = set(map(int, numbers_on_a_nearby_ticket.split(',')))
        scanning_error_rate += sum(set_of_numbers_on_a_nearby_ticket - set_of_valid_numbers)

    # Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
    print(scanning_error_rate)
