"""A1.1 - Step 2: variables, types and casting.

Run me:  python3 02_variables_and_types.py

Your snippet had `float(...)` in it. This file is about WHY, and about the
one idea that trips up more beginners than anything else: "42" is not 42.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


def show(label, value):
    """Print a value with its repr and its type."""
    print("  %-22s = %-12r (%s)" % (label, value, type(value).__name__))


# ---------------------------------------------------------------------------
heading("1. Assignment is right-to-left")

score = 7
print("  score = 7      ->  the value 7 is made, then `score` points at it")
show("score", score)

score = score + 3
print()
print("  score = score + 3")
print("      step 1: work out the RIGHT side ......  7 + 3  ->  10")
print("      step 2: re-point `score` at the answer")
show("score", score)
print()
print("  This is why `score = score + 3` is not circular nonsense.")
print("  Shorthand for the same thing:  score += 3")

score += 3
show("score (after += 3)", score)


# ---------------------------------------------------------------------------
heading("2. `=` versus `==`")

x = 5                      # assignment: store 5 in x
print("  x = 5    stores 5 in x. It is a STATEMENT and has no value.")
print("  x == 5   ASKS whether x is 5. It is an EXPRESSION worth", x == 5)
print("  x == 9   asks the same question, answer", x == 9)
print()
print("  Mixing these up is the #1 beginner bug. Python protects you:")
print("  writing `if x = 5:` is a SyntaxError, not a silent disaster.")


# ---------------------------------------------------------------------------
heading("3. The four types you need")

show("an integer", 42)
show("a float", 42.0)
show("a string", "42")
show("a boolean", True)
print()
print("  42 and 42.0 and \"42\" all LOOK like forty-two on screen.")
print("  Python treats them as three different things.")


# ---------------------------------------------------------------------------
heading("4. The big one: \"42\" is not 42")

print("  `+` does two completely different jobs depending on the types:")
print()
show('"42" + "7"', "42" + "7")
print("      ^ CONCATENATION. Two strings get glued together.")
show("42 + 7", 42 + 7)
print("      ^ ADDITION. Two numbers get summed.")
print()
print('  And "42" + 7 does neither, because Python refuses to guess:')
try:
    "42" + 7                                   # noqa: B018 - deliberate error
except TypeError as error:
    print("      TypeError:", error)
print()
print("  That error message is a GIFT. It is telling you exactly which")
print("  conversion you forgot. Read error messages; never just re-run.")


# ---------------------------------------------------------------------------
heading("5. Casting: changing a type on purpose")

print("  int(x)    -> whole number")
show('int("42")', int("42"))
show("int(3.9)", int(3.9))
print("      ^^^ CAREFUL: int() TRUNCATES. It chops the decimal part off.")
show("int(-3.9)", int(-3.9))
print("      ^^^ towards zero, so -3 not -4.")
show("round(3.9)", round(3.9))
print("      ^^^ use round() when you want actual rounding.")

print()
print("  float(x)  -> real number")
show('float("3.5")', float("3.5"))
show("float(7)", float(7))
print("      ^^^ 7 becomes 7.0. The value is the same, the type is not.")

print()
print("  str(x)    -> text")
show("str(42)", str(42))
show("str(3.5)", str(3.5))

print()
print("  bool(x)   -> True/False")
show("bool(0)", bool(0))
show("bool(1)", bool(1))
show('bool("")', bool(""))
show('bool("no")', bool("no"))
print("      ^^^ ANY non-empty string is True, even \"False\". Watch out.")


# ---------------------------------------------------------------------------
heading("6. When casting fails")

for text in ["42", "3.5", "ten", "", "12abc", " 7 "]:
    try:
        value = float(text)
    except ValueError as error:
        print("  float(%-7r) -> ValueError: %s" % (text, error))
    else:
        print("  float(%-7r) -> %r" % (text, value))

print()
print("  Note the last one: float(\" 7 \") works. Python strips spaces for")
print("  you. But float(\"12abc\") does not - it is all or nothing.")
print("  Step 05 shows how to survive these failures.")


# ---------------------------------------------------------------------------
heading("7. int() or float() for YOUR program?")

print("""
  Counting things that cannot be half:  int()
      number of students, lives left, marks out of 10

  Measuring, money, or anything averaged:  float()
      heights, prices, temperatures, test averages

  Your snippet uses float() and that is the right call - the average of
  two whole numbers is very often not whole:
""")
show("(7 + 8) / 2", (7 + 8) / 2)
print("      ^^^ 7.5. An int() version would have thrown the .5 away.")


# ---------------------------------------------------------------------------
heading("8. Naming: rules vs manners")

print("""
  RULES - break these and Python refuses to run:
      letters, digits, underscores only          my_total_2   OK
      cannot start with a digit                  2nd_number   SyntaxError
      cannot be a keyword                        class = 5    SyntaxError
      case matters       total, Total and TOTAL are 3 different variables

  MANNERS - break these and humans refuse to read your code:
      snake_case for variables                   first_number  not FirstNumber
      say what it IS                             average       not a, x, avg2
      never shadow a built-in                    see below
""")

print("  Why shadowing hurts:")
real_sum = sum                       # keep a copy so we can repair it
sum = 10                             # noqa: A001 - deliberate bad example
print("      after `sum = 10`, the built-in sum() is gone:")
try:
    sum([1, 2, 3])
except TypeError as error:
    print("      sum([1, 2, 3]) -> TypeError:", error)
sum = real_sum                       # repair it
print("      repaired:  sum([1, 2, 3]) =", sum([1, 2, 3]))
print()
print("  Names to never use for your own variables:")
print("      list  str  int  float  sum  min  max  input  print  type  id")


# ---------------------------------------------------------------------------
heading("9. Your snippet, renamed")

print("""
  Before - works, but says nothing:

      a = float(input("Enter first number: "))
      b = float(input("Enter second number: "))
      total = a + b
      avg = total / 2

  After - identical behaviour, readable in six months:

      first_number = float(input("Enter first number: "))
      second_number = float(input("Enter second number: "))
      total = first_number + second_number
      average = total / 2

  `a` and `b` are fine for throwaway maths. They are not fine in a program
  someone has to read, and that someone is usually you, later.
""")

print("Next:  python3 03_operators.py")
