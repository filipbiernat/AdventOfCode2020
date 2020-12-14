from re import split


def insert_value(memory, address, mask, next_bit_to_process, value_to_insert):  # Use recursion to apply mask on the memory address.
    if next_bit_to_process < 0:  # Eventually, after the mask is applied, insert the value.
        memory[address] = value_to_insert
    elif mask[len(mask)-1-next_bit_to_process] == '0':
        # If the bitmask bit is 0, the corresponding memory address bit is unchanged.
        insert_value(memory, address, mask, next_bit_to_process - 1, value_to_insert)
    elif mask[len(mask)-1-next_bit_to_process] == '1':
        # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
        insert_value(memory, address | (2 ** next_bit_to_process), mask, next_bit_to_process - 1, value_to_insert)
    else:
        # If the bitmask bit is X, the corresponding memory address bit is floating.
        # In practice, this means the floating bits will take on all possible values.
        insert_value(memory, address | (2 ** next_bit_to_process), mask, next_bit_to_process - 1, value_to_insert)
        insert_value(memory, address & ~(2 ** next_bit_to_process), mask, next_bit_to_process - 1, value_to_insert)


def run():
    print("\nDay 14 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day14/input.txt")]

    mem = dict()
    mask = 0
    for command in text_input:
        command_list = split("\] = | = |\[", command)
        # The initialization program can either update the bitmask or write a value to memory.
        if command_list[0] == "mask":
            mask = command_list[1]
        elif command_list[0] == "mem":
            # A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory
            # address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the
            # corresponding bit of the destination memory address.
            insert_value(memory=mem, address=int(command_list[1]), mask=mask, next_bit_to_process=len(mask)-1,
                         value_to_insert=int(command_list[2]))

    # What is the sum of all values left in memory after it completes?
    print(sum(mem.values()))
