"""B2.2.2 - Worked solutions to exercises.py.

Run me:  python3 solutions.py

This file re-runs the exercise marker using these answers, so you can see all
28 checks pass. Read the comments: they explain WHY each one is shaped the way
it is, which is what earns the method marks.
"""


# ---------------------------------------------------------------------------
# PART A
# ---------------------------------------------------------------------------

def count_elements(values):
    """1. Counter pattern. One increment per element - this is literally what
    len() does, except len() is O(1) because a list stores its own size."""
    count = 0
    for _value in values:
        count = count + 1
    return count


def sum_even(values):
    """2. Accumulator with a condition. `% 2 == 0` is the test for even.
    Starting at 0 is right here, because 0 is the identity for addition and an
    empty list genuinely has total 0."""
    total = 0
    for value in values:
        if value % 2 == 0:
            total = total + value
    return total


def second_largest(values):
    """3. Two running bests at once.

    The subtlety: the loop must start at index 1, because index 0 has already
    been used to seed `largest`. If you start at 0, the first element gets
    counted twice and becomes the "second" largest as well.

    Duplicates of the maximum count as the second largest - that is a design
    decision, and in an exam you would state it in a comment."""
    if len(values) < 2:
        return None
    largest = values[0]
    second = None
    for i in range(1, len(values)):
        value = values[i]
        if value > largest:
            second = largest          # the old champion is demoted
            largest = value
        elif second is None or value > second:
            second = value
    return second


def reversed_copy(values):
    """4. Walk the source backwards, append forwards.

    range(start, stop, step) with a negative step counts down. The stop is -1
    because stop is exclusive and we must still include index 0."""
    result = []
    for i in range(len(values) - 1, -1, -1):
        result.append(values[i])
    return result


def is_sorted(values):
    """5. Compare each neighbouring PAIR.

    There are len - 1 pairs, so the loop runs to len - 2 and compares i with
    i + 1. Returning False at the first failure is more efficient than
    checking every pair - no point continuing once you know."""
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True                        # also handles [] and [x] correctly


def all_positions(values, target):
    """6. Linear search that does NOT stop early, collecting indices.

    You need the index, so this must be an index-based loop, not `for value
    in values`."""
    result = []
    for i in range(len(values)):
        if values[i] == target:
            result.append(i)
    return result


def remove_duplicates(values):
    """7. Build-as-you-go, using the result itself as the memory of what has
    been seen. `not in result` is a hidden linear search, so this is O(n^2)
    overall - worth saying out loud if asked about efficiency."""
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def swap(values, i, j):
    """8. In-place swap with bounds checking.

    The classic three-line version with a temporary variable is:
        temp = values[i]
        values[i] = values[j]
        values[j] = temp
    Python's tuple assignment does the same thing in one line. Both are fine;
    know the three-line version because that is what pseudocode needs."""
    if i < 0 or j < 0 or i >= len(values) or j >= len(values):
        return                         # refuse silently, length unchanged
    values[i], values[j] = values[j], values[i]


def rotate_left(values):
    """9. Every element moves down one index; element 0 wraps to the end.

    Guarding the empty list first avoids values[0] raising IndexError."""
    if len(values) == 0:
        return []
    result = []
    for i in range(1, len(values)):
        result.append(values[i])
    result.append(values[0])
    return result


# ---------------------------------------------------------------------------
# PART B
# ---------------------------------------------------------------------------

def row_totals(grid):
    """10. Nested loop. The accumulator is reset INSIDE the outer loop, once
    per row - putting it outside is the commonest error here."""
    totals = []
    for r in range(len(grid)):
        row_total = 0
        for c in range(len(grid[r])):
            row_total = row_total + grid[r][c]
        totals.append(row_total)
    return totals


def column_maximum(grid, col):
    """11. One loop only: the column index is fixed, the row index varies.

    Two guards: an empty grid has no grid[0], and a column index past the end
    of a row would raise IndexError."""
    if len(grid) == 0 or col < 0 or col >= len(grid[0]):
        return None
    largest = grid[0][col]
    for r in range(1, len(grid)):
        if grid[r][col] > largest:
            largest = grid[r][col]
    return largest


def count_in_grid(grid, target):
    """12. The counter lives outside BOTH loops, so it accumulates across the
    whole grid rather than resetting each row."""
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == target:
                count = count + 1
    return count


# ===========================================================================
if __name__ == "__main__":
    import exercises

    # Inject these answers into the exercise module and run its marker.
    for _name in ("count_elements", "sum_even", "second_largest",
                  "reversed_copy", "is_sorted", "all_positions",
                  "remove_duplicates", "swap", "rotate_left",
                  "row_totals", "column_maximum", "count_in_grid"):
        setattr(exercises, _name, globals()[_name])

    print("B2.2.2 solutions - running the same marker as exercises.py")
    exercises._run()
