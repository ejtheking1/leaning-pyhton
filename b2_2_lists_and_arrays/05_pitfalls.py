"""B2.2.2 - Step 5: the six mistakes that cost marks.

Run me:  python3 05_pitfalls.py

Each section shows the WRONG code, what it actually does, and the fix.
"""


def heading(text):
    print()
    print("=" * 70)
    print(text)
    print("=" * 70)


# ===========================================================================
heading("PITFALL 1 - Off-by-one: len() is not the last index")

marks = [65, 72, 48]

print("marks =", marks, " len =", len(marks), " last valid index = 2")
print()
print("WRONG:  for i in range(len(marks) + 1)   -> IndexError")
try:
    for i in range(len(marks) + 1):
        print("   marks[%d] = %d" % (i, marks[i]))
except IndexError as error:
    print("   IndexError:", error)

print()
print("RIGHT:  for i in range(len(marks))      -> 0, 1, 2")
for i in range(len(marks)):
    print("   marks[%d] = %d" % (i, marks[i]))

print()
print("range(n) gives 0 .. n-1 and never includes n. That is exactly the set")
print("of valid indices, which is why range(len(x)) is always correct.")


# ===========================================================================
heading("PITFALL 2 - Aliasing: two names, one list")

original = [1, 2, 3]
alias = original                    # NOT a copy - the same object!
alias.append(4)

print("original =", original, "   <- we never touched 'original'...")
print("alias    =", alias)
print("same object?", original is alias)
print()
print("A variable holds a REFERENCE to the list, not the list itself.")
print("'alias = original' copies the arrow, not the box.")
print()
print("FIX - make a real copy, any of these three:")
a = original[:]                     # slice of everything
b = list(original)                  # constructor
c = original.copy()                 # explicit method
a.append(99)
print("   original =", original, "<- unchanged")
print("   copy a   =", a)
print("   same object?", original is a)


# ===========================================================================
heading("PITFALL 3 - Shallow copy of a 2-D array")

grid = [[1, 2], [3, 4]]
shallow = grid[:]                   # copies the OUTER list only
shallow[0][0] = 99                  # reaches through into the shared inner row

print("grid    =", grid, "   <- changed anyway!")
print("shallow =", shallow)
print()
print("grid[:] copied the two arrows, but both still point at the same two")
print("inner lists. For nested structures you need a DEEP copy:")

grid = [[1, 2], [3, 4]]
deep = [row[:] for row in grid]     # copy each row as well
deep[0][0] = 99
print("   grid =", grid, "<- safe")
print("   deep =", deep)
print()
print("(copy.deepcopy() does this for any depth, but write it by hand for")
print("a 2-D array so you can show the examiner you understand why.)")


# ===========================================================================
heading("PITFALL 4 - Modifying a list while looping over it")

numbers = [2, 4, 6, 8]
print("goal: remove every even number from", numbers, "-> should end up []")
print()
print("WRONG - removing while iterating makes the loop SKIP elements:")
wrong = [2, 4, 6, 8]
for value in wrong:
    if value % 2 == 0:
        wrong.remove(value)
print("   result:", wrong, "<- 4 and 8 survived!")
print("   why: the loop keeps an internal counter. It removes index 0, so")
print("        everything shifts left, then the counter moves to 1 - which")
print("        now holds what used to be at index 2. Half the list is skipped.")

print()
print("RIGHT - build a new list instead (safest, and clearest to read):")
right = []
for value in numbers:
    if value % 2 != 0:
        right.append(value)
print("   result:", right)

print()
print("ALSO RIGHT - loop over a COPY, delete from the original:")
other = [2, 4, 6, 8]
for value in other[:]:              # note the [:]
    if value % 2 == 0:
        other.remove(value)
print("   result:", other)

print()
print("ALSO RIGHT - walk backwards, so removals cannot disturb what is left:")
backwards = [2, 4, 6, 8]
for i in range(len(backwards) - 1, -1, -1):
    if backwards[i] % 2 == 0:
        backwards.pop(i)
print("   result:", backwards)


# ===========================================================================
heading("PITFALL 5 - .sort() returns None")

print("WRONG:  values = values.sort()")
broken = [3, 1, 2]
broken = broken.sort()
print("   broken is now", broken, "- the list is GONE")

print()
print("RIGHT, two options depending on what you want:")
in_place = [3, 1, 2]
in_place.sort()                     # mutates, returns None
print("   in_place.sort()  ->", in_place)
new_copy = sorted([3, 1, 2])        # returns a new list
print("   sorted(original) ->", new_copy)
print()
print("General Python rule: methods that MUTATE return None")
print("(.sort, .reverse, .append, .insert). Functions that return a new")
print("object leave the original alone (sorted, reversed, slicing).")


# ===========================================================================
heading("PITFALL 6 - Initialising 'largest' to zero")

temperatures = [-4, -11, -7, -2]
print("temperatures =", temperatures)

wrong_largest = 0
for t in temperatures:
    if t > wrong_largest:
        wrong_largest = t
print("WRONG (started at 0)      ->", wrong_largest, "- not even in the list!")

right_largest = temperatures[0]
for t in temperatures:
    if t > right_largest:
        right_largest = t
print("RIGHT (started at [0])    ->", right_largest)
print()
print("Always seed a running maximum or minimum with the FIRST ELEMENT, and")
print("handle the empty-list case separately.")


# ===========================================================================
heading("CHECKLIST before you hand in any list/array code")

for line in [
    "range(len(x)) - never len(x) + 1, never len(x) - 1 as the stop",
    "a running max/min starts at element 0, not at 0",
    "empty list handled: len(x) == 0 checked before dividing or indexing",
    "a search that finds nothing returns -1, and the caller checks for it",
    "copies made with [:] when the original must survive; rows copied too",
    "nothing added to or removed from a list while a loop is walking it",
    ".sort() called as a statement, never assigned",
    "2-D access is [row][col], in that order, everywhere",
]:
    print("  [ ]", line)
