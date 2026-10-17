"""A1.1 - Worked answers to exercises.py.

Run me:  python3 solutions.py

Open this AFTER you have had a real attempt at each exercise. Reading a
solution feels like learning and is not; struggling and then reading one
actually is.

Each answer has a note on WHY it is written that way, because the reasoning
is the part that transfers to the next question.
"""


# ---------------------------------------------------------------------------
# PART A - types and casting
# ---------------------------------------------------------------------------

def to_float(text):
    """1. Convert `text` to a float, or None if it is not a number."""
    try:
        return float(text)
    except ValueError:
        return None

# WHY: `return` inside the `try` is the trick. If float() raises, that return
# is never reached and control jumps to the except block. No flag variable,
# no if/else. Catch ValueError specifically - a bare `except:` would also
# swallow Ctrl+C and your own typos.


def is_number(text):
    """2. True if `text` could be converted to a float."""
    return to_float(text) is not None

# WHY: reuse exercise 1 rather than writing another try/except. One place
# that knows how to parse a number means one place to fix if it is wrong.
# Use `is not None`, not `!= None` - None is a single unique object, so
# identity is the right test.
#
# Writing it standalone is equally fine:
#     try:
#         float(text)
#         return True
#     except ValueError:
#         return False


def celsius_to_fahrenheit(celsius):
    """3. F = C * 9/5 + 32."""
    return celsius * 9 / 5 + 32

# WHY: precedence does the right thing here - `*` and `/` both beat `+`, and
# they run left to right, so it is ((celsius * 9) / 5) + 32. Correct.
#
# But `celsius * 9 / 5` vs `celsius * (9 / 5)`: both give the same answer in
# Python 3 because `/` is true division. In a language with integer division,
# 9 / 5 would be 1 and the whole formula would break. Multiplying first is
# the habit that survives moving languages.
#
# Returning 212.0 rather than 212 is expected: `/` always yields a float.


def pounds_to_pence(pounds):
    """4. Convert pounds to a whole number of pence."""
    return int(round(pounds * 100))

# WHY: three steps and all three matter.
#   pounds * 100   -> 0.99 * 100 is 98.99999999999999, not 99 (float binary)
#   round(...)     -> 99.0, fixing that error
#   int(...)       -> 99, a whole number of pence
#
# int(0.99 * 100) alone gives 98. That is a real bug that has shipped in real
# payment code. This is exactly why money is stored as whole pence, not as
# floating-point pounds.


# ---------------------------------------------------------------------------
# PART B - operators
# ---------------------------------------------------------------------------

def split_seconds(total_seconds):
    """5. Split seconds into (minutes, seconds)."""
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

# WHY: // and % are two halves of one division. // gives how many whole 60s
# fit; % gives what is left over. Any "convert a total into bigger units"
# question is this pair: pence to pounds, minutes to hours, items to boxes.
#
# `return minutes, seconds` builds a tuple. The caller unpacks it:
#     mins, secs = split_seconds(227)


def last_digit(number):
    """6. The last digit of a non-negative whole number."""
    return number % 10

# WHY: in base 10, the remainder on division by 10 IS the last digit. The
# string version - int(str(number)[-1]) - works but converts a number to text
# and back for no reason, and it will not earn full marks in a question that
# is testing arithmetic.


def is_even(number):
    """7. True if `number` is even."""
    return number % 2 == 0

# WHY: `number % 2 == 0` is already True or False, so return it directly.
# Writing
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# is not wrong, just four lines doing one line's work. Spotting that a
# comparison IS a boolean is a real step forward.
#
# Note -2 % 2 is 0 in Python, so negatives work without special handling.


def digit_sum(number):
    """8. Sum the digits of a non-negative whole number."""
    total = 0
    while number > 0:
        total = total + number % 10      # take the last digit
        number = number // 10            # and remove it
    return total

# WHY: peel one digit at a time off the right-hand end.
#
#     number = 1274   total = 0
#     1274 % 10 = 4   total = 4     number becomes 127
#      127 % 10 = 7   total = 11    number becomes 12
#       12 % 10 = 2   total = 13    number becomes 1
#        1 % 10 = 1   total = 14    number becomes 0  -> loop ends
#
# The loop condition `number > 0` is what stops it, and it is also why 0
# works: the body never runs and `total` is still 0, which is the right
# answer. Trace the zero case on any loop you write - it is where the marks
# hide.
#
# `while` rather than `for`, because you do not know in advance how many
# digits there are. That is the difference between the two loops.


# ---------------------------------------------------------------------------
# PART C - averages and traversals
# ---------------------------------------------------------------------------

def average_two(first, second):
    """9. The average of exactly two numbers."""
    return (first + second) / 2

# WHY: the brackets are the whole exercise. Without them, `/` goes first and
# you get first + (second / 2) - a different and wrong answer that produces
# no error at all. Your teacher's snippet avoids this by splitting the sum
# into a `total` variable first, which is also a perfectly good answer:
#     total = first + second
#     return total / 2


def average(values):
    """10. The mean of `values`, or None if empty."""
    if len(values) == 0:
        return None
    total = 0
    for value in values:
        total = total + value
    return total / len(values)

# WHY: three separate decisions here.
#
# 1. The empty guard comes FIRST, before any arithmetic. Reach the division
#    with an empty list and you get ZeroDivisionError. Guarding at the top -
#    an "early return" - keeps the rest of the function free to assume it has
#    data, so there is no nesting.
#
# 2. The accumulator starts at 0, because 0 is the value that leaves a sum
#    unchanged. A running product would start at 1 for the same reason.
#
# 3. `len(values)`, never a typed-in count. The data knows how long it is;
#    hard-coding 2 or 3 is how you get silent wrong answers (08_pitfalls.py).
#
# Returning None for "no answer exists" is a design choice and the docstring
# records it. The alternatives - returning 0, or raising ValueError - are
# defensible too, but 0 is a lie: it claims the average is zero.


def percentage(score, total):
    """11. `score` as a percentage of `total`, to 1 dp, or None."""
    if total == 0:
        return None
    return round(score / total * 100, 1)

# WHY: same early-guard shape as exercise 10 - check the impossible case,
# then do the work. `score / total * 100` runs left to right, so it is
# (score / total) * 100. Correct either way here, but think it through
# rather than hoping.
#
# round(x, 1) returns a NUMBER rounded to 1 dp. If you only wanted it to
# LOOK right on screen you would use f"{x:.1f}" and keep full precision for
# any later maths. Rounding a value you will calculate with again loses
# accuracy for good - see 04_input_output.py section 5.


def highest(values):
    """12. The largest value in `values`, or None if empty."""
    if len(values) == 0:
        return None
    best = values[0]                     # start at the first REAL value
    for value in values:
        if value > best:
            best = value
    return best

# WHY: `best = values[0]` is the whole point of the exercise.
#
# Starting at 0 instead looks harmless and is broken:
#     highest([-5, -2])  ->  0, because nothing beats 0
# Zero is not in the list. It was never a candidate. Seeding the running best
# with the first actual element means the answer is always a real member of
# the list, whatever the values are.
#
# The loop re-checks values[0] against itself on the first pass, which is one
# harmless wasted comparison. Starting the loop at values[1:] avoids it and
# is slightly harder to read; either is fine in an exam.
#
# `smallest` is the same function with `<` instead of `>`. Six traversals in
# the lists unit share this shape - see b2_2_lists_and_arrays/02.


# ---------------------------------------------------------------------------
# PART D - output formatting
# ---------------------------------------------------------------------------

def format_money(amount):
    """13. `amount` as a money string, 2 dp, thousands separated."""
    return f"£{amount:,.2f}"

# WHY: one f-string with two specifiers combined. Reading `,.2f` from the
# right: `f` means fixed-point, `.2` means two decimals, `,` means group the
# thousands. So 1234.5 becomes 1,234.50.
#
# The `.2f` also rounds for you, which is why 0.999 comes out as 1.00.
#
# The old way - "£" + str(round(amount, 2)) - gives '£12.5' for 12.5, losing
# the trailing zero, and '£1234.5' with no separator. f-strings are not just
# tidier here; they are more correct.


def summary(values):
    """14. A one-line report about `values`."""
    if len(values) == 0:
        return "no values"

    total = 0
    for value in values:
        total = total + value

    count = len(values)
    word = "value" if count == 1 else "values"
    return f"{count} {word}, total {total:.2f}, average {average(values):.2f}"

# WHY: two things worth noticing.
#
# `"value" if count == 1 else "values"` is a conditional expression - an
# if/else that produces a VALUE rather than choosing which statement runs.
# It is the right tool for picking between two alternatives inline.
#
# And it calls `average(values)` instead of recomputing total / count. The
# mean is already defined, correctly, in one place. Writing the division a
# second time means two places that can disagree - the same mistake as the
# hard-coded 2, in a different coat.
#
# The empty guard returns early again. You have now written that shape four
# times (10, 11, 12, 14). That repetition is deliberate: "handle the
# impossible case first, then assume you have data" is a habit, not a trick.


# ---------------------------------------------------------------------------
# Self-check: these answers run against the real marker.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import exercises                             # noqa: E402

    # Point the marker at the solutions in this file.
    for name in ["to_float", "is_number", "celsius_to_fahrenheit",
                 "pounds_to_pence", "split_seconds", "last_digit", "is_even",
                 "digit_sum", "average_two", "average", "percentage",
                 "highest", "format_money", "summary"]:
        setattr(exercises, name, globals()[name])

    print("A1.1 solutions, checked against the exercise marker")
    exercises._run()
