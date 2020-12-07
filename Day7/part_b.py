from re import match, findall


def fill_parent_dict(input_line, bags_dict):
    # light red bags contain 1 bright white bag, 2 muted yellow bags.
    # dotted black bags contain no other bags.
    outside_bag = match(r'([a-z]+ [a-z]+)', input_line)[0]
    inside_bags = findall(r'([0-9]+) ([a-z]+ [a-z]+)', input_line)
    bags_dict[outside_bag] = inside_bags


def calc_bags_inside(bag_color, bags_dict):
    cnt = 0
    if bag_color in bags_dict:
        for next_bag_cnt, next_bag_color in bags_dict[bag_color]:  # Iterate over bags which have to be inside our bag.
            cnt = cnt + int(next_bag_cnt) * (calc_bags_inside(next_bag_color, bags_dict) + 1)  # Add this color and all the inside bag colors.
    return cnt


def run():
    print("\nDay 7 - Part B")

    # Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and
    # their contents; bags must be color-coded and must contain specific quantities of other color-coded bags.
    bags_dict = dict()
    text_input = [line.rstrip('\n') for line in open("Day7/input.txt")]
    for input_line in text_input:
        fill_parent_dict(input_line, bags_dict)

    # How many individual bags are required inside your single shiny gold bag?
    print(calc_bags_inside("shiny gold", bags_dict))