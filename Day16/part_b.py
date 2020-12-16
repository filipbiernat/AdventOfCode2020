from re import finditer


def run():
    print("\nDay 16 - Part B")

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
    numbers_on_your_ticket = text_input[first_blank_line_index + 2].split(",")
    numbers_on_other_nearby_tickets = text_input[first_blank_line_index + 5:]
    ticket_length = len(rules_for_ticket_fields)

    category_numbers = [set() for _ in range(ticket_length)]  # Declare empty list of sets (1 set for each possible position).
                                                              # e.g. valid_numbers[0] -> list of all the numbers valid for index 0.
    # Start by determining which tickets are completely invalid; these are tickets that contain values which aren't
    # valid for any field. Ignore your ticket for now.
    for position, rule in enumerate(rules_for_ticket_fields):  # At first, process the ranges.
        match = next(finditer(r"\w+: (\d+)-(\d+) or (\d+)-(\d+)", rule))
        #         1  2     3  4 <- match group
        # class:  1- 3 or  5- 7
        #   row:  6-11 or 33-44
        lower_bounds = int(match.group(1))
        upper_bounds = int(match.group(2)) + 1
        category_numbers[position] = set(range(lower_bounds, upper_bounds))
        lower_bounds = int(match.group(3))
        upper_bounds = int(match.group(4)) + 1
        category_numbers[position].update(range(lower_bounds, upper_bounds))

    ticket_numbers = [set() for _ in range(ticket_length)]  # Declare empty list of sets (1 set for each possible position).
                                                            # e.g. ticket_numbers[0] -> list of all the numbers from valid tickets but only for index 0.
    # Now that you've identified which tickets contain invalid values, discard those tickets entirely.
    # Use the remaining valid tickets to determine which field is which.
    for numbers_on_a_nearby_ticket in numbers_on_other_nearby_tickets:  # Now, process the tickets.
        numbers_on_a_nearby_ticket_list = list(map(int, numbers_on_a_nearby_ticket.split(',')))
        if len(set(numbers_on_a_nearby_ticket_list) - set.union(*category_numbers)) == 0:  # Check if the ticket is valid.
            for position, number in enumerate(numbers_on_a_nearby_ticket_list):
                ticket_numbers[position].add(number)  # Split numbers from every valid ticket. Add them to appropriate lists.

    # Using the valid ranges for each field, determine what order the fields appear on the tickets.
    possible_categories = {}
    for category_index, category_numbers_set in enumerate(category_numbers):  # Try to match the categories with the tickets.
        for ticket_index, ticket_numbers_set in enumerate(ticket_numbers):  # For each category, find at least one set of numbers from valid tickets.
            if len(ticket_numbers_set - category_numbers_set) == 0:  # All the ticket numbers fit in the valid numbers set for this category.
                if ticket_index in possible_categories:  # If success, store in a list.
                    possible_categories[ticket_index].append(category_index)
                else:
                    possible_categories[ticket_index] = [category_index]  # If there's no least for this ticket index, create one.

    ticket_index_for_category = dict()  # So far, we only know possible categories for each position on the ticket.
                                        # Try to map each category to a ticket index.
                                        # Take possible categories and iterate from the shortest category_indices list.
    for ticket_index, category_indices in sorted(possible_categories.items(), key=lambda dict_item: len(dict_item[1])):
        category_indices = list(set(category_indices) - set(ticket_index_for_category.keys())) # Remove category indices that have already been mapped.
        last_category_index = category_indices[0]  # At this stage, there's only one category index left.
        ticket_index_for_category[last_category_index] = ticket_index

    # Once you work out which field is which, look for the six fields on your ticket that start with the word departure.
    output = 1
    for category_index in range(6):
        output *= int(numbers_on_your_ticket[ticket_index_for_category[category_index]])
    # What do you get if you multiply those six values together?
    print(output)
