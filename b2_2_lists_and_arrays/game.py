"""B2.2.2 - Array Arcade, terminal edition.

Run me:  python3 game.py

Six drills on lists and arrays, three lives a run, an explanation after every
answer. Same drills as the web version in ../game/array-arcade.html.

This file is also worth READING: the whole game is built out of the structures
it is teaching. Questions are dictionaries in a list, the drill menu is a list
of tuples, the grid questions are lists of lists, and the scoring loop is the
accumulator pattern from 02_traversal_patterns.py.

Needs nothing but the standard library.
"""

import json
import os
import random

SAVE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".arcade_scores.json")
LIVES = 3


# ===========================================================================
# drawing
# ===========================================================================

def rule(char="-", width=66):
    print(char * width)


def draw_strip(name, values, show_index):
    """Draw a 1-D list as labelled boxes, the way the notes draw them."""
    cells = [str(v).center(4) for v in values]
    edge = "+" + "+".join("----" for _ in cells) + "+"
    labels = [str(i) if show_index else "?" for i in range(len(values))]
    # the name field is 8 wide plus a space, so the first "|" lands at column 9
    # and the first cell at column 10 - the index row has to start there too
    print()
    print(" " * 10 + " ".join(label.center(4) for label in labels))
    print(" " * 9 + edge)
    print("%8s " % name + "|" + "|".join(cells) + "|")
    print(" " * 9 + edge)
    print()


def draw_grid(matrix):
    """Draw a 2-D array with row and column headers."""
    cols = len(matrix[0])
    print()
    print("        " + " ".join(("c" + str(c)).center(4) for c in range(cols)))
    edge = "      +" + "+".join("----" for _ in range(cols)) + "+"
    print(edge)
    for r, row in enumerate(matrix):
        print("   r%d |" % r + "|".join(str(v).center(4) for v in row) + "|")
        print(edge)
    print()


def draw_code(lines, numbered=True):
    print()
    for i, line in enumerate(lines):
        print(("   %2d | %s" % (i, line)) if numbered else "      " + line)
    print()


def wrap(text, width=70, indent="   "):
    """Print a paragraph without dragging in textwrap - one accumulator again."""
    words = text.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > width:
            print(indent + line)
            line = word
        else:
            line = word if line == "" else line + " " + word
    if line:
        print(indent + line)


# ===========================================================================
# drill 0 - Index Hunt
# ===========================================================================

def q_index():
    n = random.randint(5, 7)
    name = random.choice(["marks", "temps", "scores", "prices", "ages"])
    values = random.sample(range(10, 99), n)
    kind = random.choice(["first", "direct", "direct", "last", "lenminus",
                          "negative", "indexof"])
    show = False

    # Questions ask for a VALUE wherever the index appears in the question
    # itself - otherwise the answer is just the number you were handed.
    if kind == "first":
        ask = "What value is the first element of %s?" % name
        answer = values[0]
        why = "The first element is %s[0] = %d, not %s[1]. Python counts from zero." % (
            name, values[0], name)
    elif kind == "direct":
        i = random.randint(1, n - 1)
        ask = "What value is stored at %s[%d]?" % (name, i)
        answer = values[i]
        why = "Count 0, 1, 2 ... from the left: index %d holds %d." % (i, values[i])
    elif kind == "last":
        ask = "Which index holds the last element of %s?" % name
        answer = n - 1
        why = "len(%s) is %d, but the last index is %d - 1 = %d. That gap is the off-by-one trap." % (name, n, n, n - 1)
    elif kind == "lenminus":
        back = random.randint(1, 3)
        ask = "What value is stored at %s[len(%s) - %d]?" % (name, name, back)
        answer = values[n - back]
        why = "len(%s) is %d, so this is index %d - %d = %d, which holds %d." % (
            name, n, n, back, n - back, values[n - back])
    elif kind == "negative":
        j = random.randint(1, 3)
        show = True
        ask = "What value is stored at %s[-%d]?" % (name, j)
        answer = values[n - j]
        why = "-1 is the last box, so -%d counts back %d from the end: index %d - %d = %d, holding %d." % (
            j, j, n, j, n - j, values[n - j])
    else:
        k = random.randint(0, n - 1)
        ask = "What does %s.index(%d) return?" % (name, values[k])
        answer = k
        why = ".index() hands back the INDEX of the value, not the value: %d sits at index %d." % (values[k], k)

    return {"topic": "index", "ask": ask, "answer": answer, "why": why,
            "input": "index", "limit": n - 1,
            "draw": lambda: draw_strip(name, values, show)}


# ===========================================================================
# drill 1 - Slice Select
# ===========================================================================

def q_slice():
    n = random.randint(6, 8)
    letters = ["'%s'" % c for c in "abcdefgh"[:n]]
    a = random.randint(0, n - 3)
    b = random.randint(a + 2, n)
    kind = random.choice(["select", "select", "count", "which"])

    if kind == "select":
        ask = "Which indices does letters[%d:%d] return? List them, separated by commas." % (a, b)
        answer = list(range(a, b))
        why = ("The start is included, the stop is not: indices %d up to but not including %d. "
               "That is %d elements, because the count is always stop - start." % (a, b, b - a))
        return {"topic": "slice", "ask": ask, "answer": answer, "why": why,
                "input": "list", "limit": n - 1,
                "draw": lambda: draw_strip("letters", letters, True)}

    if kind == "count":
        ask = "How many elements does letters[%d:%d] return?" % (a, b)
        why = ("Stop minus start: %d - %d = %d. The box at index %d is left out, "
               "which is why the subtraction works." % (b, a, b - a, b))
        return {"topic": "slice", "ask": ask, "answer": b - a, "why": why,
                "input": "number",
                "draw": lambda: draw_strip("letters", letters, True)}

    result = letters[a:b]
    options = ["letters[%d:%d]" % (a, b)]
    if b < n:
        options.append("letters[%d:%d]" % (a, b + 1))
    if a > 0:
        options.append("letters[%d:%d]" % (a - 1, b))
    options.append("letters[%d:%d]" % (a + 1, b))
    options.append("letters[%d:%d]" % (a, b - 1))
    options = options[:4]
    correct = options[0]
    random.shuffle(options)
    why = ("The result starts at index %d and ends at index %d, so the stop must be %d "
           "- one past the last element you want." % (a, b - 1, b))
    return {"topic": "slice", "ask": "Which slice returns [%s]?" % ", ".join(result),
            "answer": options.index(correct), "why": why,
            "input": "choice", "options": options,
            "draw": lambda: draw_strip("letters", letters, True)}


# ===========================================================================
# drill 2 - Trace the Loop
# ===========================================================================

def _trace_sum():
    v = random.sample(range(2, 20), 4)
    return ["values = %s" % v, "total = 0", "for value in values:",
            "    total = total + value", "print(total)"], sum(v), \
        "An accumulator: start at 0, add every element. %s = %d." % (
            " + ".join(str(x) for x in v), sum(v))


def _trace_max_zero():
    v = random.sample(range(-40, -2), 4)
    return ["values = %s" % v, "largest = 0", "for value in values:",
            "    if value > largest:", "        largest = value",
            "print(largest)"], 0, \
        ("No element is greater than 0, so largest never changes - the answer is 0, "
         "a value that is not even in the list. Seed a running maximum with values[0].")


def _trace_max_ok():
    v = random.sample(range(-20, 40), 5)
    return ["values = %s" % v, "largest = values[0]",
            "for i in range(1, len(values)):", "    if values[i] > largest:",
            "        largest = values[i]", "print(largest)"], max(v), \
        "Seeded with values[0] = %d, then replaced whenever something bigger turns up: %d." % (v[0], max(v))


def _trace_search():
    v = random.sample(range(10, 60), 6)
    k = random.randint(0, 5)
    return ["values = %s" % v, "found = -1", "for i in range(len(values)):",
            "    if values[i] == %d:" % v[k], "        found = i",
            "        break", "print(found)"], k, \
        "Linear search returns the INDEX, not the value: %d sits at index %d." % (v[k], k)


def _trace_missing():
    v = random.sample(range(10, 60), 5)
    target = random.randint(61, 95)
    return ["values = %s" % v, "found = -1", "for i in range(len(values)):",
            "    if values[i] == %d:" % target, "        found = i",
            "print(found)"], -1, \
        ("%d is not in the list, so the if never runs and found keeps its starting value, -1. "
         "That is the standard 'not found' signal: -1 can never be a real forwards index." % target)


def _trace_skip():
    v = random.sample(range(5, 25), 5)
    return ["values = %s" % v, "total = 0", "for i in range(1, len(values)):",
            "    total = total + values[i]", "print(total)"], sum(v) - v[0], \
        "range(1, len(values)) starts at 1, so index 0 (the %d) is skipped: %d - %d = %d." % (
            v[0], sum(v), v[0], sum(v) - v[0])


def _trace_count():
    v = random.sample(range(1, 40), 6)
    evens = [x for x in v if x % 2 == 0]
    return ["values = %s" % v, "count = 0", "for value in values:",
            "    if value % 2 == 0:", "        count = count + 1",
            "print(count)"], len(evens), \
        "A conditional counter. The even values are %s - %d of them." % (evens, len(evens))


TRACE = [_trace_sum, _trace_max_zero, _trace_max_ok, _trace_search,
         _trace_missing, _trace_skip, _trace_count]


def q_trace(maker=None):
    lines, answer, why = (maker or random.choice(TRACE))()
    return {"topic": "trace", "ask": "What does this print?", "answer": answer,
            "why": why, "input": "number",
            "draw": lambda: draw_code(lines, numbered=False)}


# ===========================================================================
# drill 3 - Static or Dynamic
# ===========================================================================

SCENARIOS = [
    ("A temperature logged every hour for one day", "array",
     "24 readings, known in advance and never changing - a fixed-size structure is enough."),
    ("Every goal scored across a football season", "list",
     "Nobody knows the final count in advance, so the structure has to grow during execution."),
    ("The 64 squares of a chess board", "array",
     "The board is always 8 x 8: fixed size, fast indexed access, no resizing ever."),
    ("Students who sign up for a trip", "list",
     "Sign-ups arrive while the program runs, so the structure must grow with them."),
    ("The red, green and blue channels of one pixel", "array",
     "Always exactly three values of the same type - the textbook tiny fixed array."),
    ("Chat messages as they arrive", "list",
     "An open-ended stream: the count is unknown at the start, so it must be dynamic."),
    ("The names of the seven days of the week", "array",
     "Seven, forever. Fixed size and all the same type."),
    ("Sensor readings taken until the user presses stop", "list",
     "The user decides when to stop at run time, so the size cannot be fixed in advance."),
    ("A noughts-and-crosses board", "array",
     "A 3 x 3 grid that never changes shape - a fixed 2-D array."),
    ("Items a shopper adds to a basket", "list",
     "Items are added and removed while the program runs."),
]

OPS = [
    ("arr[2] = 9", "safe", "Overwriting one element leaves the length untouched."),
    ("arr.append(9)", "grows", "Appending makes the structure one longer, which a fixed array cannot do."),
    ("arr.pop()", "grows", "Removing an element changes the length."),
    ("arr.insert(0, 5)", "grows", "Inserting grows the structure AND shuffles every later element along."),
    ("arr.remove(5)", "grows", "Removing by value still shortens the structure."),
    ("arr.sort()", "safe", "Sorting rearranges the same elements in place; the length never changes."),
    ("arr.reverse()", "safe", "Reversing in place swaps positions without adding or removing anything."),
    ("arr[0], arr[1] = arr[1], arr[0]", "safe", "A swap is two overwrites - exactly what an array supports."),
    ("del arr[3]", "grows", "Deleting an element shortens the structure."),
    ("arr = arr + [7]", "grows", "This builds a new, longer list; the original size could not hold it."),
]

PROPS = [
    ("Its size is fixed when it is declared", "static",
     "Fixed size at declaration is the defining property of a static structure."),
    ("Memory is allocated as one contiguous block", "static",
     "Contiguous allocation is what makes O(1) address arithmetic possible."),
    ("It can grow while the program is running", "dynamic", "Growing at run time is what 'dynamic' means."),
    ("It needs extra memory for pointers and bookkeeping", "dynamic",
     "That overhead is the price a dynamic structure pays for flexibility."),
    ("It may waste memory in slots that are never filled", "static",
     "You declare the worst-case size up front, and unused slots still occupy memory."),
    ("Reading element i costs the same however large it is", "static",
     "One multiplication and one addition - O(1), independent of size."),
]


def q_kind():
    which = random.choice(["scenario", "scenario", "op", "prop"])
    if which == "scenario":
        text, answer, why = random.choice(SCENARIOS)
        options = ["array", "list"]
        ask = "Array or list?  %s" % text
    elif which == "op":
        code, answer, why = random.choice(OPS)
        options = ["safe", "grows"]
        ask = "Could this run on a fixed-size array?  %s" % code
    else:
        text, answer, why = random.choice(PROPS)
        options = ["static", "dynamic"]
        ask = "Static or dynamic?  %s" % text
    return {"topic": "kind", "ask": ask, "answer": options.index(answer),
            "why": "%s. %s" % (answer.capitalize(), why),
            "input": "choice", "options": options, "draw": None}


# ===========================================================================
# drill 4 - Grid Raid
# ===========================================================================

def q_grid():
    rows, cols = random.randint(3, 4), random.randint(3, 4)
    flat = random.sample(range(10, 99), rows * cols)
    matrix = [flat[r * cols:(r + 1) * cols] for r in range(rows)]
    kind = random.choice(["pick", "pick", "colmax", "offset"])

    if kind == "pick":
        r, c = random.randint(0, rows - 1), random.randint(0, cols - 1)
        ask = "What value is stored at grid[%d][%d]?" % (r, c)
        why = ("Row first, then column: down to row %d, then across to column %d. "
               "Swapping the indices gives a wrong answer with no error message." % (r, c))
        answer = matrix[r][c]
    elif kind == "colmax":
        c = random.randint(0, cols - 1)
        column = [matrix[r][c] for r in range(rows)]
        ask = "What is the largest value in column %d?" % c
        why = ("Column %d holds %s. Walking a column means the ROW index varies "
               "while the column stays fixed." % (c, column))
        answer = max(column)
    else:
        k = random.randint(0, rows * cols - 1)
        r, c = k // cols, k % cols
        ask = ("A 2-D array is stored in row-major order, one whole row after another. "
               "What value sits at memory offset %d?" % k)
        why = ("offset = row x columns + col. With %d columns: row = %d // %d = %d, "
               "column = the remainder %d. So offset %d is grid[%d][%d] = %d."
               % (cols, k, cols, r, c, k, r, c, matrix[r][c]))
        answer = matrix[r][c]

    return {"topic": "grid", "ask": ask, "answer": answer, "why": why,
            "input": "number", "draw": lambda: draw_grid(matrix)}


# ===========================================================================
# drill 5 - Bug Hunt
# ===========================================================================

BUGS = [
    (["def largest(values):", "    largest = 0", "    for value in values:",
      "        if value > largest:", "            largest = value",
      "    return largest"], 1,
     "This returns 0 for a list of all-negative numbers. Which line is to blame?",
     "Seeding with 0 means nothing negative can ever beat it. Start from the data: largest = values[0]."),
    (["def show_all(values):", "    for i in range(len(values) + 1):",
      "        print(values[i])"], 1,
     "This crashes with IndexError on every list. Which line is to blame?",
     "range(len(values)) already gives every valid index, 0 to len-1. The + 1 asks for one index past the end."),
    (["def backup(original):", "    copy = original", "    copy.append(0)",
      "    return copy"], 1,
     "After this runs, the caller's own list has changed too. Which line is to blame?",
     "Assignment copies the reference, not the list - both names are one object. Use original[:]."),
    (["def sorted_copy(values):", "    result = values[:]",
      "    result = result.sort()", "    return result"], 2,
     "This returns None instead of a sorted list. Which line is to blame?",
     ".sort() sorts in place and returns None. Drop the assignment: result.sort() on its own line."),
    (["def row_totals(grid):", "    totals = []", "    total = 0",
      "    for row in grid:", "        for value in row:",
      "            total = total + value", "        totals.append(total)",
      "    return totals"], 2,
     "Every row total except the first comes out too big. Which line is in the wrong place?",
     "The accumulator is never reset, so each row adds to the previous total. total = 0 belongs inside the outer loop."),
    (["def first_position(values, target):", "    position = -1",
      "    for i in range(len(values)):", "        if values[i] == target:",
      "            position = i", "    return position"], 4,
     "This returns the LAST matching position instead of the first. Which line needs a break after it?",
     "Without stopping, a later match overwrites the earlier one. Add break after recording the position."),
    (["def column_total(grid, col):", "    total = 0",
      "    for r in range(len(grid)):", "        total = total + grid[col][r]",
      "    return total"], 3,
     "This reads the wrong cells and crashes on a non-square grid. Which line is to blame?",
     "The indices are swapped. Down a column the row varies and the column is fixed: grid[r][col]."),
    (["def make_grid(rows, cols):", "    return [[0] * cols] * rows"], 1,
     "Writing to one cell of this grid changes the same cell in every row. Which line is to blame?",
     "* rows repeats one row REFERENCE, so all rows are one object. Use [[0] * cols for _ in range(rows)]."),
    (["def drop_evens(numbers):", "    for n in numbers:", "        if n % 2 == 0:",
      "            numbers.remove(n)", "    return numbers"], 3,
     "Given [2, 4, 6, 8] this returns [4, 8] instead of []. Which line is to blame?",
     "Removing from the list the loop is still walking makes it skip elements. Build a new list instead."),
    (["def average(values):", "    total = 0", "    for value in values:",
      "        total = total + value", "    return total / len(values)"], 4,
     "This crashes with ZeroDivisionError on an empty list. Which line is to blame?",
     "len(values) is 0 for an empty list. Guard it first: if len(values) == 0: return 0."),
]


def q_bug(item=None):
    lines, bug, ask, why = item or random.choice(BUGS)
    return {"topic": "bug", "ask": ask + "  (give the line number)", "answer": bug,
            "why": why, "input": "number",
            "draw": lambda: draw_code(lines)}


# ===========================================================================
# drills
# ===========================================================================

DRILLS = [
    ("Index Hunt", "index", 7, q_index, "01_lists_basics.py section 2"),
    ("Slice Select", "slice", 7, q_slice, "01_lists_basics.py section 6"),
    ("Trace the Loop", "trace", 7, q_trace, "02_traversal_patterns.py"),
    ("Static or Dynamic", "kind", 8, q_kind, "00_notes.md section 2"),
    ("Grid Raid", "grid", 7, q_grid, "04_two_dimensional.py"),
    ("Bug Hunt", "bug", 7, q_bug, "05_pitfalls.py"),
    ("Boss Run", "boss", 12, None, "the whole unit"),
]


def build_run(key):
    if key == "bug":
        return [q_bug(b) for b in random.sample(BUGS, 7)]
    if key == "trace":
        return [q_trace(t) for t in random.sample(TRACE, len(TRACE))][:7]
    if key == "boss":
        makers = [q_index, q_slice, q_trace, q_kind, q_grid, q_bug]
        run = [makers[i % len(makers)]() for i in range(12)]
        random.shuffle(run)
        return run
    drill = [d for d in DRILLS if d[1] == key][0]
    return [drill[3]() for _ in range(drill[2])]


# ===========================================================================
# input
# ===========================================================================

class Quit(Exception):
    """Raised when the player types q - unwinds straight back to the menu."""


def ask_player(question):
    """Read one answer and return it in the same shape as question['answer']."""
    style = question["input"]
    if style == "choice":
        for i, option in enumerate(question["options"]):
            print("     %d) %s" % (i + 1, option))
    while True:
        if style == "list":
            raw = input("   indices (e.g. 2,3,4) > ").strip()
        elif style == "choice":
            raw = input("   your answer (1-%d) > " % len(question["options"])).strip()
        else:
            raw = input("   your answer > ").strip()

        if raw.lower() in ("q", "quit"):
            raise Quit
        if raw == "":
            continue

        if style == "list":
            try:
                picked = sorted(int(p) for p in raw.replace(" ", "").split(",") if p != "")
            except ValueError:
                print("   Whole numbers separated by commas, please.")
                continue
            if any(p < 0 or p > question["limit"] for p in picked):
                print("   Those must be valid indices, 0 to %d." % question["limit"])
                continue
            return picked

        try:
            value = int(raw)
        except ValueError:
            print("   A whole number, please (or q to stop).")
            continue
        if style == "choice":
            if not 1 <= value <= len(question["options"]):
                print("   Pick one of the numbers listed.")
                continue
            return value - 1
        return value


# ===========================================================================
# the run loop
# ===========================================================================

def play(key, name):
    questions = build_run(key)
    score = streak = correct = answered = 0
    lives = LIVES
    misses = {}

    print()
    rule("=")
    print("  %s - %d questions, %d lives. Type q at any prompt to stop." % (name, len(questions), LIVES))
    rule("=")

    try:
        for number, question in enumerate(questions, start=1):
            print()
            rule()
            print("  Q%d/%d    score %d    streak x%d    lives %s"
                  % (number, len(questions), score, min(1 + streak // 2, 3),
                     "#" * lives + "." * (LIVES - lives)))
            rule()
            wrap(question["ask"])
            if question["draw"]:
                question["draw"]()
            given = ask_player(question)
            answered += 1

            if given == question["answer"]:
                gain = (100 + 50 * min(streak, 4)) * (2 if key == "boss" else 1)
                correct += 1
                score += gain
                streak += 1
                print("   CORRECT  (+%d)" % gain)
            else:
                streak = 0
                lives -= 1
                misses[question["topic"]] = misses.get(question["topic"], 0) + 1
                shown = question["answer"]
                if question["input"] == "choice":
                    shown = question["options"][question["answer"]]
                print("   NOT QUITE.  The answer was: %s" % shown)
            wrap(question["why"])
            if lives == 0:
                print()
                print("   Out of lives.")
                break
    except Quit:
        print("\n   Stopped early.")

    report(key, name, score, correct, answered, misses)


def report(key, name, score, correct, answered, misses):
    accuracy = round(100 * correct / answered) if answered else 0
    print()
    rule("=")
    print("  %s - final score %d" % (name, score))
    rule("=")
    print("   correct   %d / %d" % (correct, answered))
    print("   accuracy  %d%%" % accuracy)
    for floor, rank in [(95, "Array architect"), (80, "Index master"),
                        (65, "Solid traversal"), (45, "Getting there"),
                        (0, "Back to the notes")]:
        if accuracy >= floor:
            print("   rank      %s" % rank)
            break

    if misses:
        print()
        print("   What to re-read:")
        for topic in sorted(misses, key=lambda t: -misses[t]):
            drill = [d for d in DRILLS if d[1] == topic][0]
            print("     %dx  %-18s %s" % (misses[topic], drill[0], drill[4]))

    best = load_scores()
    previous = best.get(key, 0)
    if score > previous:
        best[key] = score
        save_scores(best)
        print()
        print("   New best for this drill (was %d)." % previous)
    elif previous:
        print()
        print("   Best so far for this drill: %d." % previous)


# ===========================================================================
# saved scores
# ===========================================================================

def load_scores():
    try:
        with open(SAVE, "r") as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (IOError, OSError, ValueError):
        return {}          # no save file yet, or it is unreadable - start fresh


def save_scores(scores):
    try:
        with open(SAVE, "w") as handle:
            json.dump(scores, handle)
    except (IOError, OSError):
        pass               # a read-only disk must not end the game


# ===========================================================================
# menu
# ===========================================================================

BLURBS = {
    "index": "Zero-based counting, len - 1, negative indices.",
    "slice": "Why the stop index is excluded.",
    "trace": "Accumulators, running maxima, linear search.",
    "kind": "Array or list? What a fixed array survives.",
    "grid": "2-D arrays: row before column, row-major offsets.",
    "bug": "One line is wrong. Find it.",
    "boss": "All six drills mixed, double points.",
}


def menu():
    print()
    print("   ARRAY[ARCADE]   IB DP Computer Science, B2.2 data structures")
    best = load_scores()
    print()
    for i, (name, key, count, _gen, _file) in enumerate(DRILLS, start=1):
        mark = "best %d" % best[key] if key in best else "unplayed"
        print("   %d) %-18s %-48s %s" % (i, name, BLURBS[key], mark))
    print("   q) quit")
    print()


def main():
    random.seed()
    print()
    rule("=")
    print("  ARRAY[ARCADE] - lists and arrays, B2.2.2")
    rule("=")
    while True:
        menu()
        choice = input("   pick a drill > ").strip().lower()
        if choice in ("q", "quit", ""):
            print("\n   Bye. Scores are kept in %s\n" % os.path.basename(SAVE))
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(DRILLS):
            print("   Pick a number from the list.")
            continue
        name, key = DRILLS[int(choice) - 1][0], DRILLS[int(choice) - 1][1]
        play(key, name)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n   Bye.\n")
