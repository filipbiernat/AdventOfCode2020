def departure_timestamp(earliest_timestamp, bus_id):  # Calculate the next departure timestamp after earliest timestamp.
    # Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point
    # in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to
    # the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.
    return earliest_timestamp + bus_id - earliest_timestamp % bus_id


def run():
    print("\nDay 13 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day13/input.txt")]
    # The first line is your estimate of the earliest timestamp you could depart on a bus.
    earliest_timestamp = int(text_input[0])
    # The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must
    # be out of service, so you decide to ignore them.
    departure_timestamps_dict = {int(bus_id): departure_timestamp(earliest_timestamp, int(bus_id))
                                 for bus_id in text_input[1].split(',') if bus_id != 'x'}

    # To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport.
    earliest_bus_id = min(departure_timestamps_dict, key=departure_timestamps_dict.get)

    # What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to
    # wait for that bus?
    print(earliest_bus_id * (departure_timestamps_dict[earliest_bus_id] - earliest_timestamp))
