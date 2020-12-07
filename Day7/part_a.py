from re import match, findall


def fill_parent_dict(input_line, bags_dict):
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    # dotted black bags contain no other bags.
    outside_bag = match(r'([a-z]+ [a-z]+)', input_line)[0]
    inside_bags = findall(r'([0-9]+) ([a-z]+ [a-z]+)', input_line)
    for inside_bag_cnt, inside_bag_color in inside_bags:
        if inside_bag_color not in bags_dict:  # Add to dict if new color.
            bags_dict[inside_bag_color] = []
        bags_dict[inside_bag_color].append(outside_bag)  # Add to list for this color.


def get_all_bags_containing_bag_of_color(bag_color, bags_dict):
    all_bags_containing_bag_of_color = set()
    if bag_color in bags_dict:
        for outside_bag_color in bags_dict[bag_color]:  # Iterate over bags which can contain our bag.
            all_bags_containing_bag_of_color.add(outside_bag_color)   # Add this color and all the outside bag colors.
            all_bags_containing_bag_of_color.update(get_all_bags_containing_bag_of_color(outside_bag_color, bags_dict))
    return all_bags_containing_bag_of_color


def run():
    print("\nDay 7 - Part A")

    # Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and
    # their contents; bags must be color-coded and must contain specific quantities of other color-coded bags.
    bags_dict = dict()
    text_input = [line.rstrip('\n') for line in open("Day7/input.txt")]
    for input_line in text_input:
        fill_parent_dict(input_line, bags_dict)

    # How many bag colors can eventually contain at least one shiny gold bag?
    print(len(get_all_bags_containing_bag_of_color("shiny gold", bags_dict)))
