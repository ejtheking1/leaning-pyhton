"""B2.2.2 - Step 4: two-dimensional arrays.

Run me:  python3 04_two_dimensional.py

A 2-D array is an array of arrays. Say "ROW first, then COLUMN" out loud every
single time you write grid[r][c], until it is automatic.
"""


def heading(text):
    print()
    print(text)
    print("-" * len(text))


# ===========================================================================
heading("1. Building a 2-D array")

# Four students, three tests each. Rows = students, columns = tests.
marks = [
    [65, 72, 80],      # row 0 - Ama
    [48, 55, 51],      # row 1 - Ben
    [91, 88, 95],      # row 2 - Chloe
    [38, 42, 60],      # row 3 - Dev
]
students = ["Ama", "Ben", "Chloe", "Dev"]
tests = ["Test1", "Test2", "Test3"]

ROWS = len(marks)              # number of rows        = number of students
COLS = len(marks[0])           # length of ONE row     = number of tests

print("ROWS (len(marks))    =", ROWS)
print("COLS (len(marks[0])) =", COLS)
print("marks[2][0] =", marks[2][0], "-> row 2, column 0 -> Chloe's Test1")
print("marks[0][2] =", marks[0][2], "-> row 0, column 2 -> Ama's Test3")
print()
print("Swap the two indices and you get a different, plausible-looking,")
print("completely wrong number. There is no error message to warn you.")


# ===========================================================================
heading("2. Creating an EMPTY 2-D array (the right way)")

good = [[0] * COLS for _ in range(ROWS)]    # a fresh row object each time
print("good =", good)
good[0][0] = 99
print("after good[0][0] = 99 ->", good, "<- only ONE cell changed. Correct.")

bad = [[0] * COLS] * ROWS                   # DANGER: 4 references to ONE row
bad[0][0] = 99
print()
print("bad  =", bad, "<- ONE change hit every row!")
print("Because [row] * 4 copies the REFERENCE, not the row. All four rows")
print("are the same object in memory. This is called ALIASING.")


# ===========================================================================
heading("3. Printing a grid neatly")

print("        " + "".join("%8s" % t for t in tests))
for r in range(ROWS):
    line = "%-8s" % students[r]
    for c in range(COLS):
        line += "%8d" % marks[r][c]
    print(line)


# ===========================================================================
heading("4. Nested loops - the core skill")

print("ROW-WISE traversal (outer = rows, inner = columns):")
print("  visits in order: (0,0) (0,1) (0,2) (1,0) (1,1) ...")
print("  this is also the order the cells sit in memory - 'row-major'")
total = 0
for r in range(ROWS):
    row_total = 0
    for c in range(COLS):
        row_total += marks[r][c]
        total += marks[r][c]
    print("   %-6s total %3d  average %5.1f" % (students[r], row_total,
                                                row_total / COLS))
print("   ALL marks: total %d, average %.2f" % (total, total / (ROWS * COLS)))

print()
print("COLUMN-WISE traversal (outer = columns, inner = rows):")
print("  the loops are SWAPPED - this is how you get per-test statistics")
for c in range(COLS):
    col_total = 0
    col_best = marks[0][c]
    for r in range(ROWS):
        col_total += marks[r][c]
        if marks[r][c] > col_best:
            col_best = marks[r][c]
    print("   %-6s average %5.1f  highest %d" % (tests[c], col_total / ROWS,
                                                 col_best))


# ===========================================================================
heading("5. Searching a 2-D array")

def find_value(grid, target):
    """Return (row, col) of the first match, or (-1, -1) if absent."""
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == target:
                return (r, c)
    return (-1, -1)


for target in (88, 100):
    position = find_value(marks, target)
    if position == (-1, -1):
        print("   %3d not found" % target)
    else:
        print("   %3d found at row %d, column %d (%s, %s)"
              % (target, position[0], position[1],
                 students[position[0]], tests[position[1]]))


def best_overall(grid, names):
    """Which row has the highest total? Combines patterns 1 and 2."""
    best_index = 0
    best_total = -1
    for r in range(len(grid)):
        row_total = 0
        for c in range(len(grid[r])):
            row_total += grid[r][c]
        if row_total > best_total:
            best_total = row_total
            best_index = r
    return names[best_index], best_total


name, score = best_overall(marks, students)
print("   top student overall:", name, "with", score)


# ===========================================================================
heading("6. Transposing - rows become columns")

def transpose(grid):
    """Build a new grid where new[c][r] == old[r][c]."""
    rows = len(grid)
    cols = len(grid[0])
    result = [[0] * rows for _ in range(cols)]   # note: cols x rows
    for r in range(rows):
        for c in range(cols):
            result[c][r] = grid[r][c]
    return result


flipped = transpose(marks)
print("original is %d x %d, transposed is %d x %d"
      % (ROWS, COLS, len(flipped), len(flipped[0])))
for row in flipped:
    print("   ", row)


# ===========================================================================
heading("7. A 2-D array that is not numbers: noughts and crosses")

board = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"],
]

for r in range(3):
    print("   " + " | ".join(board[r]))
    if r < 2:
        print("   " + "-" * 9)


def diagonal_win(board, player):
    """Check the top-left to bottom-right diagonal: cells where row == col."""
    for i in range(3):
        if board[i][i] != player:
            return False
    return True


print()
print("   X wins on the main diagonal?", diagonal_win(board, "X"))
print("   O wins on the main diagonal?", diagonal_win(board, "O"))
print()
print("The main diagonal is every cell where row index == column index.")
print("The other diagonal is every cell where row + col == size - 1.")


# ===========================================================================
heading("8. Memory: why row-major order matters")

print("The 2-D array")
print("   [[1, 2, 3],")
print("    [4, 5, 6]]")
print("is really stored as a single run of cells:  1 2 3 4 5 6")
print()
print("So the address of grid[r][c] is")
print("   base_address + (r * COLS + c) * size_of_one_element")
print()
print("Worked example: base 2000, 4 bytes per int, COLS = 3, want grid[1][2]:")
print("   2000 + (1 * 3 + 2) * 4 = 2000 + 20 = 2020")
print()
print("That formula is why every row of a true 2-D array must be the same")
print("length - the arithmetic breaks otherwise. Python lists let you make")
print("ragged rows, but IB 2-D arrays are rectangular.")
