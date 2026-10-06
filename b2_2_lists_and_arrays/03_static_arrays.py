"""B2.2.2 - Step 3: making Python behave like a STATIC ARRAY.

Run me:  python3 03_static_arrays.py

Python has no fixed-size array type, but B2.2.1 asks you to compare static and
dynamic structures, and IB pseudocode questions are usually written in terms of
arrays. So you need to be able to write array-style code on purpose.

The rules you impose on yourself:
    1. Decide the SIZE up front and create the array full of placeholders.
    2. Only ever OVERWRITE elements:  arr[i] = value
    3. Never append, insert, pop or remove - those change the size.
    4. Track how many slots are actually USED with a separate counter.
    5. Check bounds yourself before writing.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ===========================================================================
heading("1. Declaring a fixed-size array")

CAPACITY = 5                           # a CONSTANT: capitals, never reassigned
temperatures = [0] * CAPACITY          # 5 slots, all pre-filled with 0

print("temperatures =", temperatures)
print("capacity     =", CAPACITY)
print()
print("IB pseudocode equivalent:   TEMPERATURES = new array[5]")
print("Java equivalent:            int[] temperatures = new int[5];")
print()
print("Pick a placeholder that cannot be confused with real data:")
print("   numbers that can be 0  -> use None, not 0")
print("   text                   -> use None or \"\"")
unset = [None] * 3
print("   unset =", unset)


# ===========================================================================
heading("2. Filling it by index only")

readings = [19, 22, 25, 18, 21]        # the data we want to load
for i in range(CAPACITY):
    temperatures[i] = readings[i]      # OVERWRITE - size never changes
    print("   temperatures[%d] = %-3d -> %s" % (i, readings[i], temperatures))

print()
print("len(temperatures) is still", len(temperatures), "- it never moved.")


# ===========================================================================
heading("3. The counter pattern: a part-full array")

# Real arrays are often not full. You keep a 'count' of used slots, and you
# only ever look at elements 0 .. count-1.
names = [None] * CAPACITY
count = 0                              # number of slots actually in use


def add_name(array, used, capacity, new_name):
    """Add to the first free slot. Returns the new 'used' count.

    This is how you simulate .append() on a fixed array - and it shows you
    exactly why a static structure is inflexible: when it is full, it is full.
    """
    if used >= capacity:
        print("   ARRAY FULL - cannot add", repr(new_name))
        return used                    # refuse, do not grow
    array[used] = new_name
    return used + 1


for candidate in ["Ama", "Ben", "Chloe", "Dev", "Esi", "Femi"]:
    count = add_name(names, count, CAPACITY, candidate)
    print("   add %-7s -> count = %d  %s" % (repr(candidate), count, names))

print()
print("Only read the USED part of the array:")
for i in range(count):                 # NOT range(len(names)) - that shows Nones
    print("   names[%d] = %s" % (i, names[i]))


# ===========================================================================
heading("4. Deleting from a static array: shuffle, do not shrink")

def delete_at(array, used, index):
    """Remove element at `index` by shifting everything after it left by one.

    This is what list.pop(i) does for you internally, and it is why inserting
    or deleting in the middle of an array is O(n) while reading is O(1).
    """
    for i in range(index, used - 1):
        array[i] = array[i + 1]        # each element steps one place left
    array[used - 1] = None             # blank the now-duplicated last slot
    return used - 1


print("before        :", names, "count =", count)
count = delete_at(names, count, 1)     # remove 'Ben'
print("delete index 1:", names, "count =", count)
print()
print("Notice: the array is STILL 5 long. We did not free memory, we just")
print("stopped counting the last slot. That is exactly how static works.")


# ===========================================================================
heading("5. Inserting into a static array: shuffle right")

def insert_at(array, used, capacity, index, value):
    """Make room at `index` by shifting everything from the end rightwards."""
    if used >= capacity:
        print("   ARRAY FULL - cannot insert")
        return used
    for i in range(used, index, -1):   # walk BACKWARDS or you overwrite data
        array[i] = array[i - 1]
    array[index] = value
    return used + 1


print("before        :", names, "count =", count)
count = insert_at(names, count, CAPACITY, 1, "Bea")
print("insert at 1   :", names, "count =", count)
print()
print("The loop runs backwards. Try it forwards on paper and watch every")
print("element turn into a copy of the first one - a classic exam trap.")


# ===========================================================================
heading("6. Bounds checking - do it yourself")

def safe_get(array, used, index):
    """Read an element, refusing out-of-range indices instead of crashing."""
    if index < 0 or index >= used:
        return None                    # or raise, but be consistent
    return array[index]


for test_index in (0, 3, 9, -1):
    print("   safe_get(index=%2d) -> %s" % (test_index,
                                            safe_get(names, count, test_index)))

print()
print("A valid index satisfies   0 <= index <= used - 1.")
print("Writing 'index <= used' instead of '< used' is the off-by-one error.")


# ===========================================================================
heading("7. Side by side: the same job, both structures")

print("STATIC  (fixed 5 slots, counter, refuses a 6th name)")
print("   names   =", names)
print("   count   =", count, "of capacity", CAPACITY)
print("   full?   ", count >= CAPACITY)

print()
print("DYNAMIC (a Python list, grows as needed, no capacity at all)")
dynamic_names = []
for candidate in ["Ama", "Ben", "Chloe", "Dev", "Esi", "Femi", "Gift"]:
    dynamic_names.append(candidate)
print("   names   =", dynamic_names)
print("   len     =", len(dynamic_names), "- all 7 fitted, no refusals")

print()
print("Trade-off to write in an exam:")
print("  static  - predictable memory, fast indexed access, no pointer")
print("            overhead; BUT size fixed at declaration, so it either")
print("            wastes unused slots or overflows.")
print("  dynamic - adapts to however much data arrives at run time; BUT")
print("            uses extra memory for bookkeeping and resizing costs time.")
