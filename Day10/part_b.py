from collections import defaultdict


def run():
    print("\nDay 10 - Part B")

    # Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter
    # can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
    text_input = [int(line.rstrip('\n')) for line in open("Day10/input.txt")]

    # Treat the charging outlet near your seat as having an effective joltage rating of 0. In addition, your
    # device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.
    adapters = sorted(text_input + [0, max(text_input) + 3])

    # To completely determine whether you have enough adapters, you'll need to figure out how many different ways
    # they can be arranged. Every arrangement needs to connect the charging outlet to your device.
    ways_to_arrange = defaultdict(lambda: 0)  # If there is no adapter with such joltage, treat it as 0 ways to arrange.
    ways_to_arrange[0] = 1  # At the beginning, there is one way to arrange.

    for adapter in adapters[1:]:  # For each adapter, sum ways to arrange 3 joltages right before.
        ways_to_arrange[adapter] = ways_to_arrange[adapter-1] + ways_to_arrange[adapter-2] + ways_to_arrange[adapter-3]

    # What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
    print(ways_to_arrange[max(adapters)])  # The device is the last item of the adapters list.
