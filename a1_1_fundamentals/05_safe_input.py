"""A1.1 - Step 5: input that cannot kill your program.

Run me:  python3 05_safe_input.py

Give your snippet to a friend and ask them to test it. They will type "ten",
or "", or "3,5" with a comma, and your program will die with a red traceback.
A program that crashes on bad input is not finished.

This file builds up a `read_float()` function you can paste into every
program you write from now on.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ---------------------------------------------------------------------------
heading("1. What actually goes wrong")

print("  float(\"ten\") raises an exception. An exception that nobody")
print("  catches stops the program dead:\n")

print("      Traceback (most recent call last):")
print('        File "average.py", line 1, in <module>')
print('          a = float(input("Enter first number: "))')
print("      ValueError: could not convert string to float: 'ten'\n")

print("  The user sees that. They have no idea what it means. The rest of")
print("  your program never runs.")


# ---------------------------------------------------------------------------
heading("2. try / except: catching the exception")

print("""
      try:
          value = float(text)        # the risky line goes here
      except ValueError:
          print("That is not a number.")

Read it as: "TRY this; if it raises a ValueError, run the except block
INSTEAD of crashing."
""")

for text in ["10", "3.5", "ten", "", "3,5"]:
    try:
        value = float(text)
    except ValueError:
        print("      %-7r -> rejected" % text)
    else:
        print("      %-7r -> accepted as %r" % (text, value))

print()
print("  Note %r: a comma is the decimal separator in much of the world,"
      % "3,5")
print("  but Python insists on a dot. Worth saying so in your error message.")


# ---------------------------------------------------------------------------
heading("3. The full shape: try / except / else")

print("""
      try:
          risky_thing()
      except SomeError:
          # ran only if that error happened
      else:
          # ran only if NOTHING went wrong
      finally:
          # ran either way, always

Catch the specific error you expect. A bare `except:` swallows EVERYTHING,
including your own typos and the user pressing Ctrl+C, and turns a clear
bug into a mystery. Name the error.
""")

print("  Errors you will meet in this unit:")
print("      ValueError       float(\"ten\")       - right type, bad content")
print("      TypeError        \"42\" + 7           - wrong type entirely")
print("      ZeroDivisionError  1 / 0            - the maths is impossible")
print("      IndexError       [1, 2][5]          - no such position")
print("      NameError        print(totl)        - misspelled a name")


# ---------------------------------------------------------------------------
heading("4. Keep asking until they get it right")

print("""
One try/except tells the user they were wrong but gives up. A LOOP keeps
asking. This is the standard pattern, and it is worth knowing by heart:

      def read_float(prompt):
          \"\"\"Ask until the user types a valid number. Return it as a float.\"\"\"
          while True:
              text = input(prompt)
              try:
                  return float(text)         # valid -> leave the loop AND
              except ValueError:             #          the function, at once
                  print(f"  '{text}' is not a number. Use digits, e.g. 3.5")

`while True:` loops forever. The `return` inside the `try` is the only way
out, and it is only reachable when float() did not raise. So the loop can
only end with a valid number in hand.
""")


def read_float(prompt):
    """Ask until the user types a valid number. Return it as a float."""
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("  '%s' is not a number. Use digits, e.g. 3.5" % text)


# We simulate it here so this file runs without you typing anything.
def _simulate(reader, typed):
    """Run `reader` with `typed` standing in for what the user types."""
    import builtins
    queue = list(typed)
    original = builtins.input

    def fake_input(prompt=""):
        entry = queue.pop(0)
        print("%s%s" % (prompt, entry))
        return entry

    builtins.input = fake_input
    try:
        return reader()
    finally:
        builtins.input = original


print("  Simulated run - the user fumbles twice, then succeeds:\n")
result = _simulate(lambda: read_float("  Enter first number: "),
                   ["ten", "", "10"])
print("\n  read_float returned %r (%s)" % (result, type(result).__name__))
print("  Two bad attempts, no crash, and a usable float at the end.")


# ---------------------------------------------------------------------------
heading("5. Validation: valid type is not the same as sensible value")

print("""
float("-5") succeeds. But "-5" is nonsense for a test mark, an age, or a
price. Type-checking and RANGE-checking are two different jobs:

      def read_float_in_range(prompt, lowest, highest):
          while True:
              value = read_float(prompt)              # type is now safe
              if lowest <= value <= highest:          # is it sensible?
                  return value
              print(f"  Enter a number from {lowest} to {highest}.")

Note `lowest <= value <= highest`. Python lets you chain comparisons just
like maths does - no need for `and`.
""")


def read_float_in_range(prompt, lowest, highest):
    """Ask until the user gives a number between lowest and highest."""
    while True:
        value = read_float(prompt)
        if lowest <= value <= highest:
            return value
        print("  Enter a number from %s to %s." % (lowest, highest))


print("  Simulated run asking for a mark out of 100:\n")
mark = _simulate(lambda: read_float_in_range("  Mark (0-100): ", 0, 100),
                 ["abc", "150", "-4", "72"])
print("\n  Accepted %r. It rejected text, too big, and negative." % mark)

print()
print("  The three questions to ask about any input:")
print("      1. is it the right TYPE?        -> try/except")
print("      2. is it in the right RANGE?    -> if lowest <= value <= highest")
print("      3. is it PRESENT at all?        -> if text == \"\"")


# ---------------------------------------------------------------------------
heading("6. The same idea for whole numbers")

print("""
      def read_int(prompt):
          while True:
              text = input(prompt)
              try:
                  return int(text)
              except ValueError:
                  print(f"  '{text}' is not a whole number.")

Careful: int("3.5") FAILS, because 3.5 is not a whole number literal. If
you want "accept 3.5, use 3", convert in two steps: int(float(text)).
""")

for text in ["7", "3.5", "-2"]:
    try:
        direct = int(text)
    except ValueError:
        direct = "ValueError"
    print("      %-6r  int(text) -> %-12s  int(float(text)) -> %r"
          % (text, direct, int(float(text))))


# ---------------------------------------------------------------------------
heading("7. Your snippet, now unkillable")

print('''
      def read_float(prompt):
          """Ask until the user types a valid number."""
          while True:
              text = input(prompt)
              try:
                  return float(text)
              except ValueError:
                  print(f"  '{text}' is not a number. Try again.")


      first = read_float("Enter first number: ")
      second = read_float("Enter second number: ")
      average = (first + second) / 2
      print(f"The average is {average:.2f}")

Four lines of program, one reusable helper above it. The helper gets written
once and pasted into everything you build after this. That is what a
function is FOR, which is step 07.
''')

print("Next:  python3 06_two_to_many.py")
