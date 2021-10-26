"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    # example "/ 6 - 4 2"
    # "6 4 / 2 -"
    tokens = s.split(" ")
    stack = []
    operators = ["+", "-", "*", "/"]


    while len(tokens) > 0:
        tolken = tokens[-1]
        if tolken not in operators:
            stack.append(int(tokens.pop()))
        else:
            first_op = stack.pop()
            second_op = stack.pop()
            sol = 0
            if tolken == "+":
                sol = first_op + second_op
            elif tolken == "-":
                sol = first_op - second_op
            elif tolken == "*":
                sol = first_op * second_op
            elif tolken == "/":
                sol = first_op // second_op
            stack.append(sol)
            tokens.pop()
    return stack.pop()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
