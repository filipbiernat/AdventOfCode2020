def is_tree_encountered(map_row, y, delta_x):
    x = delta_x * y
    # Due to something you read about once involving arboreal genetics and biome stability, the same pattern
    # repeats to the right many times.
    return map_row[x % len(map_row)] == '#'


def how_many_trees_encountered(text_input):
    # Starting at the top-left corner of your map and following a slope of right 3 and down 1,
    # how many trees would you encounter?
    return sum(is_tree_encountered(input_line, int(num), 3) for num, input_line in enumerate(text_input))


def run():
    print("\nDay 3 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day3/input.txt")]
    print(how_many_trees_encountered(text_input))
