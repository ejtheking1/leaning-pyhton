"""A1.1 - Step 7: functions, and why your snippet cannot be tested.

Run me:  python3 07_functions.py

This is the step that changes how you write code. Everything before it was
detail; this is structure.

Your five-line snippet mixes three different jobs into one lump:

      get the data  ->  work out the answer  ->  show the answer

So the only way to test it is to run it and type numbers in yourself, every
single time, by hand. Pull the middle job out into a function and a computer
can check it for you in microseconds. That is how exercises.py marks you.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ---------------------------------------------------------------------------
heading("1. The anatomy of a function")

print('''
      def average(values):                       <- def, name, parameters, colon
          """Return the mean of a list."""       <- docstring: what it does
          total = 0                              |
          for value in values:                   |  the BODY, indented
              total = total + value              |
          return total / len(values)             <- hands the answer back


      result = average([10, 5, 9])               <- a CALL, with an ARGUMENT

  Vocabulary the exam uses precisely, so get it right:

      parameter   the name in the definition      `values`
      argument    the actual value you pass in    `[10, 5, 9]`
      return      sends a value back to the caller
      call        running the function
      scope       where a name is visible
''')


# ---------------------------------------------------------------------------
heading("2. return is not print")

def average_printed(values):
    """Print the mean. Returns nothing useful."""
    total = 0
    for value in values:
        total = total + value
    print(total / len(values))


def average(values):
    """Return the mean of a non-empty list of numbers."""
    total = 0
    for value in values:
        total = total + value
    return total / len(values)


print("  average_printed([10, 5, 9]) runs and shows: ", end="")
captured = average_printed([10, 5, 9])
print("  ...but its value is %r" % captured)
print("      ^^^ None. A function with no `return` gives back None.")
print("      You cannot do maths with it, store it, or test it.")
print()
print("  average([10, 5, 9]) returns %r - a real value." % average([10, 5, 9]))
print("      Which means you can keep using it:")
print("      average([10, 5, 9]) * 2 =", average([10, 5, 9]) * 2)
print()
print("  RULE: functions that CALCULATE should return, not print.")
print("  Let the caller decide whether to print, store or re-use the answer.")
print("  This single rule is most of what 'good structure' means.")


# ---------------------------------------------------------------------------
heading("3. Separating the three jobs")

print('''
      INPUT        read_float()      talks to the user
      PROCESS      average()         pure maths, no input, no print
      OUTPUT       the print line    talks to the user

The middle one is the valuable part. It has no idea where its numbers came
from - a keyboard, a file, a test - and no opinion about what happens to
its answer. That independence is exactly what makes it testable.
''')

print("  Testing average() takes no typing at all:\n")
checks = [
    ([10, 5, 9], 8.0),
    ([4], 4.0),
    ([1, 2], 1.5),
    ([-2, 2], 0.0),
]
for values, expected in checks:
    got = average(values)
    verdict = "PASS" if abs(got - expected) < 1e-9 else "FAIL"
    print("      %-14s -> %-6r expected %-6r  %s"
          % (values, got, expected, verdict))

print()
print("  Four tests, instantly, repeatable forever. Try that with a program")
print("  that stops to wait for input in the middle.")


# ---------------------------------------------------------------------------
heading("4. Scope: names live inside the function")

def demonstrate_scope():
    """Show that a local name does not leak out."""
    inside = "I only exist in here"
    return inside


returned = demonstrate_scope()
print("  The function returned:", repr(returned))
try:
    print(inside)                              # noqa: F821 - deliberate
except NameError as error:
    print("  Asking for `inside` outside the function -> NameError:", error)

print()
print("  `inside` is LOCAL to the function. It is created on each call and")
print("  destroyed when the function returns. That is a feature: it means")
print("  a function cannot accidentally wreck a variable somewhere else.")

counter = 10


def tries_to_change_it(counter):
    """Reassigning a parameter does not touch the caller's variable."""
    counter = 999
    return counter


print()
print("  Before the call, the outer counter =", counter)
print("  The function returned", tries_to_change_it(counter))
print("  After the call, the outer counter is STILL", counter)
print("      ^^^ a parameter is a fresh local name, not a link back.")
print("      (Lists behave differently - see 05_pitfalls.py in the lists")
print("       unit for aliasing, which is the exception to this.)")


# ---------------------------------------------------------------------------
heading("5. Default values and multiple returns")

def describe(values, decimals=2):
    """Return (total, average) for `values`, rounded to `decimals`."""
    if len(values) == 0:
        return 0.0, None                       # no average exists
    total = 0
    for value in values:
        total = total + value
    return round(total, decimals), round(total / len(values), decimals)


print("  def describe(values, decimals=2):")
print("      `decimals=2` is a DEFAULT. Callers may leave it out.\n")
print("      describe([10, 5, 9])        ->", describe([10, 5, 9]))
print("      describe([10, 5, 9], 4)     ->", describe([10, 5, 9], 4))
print("      describe([1, 2], decimals=0)->", describe([1, 2], decimals=0))
print("      describe([])                ->", describe([]))
print()
print("  `return a, b` hands back a tuple, which you can unpack:")
total, mean = describe([10, 5, 9])
print("      total, mean = describe([10, 5, 9])")
print("      total = %r,  mean = %r" % (total, mean))
print()
print("  And notice describe([]) returns None for the average rather than")
print("  crashing. Decide what your function does with bad input, and")
print("  write it in the docstring. That decision IS part of the design.")


# ---------------------------------------------------------------------------
heading("6. `if __name__ == \"__main__\":`")

print('''
      def average(values):
          ...

      if __name__ == "__main__":
          numbers = read_numbers()
          print(f"Average: {average(numbers):.2f}")

The guarded block runs only when you execute THIS file directly. If another
file imports yours to borrow `average`, the block is skipped - so importing
your code does not suddenly start asking the importer's user for numbers.

Every file in this unit uses it. Now you know why.
''')


# ---------------------------------------------------------------------------
heading("7. The finished program")

print('''
      """Average any number of values the user types in."""


      def read_float(prompt):
          """Ask until the user types a valid number."""
          while True:
              text = input(prompt)
              try:
                  return float(text)
              except ValueError:
                  print(f"  '{text}' is not a number. Try again.")


      def read_numbers(sentinel="done"):
          """Collect numbers until the user types `sentinel`."""
          numbers = []
          while True:
              text = input(f"Number {len(numbers) + 1} (or '{sentinel}'): ")
              if text == sentinel:
                  return numbers
              try:
                  numbers.append(float(text))
              except ValueError:
                  print(f"  '{text}' is not a number. Try again.")


      def average(values):
          """Return the mean of `values`, or None if it is empty."""
          if len(values) == 0:
              return None
          total = 0
          for value in values:
              total = total + value
          return total / len(values)


      if __name__ == "__main__":
          numbers = read_numbers()
          mean = average(numbers)
          if mean is None:
              print("No numbers entered, so there is no average.")
          else:
              print(f"Count:   {len(numbers)}")
              print(f"Average: {mean:.2f}")
''')

print("""  Compare it with where you started:

      a = float(input("Enter first number: "))
      b = float(input("Enter second number: "))
      total = a + b
      avg = total / 2
      print("The average is", avg)

  Yours handles 2 numbers, crashes on bad input, and can only be checked by
  hand. The version above handles 0 or 2 or 200, survives anything typed at
  it, says something sensible when there is no answer, and its `average` can
  be tested without a human in the room.

  Same idea. The difference is entirely structure - which is the actual
  subject you are being taught.
""")

print("Next:  python3 08_pitfalls.py  then  python3 exercises.py")
