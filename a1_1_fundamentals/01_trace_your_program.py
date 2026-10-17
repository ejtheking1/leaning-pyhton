"""A1.1 - Step 1: your five lines, traced value by value.

Run me:  python3 01_trace_your_program.py

This is the exact program your teacher gave you. Nothing is changed. We just
run it in slow motion and print what is in memory after every single line, so
you can see WHY it works instead of hoping that it does.

Nothing here asks you to type anything - we feed it fake input so the trace
is the same every time. The real, interactive version is at the bottom.
"""


def heading(text):
    """Print a visible section break."""
    print()
    print(text)
    print("-" * len(text))


def state(**names):
    """Print the current value and type of each name passed in."""
    for name, value in names.items():
        print("      %-8s = %-8r (%s)" % (name, value, type(value).__name__))


# ---------------------------------------------------------------------------
heading("The program")

print('''
    1  a = float(input("Enter first number: "))
    2  b = float(input("Enter second number: "))
    3
    4  total = a + b
    5  avg = total / 2
    6
    7  print("The average is", avg)
''')

print("Five lines that do work, plus two blank ones. Let us walk them.")


# ---------------------------------------------------------------------------
heading("Line 1, in three stages")

# We pretend the user typed 10 and then 5.
typed_first = "10"
typed_second = "5"

print("The user types: 10  then  5")
print()
print("Line 1 is three operations nested inside each other. Python always")
print("finishes the INNERMOST brackets first, so read it inside out:")
print()

print('  (1) input("Enter first number: ")')
raw_a = typed_first                      # what input() would have returned
print("      prints the prompt, waits for Enter, hands back what was typed")
state(raw_a=raw_a)
print('      ^^^ note the quotes. It is the TEXT "10", not the number 10.')

print()
print("  (2) float(raw_a)")
a = float(raw_a)
print("      converts that text into a real number")
state(a=a)
print("      ^^^ no quotes now, and 10.0 not 10 - floats always show a point.")

print()
print("  (3) a = ...")
print("      the name `a` is now pointed at that value.")
state(a=a)

print()
print("If you skipped stage 2, `a` would be the string \"10\" and your whole")
print("program would quietly do the wrong thing. Watch:")
print("      %-12s = %-6r <- JOINED, because they are text"
      % ('"10" + "5"', "10" + "5"))
print("      %-12s = %-6r <- ADDED, because they are numbers"
      % ("10.0 + 5.0", 10.0 + 5.0))
print("Same `+` symbol. The TYPES decide which job it does.")


# ---------------------------------------------------------------------------
heading("Line 2: the same thing again")

b = float(typed_second)
state(a=a, b=b)
print()
print("Two names, two values. Both floats. Nothing clever - just a repeat.")


# ---------------------------------------------------------------------------
heading("Line 4: total = a + b")

print("The right-hand side is worked out FIRST:")
print("      a + b   ->  %r + %r  ->  %r" % (a, b, a + b))
print("THEN the name `total` is pointed at the answer.")
total = a + b
state(a=a, b=b, total=total)
print()
print("`=` does not mean 'equals'. It means 'store this here'. It always")
print("runs right-to-left. That is why `total = total + 1` makes sense.")


# ---------------------------------------------------------------------------
heading("Line 5: avg = total / 2")

print("      total / 2  ->  %r / 2  ->  %r" % (total, total / 2))
avg = total / 2
state(a=a, b=b, total=total, avg=avg)
print()
print("`/` is TRUE division and always gives a float, even when it divides")
print("exactly. Check:")
print("      %-8s = %-5r <- a float, not 3" % ("6 / 2", 6 / 2))
print("      %-8s = %-5r <- // is FLOOR division, gives an int"
      % ("6 // 2", 6 // 2))


# ---------------------------------------------------------------------------
heading("Line 7: print(\"The average is\", avg)")

print("print() takes several arguments and puts a SPACE between each one.")
print("That is where the space after 'is' comes from - you never typed it.")
print()
print("    output >>> ", end="")
print("The average is", avg)


# ---------------------------------------------------------------------------
heading("The trace table (learn to draw this)")

print("""
    | Line | a    | b   | total | avg | Output                |
    |------|------|-----|-------|-----|-----------------------|
    | 1    | 10.0 | -   | -     | -   | Enter first number:   |
    | 2    | 10.0 | 5.0 | -     | -   | Enter second number:  |
    | 4    | 10.0 | 5.0 | 15.0  | -   |                       |
    | 5    | 10.0 | 5.0 | 15.0  | 7.5 |                       |
    | 7    | 10.0 | 5.0 | 15.0  | 7.5 | The average is 7.5    |

Rules: one row per line that actually runs, a dash for 'does not exist yet',
and copy unchanged values down. Examiners love these, and more importantly
they stop you GUESSING what code does.
""")


# ---------------------------------------------------------------------------
heading("Now break it on purpose")

print("Three experiments. Predict the answer, then check it below.\n")

print("  A)  what if you forget float() and type 10 and 5?")
print("      ", repr("10" + "5"), "  - concatenation, so 'the average' of 105/2")
print()

print("  B)  what if you use int() and type 2.5?")
try:
    int("2.5")
except ValueError as error:
    print("       int(\"2.5\") -> ValueError:", error)
    print("       int() parses whole numbers only. float(\"2.5\") is fine:",
          repr(float("2.5")))
print()

print("  C)  what if the user types 'ten'?")
try:
    float("ten")
except ValueError as error:
    print("       float(\"ten\") -> ValueError:", error)
    print("       Your program CRASHES here. Step 05 fixes that.")


# ---------------------------------------------------------------------------
heading("The real thing")

print("""
Everything above used fake input so the trace never changes. To run the
genuine interactive version, uncomment the last three lines of this file
(delete the leading # on each) and run it again:
""")

# first = float(input("Enter first number: "))
# second = float(input("Enter second number: "))
# print("The average is", (first + second) / 2)

print("    first = float(input(\"Enter first number: \"))")
print("    second = float(input(\"Enter second number: \"))")
print("    print(\"The average is\", (first + second) / 2)")
print()
print("Notice the brackets around (first + second). Without them you get")
print("first + second/2, which is a DIFFERENT and WRONG answer. Step 03.")
print()
print("Next:  python3 02_variables_and_types.py")
