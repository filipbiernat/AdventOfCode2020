from re import sub


class CustomInt(int):
    def __mul__(self, other):  # Override multiplication with addition.
        return CustomInt(int(self) + int(other))

    def __sub__(self, other):  # Override subtraction with multiplication.
        return CustomInt(int(self) * int(other))


def eval_formula(formula):
    # Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
    # Instead, addition is evaluated before multiplication.
    formula = formula.replace("*", "-")  # Replace multiplication with subtraction.
    formula = formula.replace("+", "*")  # Replace addition with multiplication.
    formula = sub(r"\d+", lambda elem: "CustomInt(" + elem.group() + ")", formula)  # Cast all the integers to CustomInt.
    return eval(formula)


def run():
    print("\nDay 18 - Part B")

    text_input = [line.rstrip('\n') for line in open("Day18/input.txt")]

    # What do you get if you add up the results of evaluating the homework problems using these new rules?
    print(sum(list(map(eval_formula, text_input))))
