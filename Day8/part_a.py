def run_program(program):
    # The accumulator starts at 0.
    accumulator = 0
    instruction_address = 0
    executed_instruction_addresses = set()

    while instruction_address not in executed_instruction_addresses:
        executed_instruction_addresses.add(instruction_address)
        instruction, argument = program[instruction_address].split()
        if instruction == "acc":
            # acc increases or decreases a single global value called the accumulator by the value given in the argument.
            accumulator = accumulator + int(argument)
            # After an acc instruction, the instruction immediately below it is executed next.
            instruction_address = instruction_address + 1
        elif instruction == "jmp":
            # jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the
            # argument as an offset from the jmp instruction
            instruction_address = instruction_address + int(argument)
        elif instruction == "nop":
            # nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
            instruction_address = instruction_address + 1
    return accumulator


def run():
    print("\nDay 8 - Part A")

    # The boot code is represented as a text file with one instruction per line of text.
    input_program = [line.rstrip('\n') for line in open("Day8/input.txt")]

    # Immediately before any instruction is executed a second time, what value is in the accumulator?
    print(run_program(input_program))
