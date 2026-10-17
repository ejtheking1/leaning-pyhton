"""A1.1 - Step 4: getting data in and out properly.

Run me:  python3 04_input_output.py

Your snippet printed `The average is 7.5`. Fine. But type 10 and 3 into it
and the output becomes

    The average is 6.666666666666667

which is not what anyone wants to read. This file fixes the output, and
explains the one rule about input() you must never forget.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ---------------------------------------------------------------------------
heading("1. The one rule about input()")

print("""
    input() ALWAYS returns a string.

Always. Even if the user types 7. Even if they type 3.5. Even if they type
nothing at all (you get the empty string ""). There is no exception.

    name = input("Your name: ")          # "Ama"      - already a str, fine
    age  = int(input("Your age: "))      # "17" -> 17 - needs converting
    mark = float(input("Your mark: "))   # "6.5" -> 6.5
""")

print("  And input() takes an optional prompt, which it prints WITHOUT a")
print("  newline, so the cursor sits on the same line:")
print()
print('      input("Enter first number: ")')
print("      Enter first number: _            <- cursor waits here")
print()
print("  Always end a prompt with a space. `input(\"Name:\")` makes the user")
print("  type right up against the colon, and it looks broken.")


# ---------------------------------------------------------------------------
heading("2. Three ways to print a result")

average = 20 / 3

print("  (a) comma-separated - what your snippet does")
print("      print(\"The average is\", average)")
print("      output >>> ", end="")
print("The average is", average)
print("      Easy, but you get 16 decimal places and no say in it.")

print()
print("  (b) concatenation - needs str() and gets ugly fast")
print("      print(\"The average is \" + str(average))")
print("      output >>> " + "The average is " + str(average))
print("      Forget the str() and you get a TypeError:")
try:
    "The average is " + average                # noqa: B018 - deliberate
except TypeError as error:
    print("      TypeError:", error)

print()
print("  (c) f-string - use this one")
print("      print(f\"The average is {average:.2f}\")")
print(f"      output >>> The average is {average:.2f}")
print("      Readable, and you control the formatting.")


# ---------------------------------------------------------------------------
heading("3. How f-strings work")

print("""
Put an `f` immediately before the opening quote. Then anything inside
{curly braces} is evaluated as Python and dropped into the text.
""")

name = "Ama"
mark = 17.4567
total = 20

print('  name, mark, total = "Ama", 17.4567, 20')
print()
print('  f"{name}"                   ->', f"{name}")
print('  f"{name} scored {mark}"     ->', f"{name} scored {mark}")
print('  f"{mark:.1f}"               ->', f"{mark:.1f}")
print('  f"{mark / total * 100:.0f}%" ->', f"{mark / total * 100:.0f}%")
print("      ^^^ you can put a whole calculation inside the braces")
print('  f"{name=}"                  ->', f"{name=}")
print("      ^^^ the `=` form prints the name AND the value. Great for")
print("          debugging - it is a trace table you get for free.")


# ---------------------------------------------------------------------------
heading("4. Format specifiers worth memorising")

value = 1234.5678

rows = [
    ("{v}", f"{value}", "raw, all the digits"),
    ("{v:.2f}", f"{value:.2f}", "2 decimal places"),
    ("{v:.0f}", f"{value:.0f}", "no decimals (rounds)"),
    ("{v:10.2f}", f"{value:10.2f}", "2 d.p. in 10 columns, right-aligned"),
    ("{v:<10.2f}", f"{value:<10.2f}", "left-aligned"),
    ("{v:^10.2f}", f"{value:^10.2f}", "centred"),
    ("{v:,.2f}", f"{value:,.2f}", "thousands separators"),
    ("{v:+.2f}", f"{value:+.2f}", "always show the sign"),
    ("{v:.3e}", f"{value:.3e}", "scientific notation"),
]
print("  with value = %r\n" % value)
for spec, result, note in rows:
    print("      %-11s -> %-14r %s" % (spec, result, note))

print()
print("  Right-aligning numbers in a fixed width is how you make a table")
print("  line up. Compare:")
print()
for item, price in [("Bread", 1.2), ("Milk", 0.85), ("Chocolate", 12.5)]:
    print("      %-12s %s" % (item, price))
print("      ^^^ ragged. Now with a specifier:")
print()
for item, price in [("Bread", 1.2), ("Milk", 0.85), ("Chocolate", 12.5)]:
    print(f"      {item:<12}{price:>8.2f}")


# ---------------------------------------------------------------------------
heading("5. round() vs formatting - they are not the same")

ugly = 20 / 3
print("  value =", ugly)
print()
print("  round(value, 2)     ->", round(ugly, 2), " a NEW NUMBER, rounded")
print('  f"{value:.2f}"      ->', repr(f"{ugly:.2f}"), "   a STRING, for display")
print()
print("  Use round() when a later calculation needs the rounded value.")
print("  Use a format spec when you only want it to LOOK right on screen.")
print()
print("  Rounding early loses accuracy. Rounding for display never does:")
quarter = 1 / 3
print("      round(1/3, 2) * 3     =", round(quarter, 2) * 3, " <- drifted")
print("      (1/3) * 3             =", quarter * 3, " <- kept full precision")
print("  Rule: calculate at full precision, round only at the final print.")


# ---------------------------------------------------------------------------
heading("6. print()'s own options")

print("  By default print() puts a space between arguments and a newline")
print("  at the end. Both are changeable:")
print()
print("      print('a', 'b', 'c')            ->", end=" ")
print('a', 'b', 'c')
print("      print('a', 'b', sep='-')        ->", end=" ")
print('a', 'b', sep='-')
print("      print('a', 'b', sep='')         ->", end=" ")
print('a', 'b', sep='')
print("      print('no newline', end='')     -> ", end="")
print('no newline', end='')
print("  <- next print continued on the same line")
print()
print("  `end=\"\"` is how you build a line in pieces, e.g. a progress bar:")
print("      ", end="")
for i in range(20):
    print("#", end="")
print(" done")


# ---------------------------------------------------------------------------
heading("7. Your snippet, with proper output")

print("""
  Before:

      print("The average is", avg)
      >>> The average is 6.666666666666667

  After:

      print(f"The average is {average:.2f}")
      >>> The average is 6.67

  Or, if you want to show the working - which is what a real program for a
  teacher would do:

      print(f"You entered {first} and {second}.")
      print(f"Total:   {total:>8.2f}")
      print(f"Average: {average:>8.2f}")
""")

first, second = 10.0, 3.0
total = first + second
average = total / 2
print("  Live:")
print(f"      You entered {first} and {second}.")
print(f"      Total:   {total:>8.2f}")
print(f"      Average: {average:>8.2f}")

print()
print("Next:  python3 05_safe_input.py")
