"""B2.2.2 - Step 2: the traversal algorithms IB asks for again and again.

Run me:  python3 02_traversal_patterns.py

Every one of these is written the LONG way, with an explicit loop, because the
exam asks you to "construct an algorithm" - not to call a built-in. Each
function ends with a comment showing the equivalent built-in, so you know what
you would use in your IA once the marks are no longer for the loop itself.

The six patterns:
    1. sum and average          (accumulator)
    2. maximum and minimum      (running best)
    3. linear search            (find a position, with a found-flag)
    4. count matching          (conditional accumulator)
    5. filter into a new list   (build-as-you-go)
    6. common elements          (nested loop / two structures)
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ===========================================================================
# PATTERN 1 - ACCUMULATOR: sum and average
# ===========================================================================
def total_of(values):
    """Add every element together.

    The pattern: start an accumulator at the identity value (0 for adding),
    then update it once per element.
    """
    running_total = 0                      # 1. initialise OUTSIDE the loop
    for value in values:                   # 2. visit every element
        running_total = running_total + value   # 3. update
    return running_total                   # 4. report AFTER the loop


def average_of(values):
    """Mean of a list. Guard against the empty list - division by zero."""
    if len(values) == 0:
        return 0                           # or raise an error; decide and say so
    return total_of(values) / len(values)


# ===========================================================================
# PATTERN 2 - RUNNING BEST: maximum and minimum
# ===========================================================================
def largest_of(values):
    """Find the biggest value.

    Start with the FIRST element as the current best - never with 0, because
    every value might be negative. Then compare each remaining element.
    """
    if len(values) == 0:
        return None
    largest = values[0]                    # assume the first is the winner
    for i in range(1, len(values)):        # start at 1: index 0 is already in
        if values[i] > largest:
            largest = values[i]            # new champion
    return largest


def smallest_of(values):
    """Same shape, one operator flipped."""
    if len(values) == 0:
        return None
    smallest = values[0]
    for i in range(1, len(values)):
        if values[i] < smallest:
            smallest = values[i]
    return smallest


def index_of_largest(values):
    """Often more useful: WHERE is the biggest value?"""
    if len(values) == 0:
        return -1
    best_index = 0
    for i in range(1, len(values)):
        if values[i] > values[best_index]:
            best_index = i
    return best_index


# ===========================================================================
# PATTERN 3 - LINEAR SEARCH
# ===========================================================================
def linear_search(values, target):
    """Return the index of target, or -1 if it is not there.

    Linear search checks elements one at a time from the start. It works on
    ANY list, sorted or not. Worst case it looks at all n elements, so its
    efficiency is O(n).

    Returning -1 for 'not found' is the standard convention, because -1 can
    never be a real forwards index.
    """
    for i in range(len(values)):
        if values[i] == target:
            return i                       # found: stop immediately
    return -1                              # loop finished: it was not there


def linear_search_with_flag(values, target):
    """The same algorithm in the flag style IB pseudocode uses.

    Useful when your language has no early 'return', and it is what a
    'construct an algorithm using a while loop' question is fishing for.
    """
    found = False
    position = -1
    i = 0
    while i < len(values) and not found:   # stop as soon as found becomes True
        if values[i] == target:
            found = True
            position = i
        i = i + 1
    return position


# ===========================================================================
# PATTERN 4 - CONDITIONAL ACCUMULATOR: count how many pass a test
# ===========================================================================
def count_passes(marks, pass_mark=50):
    """How many marks are at or above the pass mark?"""
    count = 0
    for mark in marks:
        if mark >= pass_mark:
            count = count + 1
    return count


# ===========================================================================
# PATTERN 5 - BUILD A NEW LIST (filter)
# ===========================================================================
def failing_marks(marks, pass_mark=50):
    """Collect the elements that match a condition into a NEW list.

    Start with an empty list and append. Note this is a DYNAMIC operation -
    you cannot do it with a fixed-size array without first counting.
    """
    result = []
    for mark in marks:
        if mark < pass_mark:
            result.append(mark)
    return result


def doubled(values):
    """Map: same length out, every element transformed."""
    result = []
    for value in values:
        result.append(value * 2)
    return result


# ===========================================================================
# PATTERN 6 - TWO STRUCTURES: elements common to both
# ===========================================================================
def common_elements(first, second):
    """Values that appear in both lists, listed once each.

    A nested loop: for every element of `first`, scan `second`. With lists of
    length n and m that is n * m comparisons - O(n*m). Using `in` hides the
    inner loop but does not remove it.
    """
    result = []
    for value in first:
        if value in second and value not in result:
            result.append(value)
    return result


def common_elements_nested(first, second):
    """Identical logic with the inner loop written out, exam style."""
    result = []
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                already_recorded = False
                for k in range(len(result)):
                    if result[k] == first[i]:
                        already_recorded = True
                if not already_recorded:
                    result.append(first[i])
    return result


# ===========================================================================
# DEMONSTRATION
# ===========================================================================
if __name__ == "__main__":
    marks = [65, 72, 48, 91, 55, 38, 77]

    heading("The data")
    print("marks =", marks)
    print("index   0   1   2   3   4   5   6")

    heading("Pattern 1 - accumulator")
    print("total_of(marks)   =", total_of(marks), "  (built-in: sum)")
    print("average_of(marks) =", round(average_of(marks), 2))
    print("average_of([])    =", average_of([]), "  <- empty list guarded")

    heading("Pattern 2 - running best")
    print("largest_of(marks)     =", largest_of(marks), "  (built-in: max)")
    print("smallest_of(marks)    =", smallest_of(marks), "  (built-in: min)")
    print("index_of_largest(..)  =", index_of_largest(marks),
          "  <- marks[3] is the 91")
    print("largest_of([-5, -2, -9]) =", largest_of([-5, -2, -9]),
          " <- would be WRONG if we had started 'largest = 0'")

    heading("Pattern 3 - linear search")
    for target in (48, 100):
        print("linear_search(marks, %-4s) = %2d"
              % (target, linear_search(marks, target)))
        print("  with-flag version       = %2d"
              % linear_search_with_flag(marks, target))
    print("A -1 means 'not present'. Always check for it before using the")
    print("result as an index!")

    heading("Pattern 4 - conditional count")
    print("count_passes(marks)        =", count_passes(marks))
    print("count_passes(marks, 70)    =", count_passes(marks, 70))

    heading("Pattern 5 - build a new list")
    print("failing_marks(marks) =", failing_marks(marks))
    print("doubled([1, 2, 3])   =", doubled([1, 2, 3]))
    print("original marks still =", marks, "<- untouched, we built a new list")

    heading("Pattern 6 - common elements")
    group_a = [3, 7, 9, 12, 7]
    group_b = [2, 7, 12, 20]
    print("group_a =", group_a)
    print("group_b =", group_b)
    print("common_elements        =", common_elements(group_a, group_b))
    print("common_elements_nested =", common_elements_nested(group_a, group_b))
    print("Note 7 appears twice in group_a but once in the answer - that was a")
    print("design decision, and in an exam you should state it.")

    heading("Efficiency summary (worth quoting in Paper 1)")
    print("  sum / max / min / count / linear search : O(n)  - one pass")
    print("  common elements with a nested loop      : O(n*m)")
    print("  reading one element by index            : O(1)  - instant")
