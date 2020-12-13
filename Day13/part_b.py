def run():
    print("\nDay 13 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day13/input.txt")]
    # The first line in your input is no longer relevant.
    # The second line lists the bus IDs that are in service according to the shuttle company.
    # An x in the schedule means there are no constraints on what bus IDs must depart at that time.
    departure_time_deltas_dict = {int(bus_id): time_delta
                                  for time_delta, bus_id in enumerate(text_input[1].split(',')) if bus_id != 'x'}

    # The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp such that
    # the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute.
    earliest_timestamp = 0
    product_of_bus_ids_so_far = 1  # For the first bus line, increase the timestamp by one.
    for bus_id, time_delta in departure_time_deltas_dict.items():  # Iterate over bus lines.
        while not (earliest_timestamp + time_delta) % bus_id == 0:  # For the current bus line, keep iterating until the earliest timestamp matches its frequency.
            earliest_timestamp += product_of_bus_ids_so_far  # Jump to the next timestamp, that satisfies all the bus lines so far.
        product_of_bus_ids_so_far *= bus_id  # Before jumping to the next bus line update the product of the bus IDs so far.

    # What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
    print(earliest_timestamp)
