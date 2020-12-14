from re import split


def insert_value(memory, address, mask, next_bit_to_process, value_to_insert):  # Use recursion to apply mask on the value to insert.
    if next_bit_to_process < 0:  # Eventually, after the mask is applied, insert the value.
        memory[address] = value_to_insert
    elif mask[len(mask)-1-next_bit_to_process] == '0':
        # A 0 or 1 overwrites the corresponding bit in the value.
        insert_value(memory, address, mask, next_bit_to_process - 1, value_to_insert & ~(2 ** next_bit_to_process))
    elif mask[len(mask)-1-next_bit_to_process] == '1':
        # A 0 or 1 overwrites the corresponding bit in the value.
        insert_value(memory, address, mask, next_bit_to_process - 1, value_to_insert | (2 ** next_bit_to_process))
    else:
        # An X leaves the bit in the value unchanged.
        insert_value(memory, address, mask, next_bit_to_process - 1, value_to_insert)


def run():
    print("\nDay 14 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day14/input.txt")]

    mem = dict()
    mask = 0
    for command in text_input:
        command_list = split("\] = | = |\[", command)
        # The initialization program can either update the bitmask or write a value to memory.
        if command_list[0] == "mask":
            mask = command_list[1]
        elif command_list[0] == "mem":
            # The current bitmask is applied to values immediately before they are written to memory.
            insert_value(memory=mem, address=int(command_list[1]), mask=mask, next_bit_to_process=len(mask)-1,
                         value_to_insert=int(command_list[2]))

    # What is the sum of all values left in memory after it completes?
    print(sum(mem.values()))