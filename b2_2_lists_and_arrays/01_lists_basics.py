"""B2.2.2 - Step 1: the 1-D list.

Run me:  python3 01_lists_basics.py

Read each block of code, then read the output it produced. Change the numbers
and run it again - breaking things on purpose is the fastest way to learn.
"""


def heading(text):
    """Print a visible section break."""
    print()
    print(text)
    print("-" * len(text))


# ---------------------------------------------------------------------------
heading("1. Creating a list")

marks = [65, 72, 48, 91, 55]          # a literal list of 5 integers
empty = []                            # a list with nothing in it, length 0
zeros = [0] * 5                       # [0, 0, 0, 0, 0] - handy for arrays
names = ["Ama", "Ben", "Chloe"]       # lists can hold any type
mixed = [1, "two", 3.0, True]         # ...even several types at once

print("marks =", marks)
print("empty =", empty, "with length", len(empty))
print("zeros =", zeros)
print("names =", names)
print("mixed =", mixed, "<- legal in Python, NOT legal in a true array")


# ---------------------------------------------------------------------------
heading("2. Indexing: counting starts at 0")

print("marks        =", marks)
print("marks[0]     =", marks[0], " <- first element")
print("marks[2]     =", marks[2])
print("len(marks)   =", len(marks), " <- how MANY elements")
print("marks[len(marks) - 1] =", marks[len(marks) - 1], " <- last element")
print("marks[-1]    =", marks[-1], " <- Python shortcut for the last one")
print("marks[-2]    =", marks[-2], " <- second from the end")

# Asking for an index that does not exist is an error, not a silent 0.
try:
    print(marks[5])
except IndexError as error:
    print("marks[5] ->  IndexError:", error)
    print("            length is 5, so the LAST valid index is 4.")


# ---------------------------------------------------------------------------
heading("3. Changing an element (size stays the same)")

print("before:", marks)
marks[2] = 50                  # Chloe's resit
print("after marks[2] = 50:", marks)
print("Length is still", len(marks), "- this operation is ARRAY-SAFE.")


# ---------------------------------------------------------------------------
heading("4. Growing and shrinking (dynamic behaviour)")

basket = []
print("start           ", basket, "len =", len(basket))

basket.append("bread")         # add to the END
basket.append("milk")
basket.append("eggs")
print("after 3 appends ", basket, "len =", len(basket))

basket.insert(1, "jam")        # squeeze in at index 1, shift the rest right
print("insert(1, 'jam')", basket)

removed = basket.pop()         # remove and return the LAST item
print("pop()           ", basket, "- removed", repr(removed))

removed = basket.pop(0)        # remove and return item at index 0
print("pop(0)          ", basket, "- removed", repr(removed))

basket.remove("milk")          # remove by VALUE, not by index, first match only
print("remove('milk')  ", basket)

print()
print("None of the four lines above would be possible with a static array.")
print("That is the whole static-vs-dynamic distinction, in code.")


# ---------------------------------------------------------------------------
heading("5. Searching and counting without writing a loop")

temps = [19, 22, 22, 25, 18, 22]
print("temps          =", temps)
print("22 in temps    =", 22 in temps, "   <- membership test, True/False")
print("temps.index(22)=", temps.index(22), "    <- position of the FIRST 22")
print("temps.count(22)=", temps.count(22), "    <- how many 22s")
print("99 in temps    =", 99 in temps)

try:
    temps.index(99)
except ValueError as error:
    print("temps.index(99) ->  ValueError:", error)
    print("                    always test with 'in' before calling .index()")


# ---------------------------------------------------------------------------
heading("6. Slicing: a COPY of part of the list")

letters = ["a", "b", "c", "d", "e", "f"]
print("letters      =", letters)
print("letters[1:4] =", letters[1:4], "<- from 1 UP TO BUT NOT INCLUDING 4")
print("letters[:3]  =", letters[:3], "     <- from the start")
print("letters[3:]  =", letters[3:], "     <- to the end")
print("letters[:]   =", letters[:], " <- a full copy (remember this!)")
print("letters[::2] =", letters[::2], "     <- every 2nd element")
print("letters[::-1]=", letters[::-1], "<- reversed copy")
print()
print("Why 'up to but not including'?  Because then the number of elements")
print("in letters[a:b] is simply b - a.  letters[1:4] -> 4 - 1 = 3 elements.")


# ---------------------------------------------------------------------------
heading("7. Sorting: in place vs a sorted copy")

scores = [7, 3, 9, 1]
print("scores            =", scores)
print("sorted(scores)    =", sorted(scores), "<- NEW list returned")
print("scores is still   =", scores, "    <- original untouched")

scores.sort()
print("after scores.sort() =", scores, "<- original CHANGED in place")
print("note:", repr(scores.sort()), "- .sort() returns None, never assign it!")

scores.sort(reverse=True)
print("sort(reverse=True)  =", scores)


# ---------------------------------------------------------------------------
heading("8. Three ways to walk a list - know all three")

fruit = ["apple", "banana", "cherry"]

print("A) for each element  (cleanest when you only need the value)")
for item in fruit:
    print("     ", item)

print("B) for each index    (use when you need the position, or must WRITE)")
for i in range(len(fruit)):
    print("      index", i, "holds", fruit[i])

print("C) while loop        (closest to IB pseudocode)")
i = 0
while i < len(fruit):
    print("      index", i, "holds", fruit[i])
    i = i + 1

print()
print("The same loop in IB pseudocode:")
print("    loop I from 0 to FRUIT.length - 1")
print("        output FRUIT[I]")
print("    end loop")
