def get_num_questions_everyone_answered_yes(group_answers):
    group_answers_list_of_sets = [set(elem) for elem in group_answers.split()]  # One set for every group member
    # You need to identify the questions to which everyone answered "yes"!
    return len(set.intersection(*group_answers_list_of_sets))


def run():
    print("\nDay 6 - Part B")

    # Each group's answers are separated by a blank line, and within each group, each person's
    # answers are on a single line.
    input_entries = open("Day6/input.txt").read().split("\n\n")
    # What is the sum of those counts?
    print(sum(map(get_num_questions_everyone_answered_yes, input_entries)))
