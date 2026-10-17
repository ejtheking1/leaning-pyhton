"""A1.1 - Step 8: the ten mistakes that cost marks.

Run me:  python3 08_pitfalls.py

Every one of these is something that either silently gives a wrong answer or
produces an error message beginners cannot decode. Read the error messages
here, in calm conditions, so you recognise them under exam pressure.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


def pitfall(number, title):
    print()
    print("PITFALL %d - %s" % (number, title))
    print("-" * (len("PITFALL %d - %s" % (number, title))))


# ---------------------------------------------------------------------------
pitfall(1, "forgetting the cast, so you concatenate instead of adding")

print("  WRONG:")
print("      a = input(\"First: \")      # \"10\"")
print("      b = input(\"Second: \")     # \"5\"")
print("      print((a + b) / 2)")
print()
a, b = "10", "5"
print("      a + b is %r, not 15" % (a + b))
try:
    (a + b) / 2
except TypeError as error:
    print("      (a + b) / 2 -> TypeError:", error)
print()
print("  RIGHT:  a = float(input(\"First: \"))")
print("  TELL:   the error says 'str' where you expected a number.")


# ---------------------------------------------------------------------------
pitfall(2, "the missing brackets in an average")

first, second = 10.0, 5.0
print("  WRONG:  average = first + second / 2   ->", first + second / 2)
print("  RIGHT:  average = (first + second) / 2 ->", (first + second) / 2)
print()
print("  No error. No warning. Just a wrong number that looks fine.")
print("  `/` binds tighter than `+`, so the division happens first.")
print("  TELL:   nothing. This is why you TRACE code instead of trusting it.")


# ---------------------------------------------------------------------------
pitfall(3, "using = where you meant ==")

print("  WRONG:  if total = 15:        -> SyntaxError, caught immediately")
print("  RIGHT:  if total == 15:")
print()
print("  Python saves you here. Many languages do not. Remember:")
print("      =   store this value       (a command)")
print("      ==  are these the same?    (a question)")


# ---------------------------------------------------------------------------
pitfall(4, "integer division when you wanted a real answer")

print("  WRONG:  average = (7 + 8) // 2   ->", (7 + 8) // 2)
print("  RIGHT:  average = (7 + 8) / 2    ->", (7 + 8) / 2)
print()
print("  `//` threw the .5 away. Use `//` only when you genuinely want a")
print("  whole number - how many full boxes, how many whole minutes.")
print("  TELL:   your averages are always slightly too low.")


# ---------------------------------------------------------------------------
pitfall(5, "dividing by a count that might be zero")

print("  WRONG:")
print("      average = total / len(numbers)      # numbers might be empty")
numbers = []
try:
    1 / len(numbers)
except ZeroDivisionError as error:
    print("      -> ZeroDivisionError:", error)
print()
print("  RIGHT:")
print("      if len(numbers) == 0:")
print("          print(\"No numbers entered.\")")
print("      else:")
print("          print(total / len(numbers))")
print()
print("  TELL:   works in testing (you always type something), dies the")
print("          first time a real user just presses Enter.")


# ---------------------------------------------------------------------------
pitfall(6, "the hard-coded count")

print("  WRONG:")
print("      total = first + second + third")
print("      average = total / 2            # 2 numbers? there are 3")
print()
print("  The code says 3 in one place and 2 in another. One of them is a")
print("  lie, and the computer believes whichever one it reads.")
print()
print("  RIGHT:  average = total / len(numbers)")
print("  TELL:   nothing at all. Silent wrong answers. Count, never type.")


# ---------------------------------------------------------------------------
pitfall(7, "shadowing a built-in name")

print("  WRONG:  sum = 0        # the built-in sum() is now gone")
print("          input = 5      # input() is now gone, program unusable")
print()
real_list = list
list = [1, 2, 3]                               # noqa: A001 - deliberate
try:
    list("abc")
except TypeError as error:
    print("      after `list = [1, 2, 3]`,  list(\"abc\") -> TypeError:", error)
list = real_list
print("      repaired:  list(\"abc\") =", list("abc"))
print()
print("  RIGHT:  total = 0, values = [1, 2, 3], user_input = 5")
print("  TELL:   a built-in function suddenly 'is not callable'.")


# ---------------------------------------------------------------------------
pitfall(8, "comparing floats with ==")

print("  WRONG:  if 0.1 + 0.2 == 0.3:        ->", 0.1 + 0.2 == 0.3)
print("          because 0.1 + 0.2 is actually", 0.1 + 0.2)
print()
print("  RIGHT:  if abs((0.1 + 0.2) - 0.3) < 1e-9:  ->",
      abs((0.1 + 0.2) - 0.3) < 1e-9)
print()
print("  Floats are stored in binary and 0.1 has no exact binary form, so")
print("  tiny errors are unavoidable. Compare the GAP against a tolerance.")
print("  TELL:   a condition that is obviously true never fires.")


# ---------------------------------------------------------------------------
pitfall(9, "assuming input() ever returns a number")

print("  It does not. Not once. Not ever.")
print()
print("      input() -> str          ALWAYS")
print()
print("  Three signs you forgot a cast:")
print("      * numbers 'add up' to something far too long (105 instead of 15)")
print("      * TypeError mentioning 'str'")
print("      * a comparison like `if age > 18` raises TypeError")
try:
    "17" > 18                                  # noqa: B015 - deliberate
except TypeError as error:
    print("        \"17\" > 18 -> TypeError:", error)


# ---------------------------------------------------------------------------
pitfall(10, "reading a variable before you set it")

print("  WRONG:")
print("      print(total)        # nothing has been stored in total yet")
print("      total = 15")
print()
try:
    print(undefined_total)                     # noqa: F821 - deliberate
except NameError as error:
    print("      -> NameError:", error)
print()
print("  Python runs top to bottom. A name must be assigned on a line that")
print("  has ALREADY RUN. Also catches typos - `print(totl)` is the same")
print("  error, and the message names the misspelling for you. Read it.")


# ---------------------------------------------------------------------------
heading("Spot the bugs")

print("""
Four short programs. Each has exactly one bug. Find it before reading on.

  (a)  first = input("First: ")
       second = input("Second: ")
       print("Average:", (first + second) / 2)

  (b)  total = 0
       for value in [3, 7, 11]:
           total = value
       print("Total:", total)

  (c)  numbers = [4, 8]
       total = 0
       for value in numbers:
           total = total + value
       print("Average:", total / 2)

  (d)  mark = float(input("Mark: "))
       if mark = 100:
           print("Perfect!")
""")

print("""
ANSWERS

  (a)  No float(). `first + second` concatenates the two strings, then
       dividing a str raises TypeError. Fix: float(input(...)) on both.

  (b)  `total = value` instead of `total = total + value`. It overwrites
       the accumulator instead of adding to it, so you get 11 - the last
       value - rather than 21. Pitfall: an accumulator must ACCUMULATE.

  (c)  The hard-coded 2. It is right by luck today and wrong the moment
       numbers has three items. Fix: total / len(numbers).

  (d)  `=` instead of `==`. SyntaxError. Fix: if mark == 100:

  Got all four? You are reading code rather than skimming it, which is the
  whole skill. Now go and earn some marks:
""")

print("    python3 exercises.py")
