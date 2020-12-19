from re import sub


class CustomInt(int):
    def __add__(self, other):
        return CustomInt(int(self) + int(other))

    def __sub__(self, other):  # Override subtraction with multiplication.
        return CustomInt(int(self) * int(other))


def eval_formula(formula):
    # The rules of operator precedence have changed. Rather than evaluating multiplication before addition, the
    # operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
    formula = formula.replace("*", "-")  # Replace multiplication with subtraction.
    formula = sub(r"\d+", lambda elem: "CustomInt(" + elem.group() + ")", formula)  # Cast all the integers to CustomInt.
    return eval(formula)


def run():
    print("\nDay 18 - Part A")

    text_input = [line.rstrip('\n') for line in open("Day18/input.txt")]

    # Evaluate the expression on each line of the homework; what is the sum of the resulting values?
    print(sum(list(map(eval_formula, text_input))))
