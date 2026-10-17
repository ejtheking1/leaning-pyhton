"""A1.1 - Step 3: arithmetic operators and precedence.

Run me:  python3 03_operators.py

Your snippet had `a + b` and `total / 2` in it. Both look obvious. Both hide
an exam question. This file covers the seven arithmetic operators, the three
that behave unexpectedly, and the bracket mistake that silently gives the
wrong average.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


def show(expression, value):
    print("  %-16s = %-10r (%s)" % (expression, value, type(value).__name__))


# ---------------------------------------------------------------------------
heading("1. All seven, on 7 and 2")

show("7 + 2", 7 + 2)
show("7 - 2", 7 - 2)
show("7 * 2", 7 * 2)
show("7 / 2", 7 / 2)
show("7 // 2", 7 // 2)
show("7 % 2", 7 % 2)
show("7 ** 2", 7 ** 2)


# ---------------------------------------------------------------------------
heading("2. `/` ALWAYS gives a float")

show("7 / 2", 7 / 2)
show("6 / 2", 6 / 2)
print("      ^^^ 3.0, not 3. Even when it divides perfectly.")
show("6 / 3 == 2", 6 / 3 == 2)
print("      ^^^ but it still COMPARES equal to 2. Value vs type again.")
print()
print("  This matters when something needs a whole number:")
print("      a list index must be an int, so values[6 / 2] is a TypeError")
values = [10, 20, 30, 40]
position = 6 / 2                 # a float, even though it is a whole 3.0
try:
    values[position]                           # noqa: B018 - deliberate
except TypeError as error:
    print("      TypeError:", error)
print("      values[6 // 2] works, because // gives an int:",
      values[6 // 2])


# ---------------------------------------------------------------------------
heading("3. `//` floors - it does not round")

for pair in [(7, 2), (-7, 2), (9, 3), (1, 3)]:
    top, bottom = pair
    print("  %3d // %d = %-4d     %3d / %d = %-20r"
          % (top, bottom, top // bottom, top, bottom, top / bottom))

print()
print("  Look at -7 // 2. It is -4, NOT -3.")
print("  `//` always rounds DOWN (towards minus infinity), not towards zero.")
print("  int(-7 / 2) gives", int(-7 / 2), "because int() truncates instead.")
print("  Two operators, two different answers for negatives. Exam material.")


# ---------------------------------------------------------------------------
heading("4. `%` - the remainder, and what it is really for")

print("  The obvious use:")
show("17 % 5", 17 % 5)
print()
print("  Use 1: is it even? (n % 2 == 0)")
for n in [4, 7, 10, 13]:
    print("      %2d %% 2 = %d  ->  %s" % (n, n % 2, "even" if n % 2 == 0 else "odd"))

print()
print("  Use 2: pulling digits apart")
number = 1274
print("      number = %d" % number)
print("      number %% 10  = %d   <- last digit" % (number % 10))
print("      number // 10 = %d  <- everything else" % (number // 10))
print("      repeat those two and you can walk every digit of any number.")

print()
print("  Use 3: wrapping round a cycle (clock faces, days of the week)")
for hour in [13, 23, 25, 36]:
    print("      %2d-hour clock -> %2d on a 12-hour clock" % (hour, hour % 12))

print()
print("  Use 4: converting seconds into minutes and seconds")
seconds = 227
print("      %d seconds = %d min %d sec"
      % (seconds, seconds // 60, seconds % 60))
print("      // gives the whole part, % gives the leftover. A classic pair.")


# ---------------------------------------------------------------------------
heading("5. Precedence - and the average bug")

print("""
  Highest to lowest:

      ()          brackets
      **          exponent
      -x          unary minus
      * / // %    multiply and divide   (left to right)
      + -         add and subtract      (left to right)
""")

first, second = 10.0, 5.0
print("  With first = 10.0 and second = 5.0:")
print()
show("first + second / 2", first + second / 2)
print("      ^^^ WRONG. `/` binds tighter than `+`, so this is")
print("          first + (second / 2)  =  10.0 + 2.5  =  12.5")
show("(first + second) / 2", (first + second) / 2)
print("      ^^^ RIGHT. 7.5. The brackets force the addition to go first.")
print()
print("  Your snippet dodges this by using a `total` variable:")
total = first + second
print("      total = first + second      ->", total)
print("      average = total / 2         ->", total / 2)
print("  Splitting it over two lines makes the order unambiguous. That is a")
print("  perfectly good reason to use an extra variable.")


# ---------------------------------------------------------------------------
heading("6. More precedence traps")

show("2 + 3 * 4", 2 + 3 * 4)
print("      ^^^ 14, not 20")
show("(2 + 3) * 4", (2 + 3) * 4)
print()
show("10 - 4 - 3", 10 - 4 - 3)
print("      ^^^ 3. Left to right: (10 - 4) - 3. NOT 10 - (4 - 3) = 9.")
print()
show("2 ** 3 ** 2", 2 ** 3 ** 2)
print("      ^^^ 512, not 64! `**` is the one that groups RIGHT to left:")
print("          2 ** (3 ** 2) = 2 ** 9 = 512")
print()
show("-3 ** 2", -3 ** 2)
print("      ^^^ -9, because ** beats the minus sign: -(3 ** 2)")
show("(-3) ** 2", (-3) ** 2)
print()
print("  You are never marked down for extra brackets. Use them.")


# ---------------------------------------------------------------------------
heading("7. Floats are not exact")

show("0.1 + 0.2", 0.1 + 0.2)
show("0.1 + 0.2 == 0.3", 0.1 + 0.2 == 0.3)
print()
print("  That is not a Python bug. Computers store floats in binary, and")
print("  0.1 has no exact binary form - just as 1/3 has no exact decimal")
print("  form. Tiny rounding errors are unavoidable.")
print()
print("  Consequences:")
print("      * never test floats with ==; test that the gap is tiny:")
print("        abs((0.1 + 0.2) - 0.3) < 1e-9  ->",
      abs((0.1 + 0.2) - 0.3) < 1e-9)
print("      * for display, round it: round(0.1 + 0.2, 2) =",
      round(0.1 + 0.2, 2))
print("      * for money, work in whole pence as ints, not pounds as floats")


# ---------------------------------------------------------------------------
heading("8. Division by zero")

try:
    1 / 0                                      # noqa: B018 - deliberate
except ZeroDivisionError as error:
    print("  1 / 0  -> ZeroDivisionError:", error)
print()
print("  Harmless-looking in a snippet dividing by a literal 2. Lethal once")
print("  you divide by something that came from the user, or by len(values)")
print("  on an empty list. Guard it:")
print()
print("      if count == 0:")
print("          print(\"No numbers entered.\")")
print("      else:")
print("          print(total / count)")


# ---------------------------------------------------------------------------
heading("9. Predict, then check")

print("  Cover the right column. Work each one out on paper first.\n")

cases = [
    ("9 // 2", 9 // 2),
    ("9 % 2", 9 % 2),
    ("9 / 2", 9 / 2),
    ("4 + 6 / 2", 4 + 6 / 2),
    ("(4 + 6) / 2", (4 + 6) / 2),
    ("7 % 10", 7 % 10),
    ("100 // 7 % 5", 100 // 7 % 5),
    ("2 * 3 ** 2", 2 * 3 ** 2),
    ("int(7 / 2)", int(7 / 2)),
    ("-9 // 2", -9 // 2),
]
for expression, value in cases:
    print("      %-14s ->  %r" % (expression, value))

print()
print("  Got 100%? Move on. Missed any? Scroll back to that section -")
print("  these exact forms turn up in paper 1 every year.")
print()
print("Next:  python3 04_input_output.py")
