"""A1.1 - Step 6: from two numbers to any number of numbers.

Run me:  python3 06_two_to_many.py

Your snippet averages exactly two numbers. The `2` is typed into the code.
This is the most important upgrade in this unit, because getting rid of that
hard-coded 2 is what turns a toy into a program - and it lands you straight
in the lists unit (b2_2_lists_and_arrays) with everything already familiar.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ---------------------------------------------------------------------------
heading("1. The problem with the 2")

print("""
      total = a + b
      avg = total / 2

Now add a third number. Beginners add the obvious line:

      total = a + b + c
      avg = total / 2            <- still 2. Silently, completely WRONG.

It does not crash. It does not warn you. It just prints a wrong answer that
looks plausible, which is the worst kind of bug there is.

The `2` and the `a + b` describe the same fact - how many numbers there are
- in two separate places. Change one, forget the other, and they disagree.

RULE: never store the same fact twice. Count the numbers, do not type the
count in.
""")


# ---------------------------------------------------------------------------
heading("2. Three numbers, done properly")

first, second, third = 10.0, 5.0, 9.0
count = 3
total = first + second + third
print("  total = %r,  count = %d,  average = %r"
      % (total, count, total / count))
print()
print("  Better, but `count = 3` is still a fact typed by hand, and we")
print("  still need a new variable name for every number. At ten numbers")
print("  this approach collapses. We need something that HOLDS numbers.")


# ---------------------------------------------------------------------------
heading("3. The accumulator pattern")

print("""
Before lists, learn the pattern that powers them. Three steps, always:

      total = 0                      1. START with an empty answer
      for value in values:           2. VISIT every item
          total = total + value      3. UPDATE the answer
      print(total)                   4. ...then use it

The variable that builds up the answer is called an ACCUMULATOR. Starting
it at 0 is not arbitrary: 0 is the value that leaves a sum unchanged.
(For a running PRODUCT you would start at 1, for the same reason.)
""")

values = [10.0, 5.0, 9.0, 12.0]
print("  values =", values)
print()
total = 0
print("      total starts at %r" % total)
for value in values:
    total = total + value
    print("      + %-5r -> total is now %r" % (value, total))
print()
print("  After the loop, total = %r" % total)


# ---------------------------------------------------------------------------
heading("4. Now the count comes from the data")

print("  len(values) ASKS the list how long it is:")
print("      len(values) =", len(values))
print()
print("      average = total / len(values) = %r / %d = %r"
      % (total, len(values), total / len(values)))
print()
print("  Nothing is typed by hand any more. Add a fifth number to `values`")
print("  and the average is still right, with zero changes to the code.")
print("  THAT is the difference between a snippet and a program.")

print()
print("  Counting it yourself, without len(), is the same pattern:")
counted = 0
for value in values:
    counted = counted + 1
print("      counted =", counted, "(an accumulator that adds 1 each time)")


# ---------------------------------------------------------------------------
heading("5. The empty-list trap")

print("  What is the average of no numbers?\n")
empty = []
total = 0
for value in empty:
    total = total + value
print("      total      =", total)
print("      len(empty) =", len(empty))
try:
    total / len(empty)
except ZeroDivisionError as error:
    print("      total / len(empty) -> ZeroDivisionError:", error)
print()
print("  It is not a bug in your loop - the average of nothing genuinely")
print("  does not exist. So SAY so, do not divide:")
print()
print("      if len(values) == 0:")
print("          print(\"No numbers entered.\")")
print("      else:")
print("          print(total / len(values))")
print()
print("  Every exam question about an average expects this guard. It is")
print("  usually worth a mark on its own.")


# ---------------------------------------------------------------------------
heading("6. Collecting input into a list")

print("""
Two shapes, depending on whether you know how many numbers to expect.

  (a) a FIXED count - use `for` with range():

      how_many = read_int("How many numbers? ")
      numbers = []
      for index in range(how_many):
          numbers.append(read_float(f"Number {index + 1}: "))

  (b) an UNKNOWN count - loop until a SENTINEL value is typed:

      numbers = []
      while True:
          text = input("Number (or 'done'): ")
          if text == "done":
              break
          numbers.append(float(text))

A SENTINEL is a special value that means "stop" rather than being data.
Pick one that can never be real data: "done" works; 0 or -1 do not, because
0 and -1 might be genuine marks.
""")

print("  range(4) produces:", list(range(4)))
print("  ...which is why `index + 1` is used in the prompt - humans count")
print("  from 1, Python counts from 0. Same off-by-one you met in lists.")


# ---------------------------------------------------------------------------
heading("7. The whole program, generalised")

print('''
      def read_float(prompt):
          while True:
              try:
                  return float(input(prompt))
              except ValueError:
                  print("  Not a number. Try again.")


      how_many = int(read_float("How many numbers? "))

      numbers = []
      for index in range(how_many):
          numbers.append(read_float(f"Number {index + 1}: "))

      if len(numbers) == 0:
          print("No numbers entered.")
      else:
          total = 0
          for value in numbers:
              total = total + value
          print(f"Total:   {total:.2f}")
          print(f"Average: {total / len(numbers):.2f}")
''')

print("  Run it mentally with how_many = 3 and the numbers 10, 5, 9:")
numbers = [10.0, 5.0, 9.0]
total = 0
for index, value in enumerate(numbers):
    total = total + value
    print("      after number %d (%r): total = %r" % (index + 1, value, total))
print("      Total:   %.2f" % total)
print("      Average: %.2f" % (total / len(numbers)))


# ---------------------------------------------------------------------------
heading("8. Where this goes next")

print("""
You have just written the four algorithms the lists unit is built on:

      sum         total = total + value
      count       counted = counted + 1
      average     total / len(values)
      build       numbers.append(value)

Add "largest", "smallest" and "search" and you have every traversal the
exam asks for. They are all the same three-step shape: start, visit, update.

      python3 ../b2_2_lists_and_arrays/02_traversal_patterns.py

Do step 07 first, though - it is the one that makes your code testable.
""")

print("Next:  python3 07_functions.py")
