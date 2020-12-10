from numpy import diff


def run():
    print("\nDay 10 - Part A")

    # Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter
    # can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
    text_input = [int(line.rstrip('\n')) for line in open("Day10/input.txt")]

    # Treat the charging outlet near your seat as having an effective joltage rating of 0. In addition, your
    # device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.
    adapters = sorted(text_input + [0, max(text_input) + 3])

    # If you use every adapter in your bag at once, what is the distribution of joltage differences between the
    # charging outlet, the adapters, and your device?
    joltage_differences = list(diff(adapters))

    # What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
    print(joltage_differences.count(1) * joltage_differences.count(3))
