def is_tree_encountered(map_row, y, delta_x):
    x = delta_x * y
    # Due to something you read about once involving arboreal genetics and biome stability, the same pattern
    # repeats to the right many times.
    return map_row[x % len(map_row)] == '#'


def how_many_trees_encountered(text_input, delta_x, delta_y):
    visited_rows = text_input[::delta_y]  # Jump over the row -> Pick only certain rows for further processing.
    return sum(is_tree_encountered(input_line, int(num), delta_x) for num, input_line in enumerate(visited_rows))


def run():
    print("\nDay 3 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day3/input.txt")]

    # Determine the number of trees you would encounter if, for each of the following slopes,
    # you start at the top-left corner and traverse the map all the way to the bottom:
    #     Right 1, down 1.
    #     Right 3, down 1. (This is the slope you already checked.)
    #     Right 5, down 1.
    #     Right 7, down 1.
    #     Right 1, down 2.
    multiplied_output = 1
    for delta_x, delta_y in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        multiplied_output = multiplied_output * how_many_trees_encountered(text_input, delta_x, delta_y)
    # What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    print(multiplied_output)
