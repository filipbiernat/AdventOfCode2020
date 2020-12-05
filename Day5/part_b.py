def binary_space_partition(seat_info, start_position=0):
    # Instead of zones or groups, this airline uses binary space partitioning to seat people.
    # A seat might be specified like FBFBBFFRLR.
    # F means to take the lower half, B means to take the upper half.
    # L means to take the lower half, R means to take the upper half.
    upper_half = seat_info[0] == "B" or seat_info[0] == "R"
    next_position = start_position + 2 ** (len(seat_info) - 1) if upper_half else start_position
    # The next letter indicates which half of that region the seat is in, and so on until
    # you're left with exactly one row.
    return binary_space_partition(seat_info[1:], next_position) if len(seat_info) > 1 else next_position


def calculate_seat_id(seat_info):
    # The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
    # (numbered 0 through 127). Each letter tells you which half of a region the given seat is in.
    # The last three characters will be either L or R; these specify exactly one of the 8 columns of seats
    # on the plane (numbered 0 through 7).
    # Every seat also has a unique seat ID: multiply the row by 8, then add the column.
    return binary_space_partition(seat_info[:7]) * 8 + binary_space_partition(seat_info[7:10])


def run():
    print("\nDay 5 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day5/input.txt")]

    # It's a completely full flight, so your seat should be the only missing boarding pass in your list.
    taken_seats = sorted(list(map(calculate_seat_id, text_input)))
    free_seats = [seat_id for seat_id in range(max(taken_seats) + 1) if seat_id not in taken_seats]
    # Your seat should be the only missing boarding pass in your list. However, there's a catch: some of
    # the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing
    # from your list as well. Your seat wasn't at the very front or back, though; the seats with IDs +1 and
    # -1 from yours will be in your list.
    # What is the ID of your seat?
    print(next(seat_id for seat_id in free_seats if (seat_id+1 in taken_seats) and (seat_id-1 in taken_seats)))
