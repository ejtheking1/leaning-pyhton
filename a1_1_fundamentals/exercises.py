"""A1.1 - Practice. 14 exercises with a built-in marker.

Run me:  python3 exercises.py

Replace each `raise NotImplementedError` with your own code, then run the
file again. It tells you which ones pass.

Rules of the game:

  * Use explicit loops and arithmetic. No sum(), max(), min(), sorted(),
    statistics.mean() or list comprehensions - the point is to be able to
    write the algorithm, which is what the exam asks for. len() is fine.
  * Every function RETURNS its answer. None of them print, and none of them
    call input(). That is what makes them markable - see 07_functions.py.
  * Decide what happens on empty or impossible input; each docstring says
    what is expected.
  * Worked answers are in solutions.py. Try first, then compare.
"""


# ---------------------------------------------------------------------------
# PART A - types and casting
# ---------------------------------------------------------------------------

def to_float(text):
    """1. Convert `text` to a float. Return None if it is not a number.

    to_float("3.5")  -> 3.5
    to_float("  7 ") -> 7.0      (float() copes with spaces itself)
    to_float("ten")  -> None
    to_float("")     -> None
    Hint: try / except ValueError. Return inside the try.
    """
    raise NotImplementedError


def is_number(text):
    """2. Return True if `text` could be converted to a float.

    is_number("42")    -> True
    is_number("-3.5")  -> True
    is_number("4e2")   -> True      (scientific notation IS a valid float)
    is_number("ten")   -> False
    Hint: you already wrote the hard part in exercise 1.
    """
    raise NotImplementedError


def celsius_to_fahrenheit(celsius):
    """3. Convert a temperature. F = C * 9/5 + 32.

    celsius_to_fahrenheit(100) -> 212.0
    celsius_to_fahrenheit(0)   -> 32.0
    celsius_to_fahrenheit(-40) -> -40.0
    Hint: watch precedence - C * 9/5 is fine, but think about why.
    """
    raise NotImplementedError


def pounds_to_pence(pounds):
    """4. Convert pounds to a whole number of pence.

    pounds_to_pence(12.5)   -> 1250
    pounds_to_pence(0.99)   -> 99
    pounds_to_pence(3.456)  -> 346        (rounded, NOT truncated)
    Hint: multiply, then round(), then int(). int() alone would truncate,
    and 0.99 * 100 is stored as 98.99999999999999 - try it and see.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART B - operators
# ---------------------------------------------------------------------------

def split_seconds(total_seconds):
    """5. Split a count of seconds into whole minutes and seconds.

    split_seconds(227) -> (3, 47)
    split_seconds(60)  -> (1, 0)
    split_seconds(45)  -> (0, 45)
    Return a tuple (minutes, seconds). Hint: // and % are a pair.
    """
    raise NotImplementedError


def last_digit(number):
    """6. Return the last digit of a non-negative whole number.

    last_digit(1274) -> 4
    last_digit(7)    -> 7
    last_digit(0)    -> 0
    Hint: one operator does this. No strings allowed.
    """
    raise NotImplementedError


def is_even(number):
    """7. Return True if `number` is even.

    is_even(4)  -> True
    is_even(7)  -> False
    is_even(0)  -> True
    is_even(-2) -> True
    Hint: % 2 == 0. Return the comparison directly - no if/else needed.
    """
    raise NotImplementedError


def digit_sum(number):
    """8. Return the sum of the digits of a non-negative whole number.

    digit_sum(1274) -> 14        (1 + 2 + 7 + 4)
    digit_sum(9)    -> 9
    digit_sum(0)    -> 0
    No str() and no indexing - use % 10 and // 10 in a while loop.
    Hint: while number > 0, peel off the last digit, then shrink the number.
    Careful: 0 must still give 0, so check your loop handles it.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART C - averages and traversals
# ---------------------------------------------------------------------------

def average_two(first, second):
    """9. Return the average of exactly two numbers.

    average_two(10, 5) -> 7.5
    average_two(7, 8)  -> 7.5
    average_two(-2, 2) -> 0.0
    This is your teacher's snippet as a function. Mind the brackets.
    """
    raise NotImplementedError


def average(values):
    """10. Return the mean of `values`, or None if the list is empty.

    average([10, 5, 9]) -> 8.0
    average([4])        -> 4.0
    average([])         -> None
    Accumulator loop plus len(). No sum(). Guard the empty case FIRST.
    """
    raise NotImplementedError


def percentage(score, total):
    """11. Return score as a percentage of total, rounded to 1 dp.

    percentage(17, 20) -> 85.0
    percentage(2, 3)   -> 66.7
    percentage(5, 0)   -> None      (a percentage of nothing is meaningless)
    Hint: guard total == 0 before dividing. round(x, 1) for the rounding.
    """
    raise NotImplementedError


def highest(values):
    """12. Return the largest value in `values`, or None if empty.

    highest([3, 9, 2]) -> 9
    highest([-5, -2])  -> -2
    highest([])        -> None
    No max(). Hint: start your running best at the FIRST element, not 0 -
    starting at 0 breaks on all-negative lists. Work out why.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART D - output formatting
# ---------------------------------------------------------------------------

def format_money(amount):
    """13. Return `amount` as a money string with 2 decimal places.

    format_money(12.5)    -> '£12.50'
    format_money(0.999)   -> '£1.00'
    format_money(1234.5)  -> '£1,234.50'
    Hint: one f-string. The spec you want combines ',' and '.2f'.
    """
    raise NotImplementedError


def summary(values):
    """14. Return a one-line report about `values`.

    summary([10, 5, 9]) -> '3 values, total 24.00, average 8.00'
    summary([4])        -> '1 value, total 4.00, average 4.00'
    summary([])         -> 'no values'
    Note: 'value' is singular for exactly one. Totals to 2 decimal places.
    Hint: reuse average(). Build the string with an f-string.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# The marker. You do not need to read past here, but you may.
# ---------------------------------------------------------------------------

def _same(got, expected):
    """Compare, allowing for float imprecision."""
    if isinstance(expected, bool):
        return isinstance(got, bool) and got == expected
    if (isinstance(expected, float)
            and isinstance(got, (int, float))
            and not isinstance(got, bool)):
        return abs(got - expected) < 1e-9
    if isinstance(expected, tuple) and isinstance(got, tuple):
        return (len(got) == len(expected)
                and all(_same(g, e) for g, e in zip(got, expected)))
    return got == expected


def _check(label, got, expected):
    if _same(got, expected):
        print("  PASS  %-38s -> %r" % (label, got))
        return True
    print("  FAIL  %-38s -> %r   (expected %r)" % (label, got, expected))
    return False


def _run():
    passed = 0
    attempted = 0
    skipped = []

    cases = [
        (1, 'to_float("3.5")', lambda: to_float("3.5"), 3.5),
        (1, 'to_float("  7 ")', lambda: to_float("  7 "), 7.0),
        (1, 'to_float("ten")', lambda: to_float("ten"), None),
        (1, 'to_float("")', lambda: to_float(""), None),

        (2, 'is_number("42")', lambda: is_number("42"), True),
        (2, 'is_number("-3.5")', lambda: is_number("-3.5"), True),
        (2, 'is_number("4e2")', lambda: is_number("4e2"), True),
        (2, 'is_number("ten")', lambda: is_number("ten"), False),

        (3, "celsius_to_fahrenheit(100)",
         lambda: celsius_to_fahrenheit(100), 212.0),
        (3, "celsius_to_fahrenheit(0)",
         lambda: celsius_to_fahrenheit(0), 32.0),
        (3, "celsius_to_fahrenheit(-40)",
         lambda: celsius_to_fahrenheit(-40), -40.0),

        (4, "pounds_to_pence(12.5)", lambda: pounds_to_pence(12.5), 1250),
        (4, "pounds_to_pence(0.99)", lambda: pounds_to_pence(0.99), 99),
        (4, "pounds_to_pence(3.456)", lambda: pounds_to_pence(3.456), 346),

        (5, "split_seconds(227)", lambda: split_seconds(227), (3, 47)),
        (5, "split_seconds(60)", lambda: split_seconds(60), (1, 0)),
        (5, "split_seconds(45)", lambda: split_seconds(45), (0, 45)),

        (6, "last_digit(1274)", lambda: last_digit(1274), 4),
        (6, "last_digit(7)", lambda: last_digit(7), 7),
        (6, "last_digit(0)", lambda: last_digit(0), 0),

        (7, "is_even(4)", lambda: is_even(4), True),
        (7, "is_even(7)", lambda: is_even(7), False),
        (7, "is_even(0)", lambda: is_even(0), True),
        (7, "is_even(-2)", lambda: is_even(-2), True),

        (8, "digit_sum(1274)", lambda: digit_sum(1274), 14),
        (8, "digit_sum(9)", lambda: digit_sum(9), 9),
        (8, "digit_sum(0)", lambda: digit_sum(0), 0),

        (9, "average_two(10, 5)", lambda: average_two(10, 5), 7.5),
        (9, "average_two(7, 8)", lambda: average_two(7, 8), 7.5),
        (9, "average_two(-2, 2)", lambda: average_two(-2, 2), 0.0),

        (10, "average([10, 5, 9])", lambda: average([10, 5, 9]), 8.0),
        (10, "average([4])", lambda: average([4]), 4.0),
        (10, "average([])", lambda: average([]), None),

        (11, "percentage(17, 20)", lambda: percentage(17, 20), 85.0),
        (11, "percentage(2, 3)", lambda: percentage(2, 3), 66.7),
        (11, "percentage(5, 0)", lambda: percentage(5, 0), None),

        (12, "highest([3, 9, 2])", lambda: highest([3, 9, 2]), 9),
        (12, "highest([-5, -2])", lambda: highest([-5, -2]), -2),
        (12, "highest([])", lambda: highest([]), None),

        (13, "format_money(12.5)", lambda: format_money(12.5), "£12.50"),
        (13, "format_money(0.999)", lambda: format_money(0.999), "£1.00"),
        (13, "format_money(1234.5)",
         lambda: format_money(1234.5), "£1,234.50"),

        (14, "summary([10, 5, 9])", lambda: summary([10, 5, 9]),
         "3 values, total 24.00, average 8.00"),
        (14, "summary([4])", lambda: summary([4]),
         "1 value, total 4.00, average 4.00"),
        (14, "summary([])", lambda: summary([]), "no values"),
    ]

    current = None
    for number, label, call, expected in cases:
        if number != current:
            current = number
            print()
            print("Exercise %d" % number)
        try:
            got = call()
        except NotImplementedError:
            print("  ----  %-38s not attempted yet" % label)
            if number not in skipped:
                skipped.append(number)
            continue
        except Exception as error:               # noqa: BLE001 - teaching tool
            print("  ERROR %-38s raised %s: %s"
                  % (label, type(error).__name__, error))
            attempted += 1
            continue
        attempted += 1
        if _check(label, got, expected):
            passed += 1

    print()
    print("=" * 68)
    print("Attempted %d checks, passed %d." % (attempted, passed))
    if skipped:
        print("Still to do: exercise(s) "
              + ", ".join(str(n) for n in skipped))
    elif passed == attempted:
        print("All of them. Open solutions.py and compare approaches -")
        print("there is usually more than one correct answer.")
        print("Then try quiz.md for the written, exam-style questions.")
    print("=" * 68)


if __name__ == "__main__":
    print("A1.1 exercise marker")
    _run()
