"""B2.2.2 - Practice. 12 exercises with a built-in marker.

Run me:  python3 exercises.py

Replace each `raise NotImplementedError` with your own code, then run the file
again. It will tell you which ones pass. Rules of the game:

  * Use explicit loops. No sum(), max(), min(), sorted(), set(), reversed(),
    [::-1] or list comprehensions - the point is to be able to write the
    algorithm, which is what the exam asks for.
  * Handle the empty list wherever it makes sense.
  * Worked answers are in solutions.py. Try first, then compare.
"""


# ---------------------------------------------------------------------------
# PART A - one-dimensional lists
# ---------------------------------------------------------------------------

def count_elements(values):
    """1. Return how many elements are in `values` - WITHOUT using len().

    count_elements([4, 5, 6]) -> 3
    count_elements([])        -> 0
    Hint: a counter plus `for value in values`.
    """
    raise NotImplementedError


def sum_even(values):
    """2. Return the total of only the EVEN numbers in `values`.

    sum_even([1, 2, 3, 4]) -> 6
    sum_even([1, 3])       -> 0
    Hint: accumulator + `if value % 2 == 0`.
    """
    raise NotImplementedError


def second_largest(values):
    """3. Return the second largest value. Return None if fewer than 2 items.

    second_largest([5, 9, 3, 7]) -> 7
    second_largest([4, 4, 1])    -> 4     (duplicates of the max are allowed)
    second_largest([2])          -> None
    Hint: track TWO running bests, and update both carefully.
    """
    raise NotImplementedError


def reversed_copy(values):
    """4. Return a NEW list with the elements in the opposite order.

    reversed_copy([1, 2, 3]) -> [3, 2, 1]
    The original must be unchanged. No [::-1], no .reverse().
    Hint: loop from len(values) - 1 down to 0 with range(start, stop, -1).
    """
    raise NotImplementedError


def is_sorted(values):
    """5. Return True if `values` is in non-decreasing order.

    is_sorted([1, 2, 2, 5]) -> True
    is_sorted([1, 3, 2])    -> False
    is_sorted([])           -> True       (nothing is out of order)
    Hint: compare each element with the NEXT one, so stop at len - 2.
    """
    raise NotImplementedError


def all_positions(values, target):
    """6. Return a list of EVERY index where `target` appears.

    all_positions([7, 1, 7, 7], 7) -> [0, 2, 3]
    all_positions([1, 2], 9)       -> []
    Hint: linear search that does not stop at the first match.
    """
    raise NotImplementedError


def remove_duplicates(values):
    """7. Return a new list keeping only the FIRST occurrence of each value,
    in the original order.

    remove_duplicates([3, 1, 3, 2, 1]) -> [3, 1, 2]
    Hint: build a result list and check `not in result` before appending.
    """
    raise NotImplementedError


def swap(values, i, j):
    """8. Swap the elements at index i and j IN PLACE. Return nothing.

    v = [1, 2, 3]; swap(v, 0, 2)  ->  v becomes [3, 2, 1]
    If either index is out of range, change nothing.
    This is an array-safe operation: the length never changes.
    Hint: you need a temporary variable - or Python's a, b = b, a.
    """
    raise NotImplementedError


def rotate_left(values):
    """9. Return a NEW list rotated one place to the left.

    rotate_left([1, 2, 3, 4]) -> [2, 3, 4, 1]
    rotate_left([])           -> []
    Hint: every element moves to index i - 1; the first wraps to the end.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART B - two-dimensional arrays
# ---------------------------------------------------------------------------

def row_totals(grid):
    """10. Return a list holding the total of each row.

    row_totals([[1, 2], [10, 20], [0, 0]]) -> [3, 30, 0]
    Hint: nested loop; one accumulator reset at the start of each row.
    """
    raise NotImplementedError


def column_maximum(grid, col):
    """11. Return the largest value in column `col`. None if the grid is empty
    or `col` is out of range.

    column_maximum([[1, 9], [5, 2]], 0) -> 5
    column_maximum([[1, 9], [5, 2]], 1) -> 9
    column_maximum([], 0)               -> None
    Hint: loop over ROWS, holding `col` fixed. Seed with grid[0][col].
    """
    raise NotImplementedError


def count_in_grid(grid, target):
    """12. Return how many cells of the 2-D array equal `target`.

    count_in_grid([[1, 0], [0, 1], [1, 1]], 1) -> 4
    Hint: nested loop, one counter outside both loops.
    """
    raise NotImplementedError


# ===========================================================================
# MARKER - you do not need to read past here, but you may
# ===========================================================================

def _check(label, got, expected):
    if got == expected:
        print("  PASS  %-34s -> %s" % (label, got))
        return True
    print("  FAIL  %-34s -> got %r, expected %r" % (label, got, expected))
    return False


def _run():
    passed = 0
    attempted = 0
    skipped = []

    cases = [
        # (exercise number, label, callable returning the value, expected)
        (1, "count_elements([4, 5, 6])", lambda: count_elements([4, 5, 6]), 3),
        (1, "count_elements([])", lambda: count_elements([]), 0),
        (2, "sum_even([1, 2, 3, 4])", lambda: sum_even([1, 2, 3, 4]), 6),
        (2, "sum_even([1, 3])", lambda: sum_even([1, 3]), 0),
        (2, "sum_even([])", lambda: sum_even([]), 0),
        (3, "second_largest([5, 9, 3, 7])",
         lambda: second_largest([5, 9, 3, 7]), 7),
        (3, "second_largest([4, 4, 1])", lambda: second_largest([4, 4, 1]), 4),
        (3, "second_largest([2])", lambda: second_largest([2]), None),
        (3, "second_largest([-5, -2])", lambda: second_largest([-5, -2]), -5),
        (4, "reversed_copy([1, 2, 3])", lambda: reversed_copy([1, 2, 3]),
         [3, 2, 1]),
        (4, "reversed_copy([])", lambda: reversed_copy([]), []),
        (4, "original untouched", _original_untouched, [1, 2, 3]),
        (5, "is_sorted([1, 2, 2, 5])", lambda: is_sorted([1, 2, 2, 5]), True),
        (5, "is_sorted([1, 3, 2])", lambda: is_sorted([1, 3, 2]), False),
        (5, "is_sorted([])", lambda: is_sorted([]), True),
        (6, "all_positions([7, 1, 7, 7], 7)",
         lambda: all_positions([7, 1, 7, 7], 7), [0, 2, 3]),
        (6, "all_positions([1, 2], 9)", lambda: all_positions([1, 2], 9), []),
        (7, "remove_duplicates([3, 1, 3, 2, 1])",
         lambda: remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2]),
        (7, "remove_duplicates([])", lambda: remove_duplicates([]), []),
        (8, "swap(v, 0, 2)", _swap_case, [3, 2, 1]),
        (8, "swap out of range changes nothing", _swap_bad_case, [1, 2, 3]),
        (9, "rotate_left([1, 2, 3, 4])", lambda: rotate_left([1, 2, 3, 4]),
         [2, 3, 4, 1]),
        (9, "rotate_left([])", lambda: rotate_left([]), []),
        (10, "row_totals([[1,2],[10,20],[0,0]])",
         lambda: row_totals([[1, 2], [10, 20], [0, 0]]), [3, 30, 0]),
        (11, "column_maximum([[1,9],[5,2]], 0)",
         lambda: column_maximum([[1, 9], [5, 2]], 0), 5),
        (11, "column_maximum([[1,9],[5,2]], 1)",
         lambda: column_maximum([[1, 9], [5, 2]], 1), 9),
        (11, "column_maximum([], 0)", lambda: column_maximum([], 0), None),
        (12, "count_in_grid([[1,0],[0,1],[1,1]], 1)",
         lambda: count_in_grid([[1, 0], [0, 1], [1, 1]], 1), 4),
    ]

    current = None
    for number, label, call, expected in cases:
        if number != current:
            current = number
            print()
            print("Exercise %d" % number)
        try:
            got = call()
        except NotImplementedError:
            print("  ----  %-34s not attempted yet" % label)
            if number not in skipped:
                skipped.append(number)
            continue
        except Exception as error:               # noqa: BLE001 - teaching tool
            print("  ERROR %-34s raised %s: %s"
                  % (label, type(error).__name__, error))
            attempted += 1
            continue
        attempted += 1
        if _check(label, got, expected):
            passed += 1

    print()
    print("=" * 62)
    print("Attempted %d checks, passed %d." % (attempted, passed))
    if skipped:
        print("Still to do: exercise(s) " +
              ", ".join(str(n) for n in skipped))
    elif passed == attempted:
        print("All of them. Now open solutions.py and compare approaches -")
        print("there is often more than one correct answer.")
    print("=" * 62)


def _original_untouched():
    """Check exercise 4 did not mutate its input."""
    source = [1, 2, 3]
    reversed_copy(source)
    return source


def _swap_case():
    values = [1, 2, 3]
    swap(values, 0, 2)
    return values


def _swap_bad_case():
    values = [1, 2, 3]
    swap(values, 0, 99)
    return values


if __name__ == "__main__":
    print("B2.2.2 exercise marker")
    _run()
