"""A1.1 - Value Lab, terminal edition.

Run me:  python3 game.py

Six drills on variables, types, operators and tracing. Three lives a run, an
explanation after every answer. Same drills as the web version in
../game/value-lab.html.

The one skill this game trains is PREDICTING what code will do before you run
it. That is the whole difference between guessing and programming.

Needs nothing but the standard library.
"""

import json
import os
import random

SAVE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    ".valuelab_scores.json")
LIVES = 3


# ===========================================================================
# drawing
# ===========================================================================

def rule(char="-", width=68):
    print(char * width)


def draw_code(lines, numbered=True):
    """Print a code block the way an exam paper does."""
    print()
    for i, line in enumerate(lines, start=1):
        if numbered:
            print("     %2d  %s" % (i, line))
        else:
            print("         %s" % line)
    print()


def draw_box(label, value):
    """Draw one variable as a labelled box."""
    text = repr(value)
    print("     %-10s +%s+" % (label, "-" * (len(text) + 2)))
    print("     %-10s | %s |" % ("", text))
    print("     %-10s +%s+" % ("", "-" * (len(text) + 2)))


def wrap(text, width=72, indent="   "):
    """Print `text` wrapped, without importing textwrap."""
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            print()
            continue
        line = indent
        for word in words:
            if len(line) + len(word) + 1 > width and line.strip():
                print(line)
                line = indent + word
            else:
                line = line + (" " if line.strip() else "") + word
        if line.strip():
            print(line)


# ===========================================================================
# question banks
# ===========================================================================

TYPE_OPTIONS = ["int", "float", "str", "bool"]

TYPES = [
    ("42", "int", "A whole number with no decimal point and no quotes."),
    ("42.0", "float",
     "The .0 is what makes it a float. Same value as 42, different type."),
    ('"42"', "str",
     "Quotes mean TEXT. This is the two characters 4 and 2, not a number."),
    ("7 / 2", "float", "`/` is true division and ALWAYS returns a float."),
    ("6 / 3", "float",
     "Still a float - 2.0, not 2. `/` never gives an int, even when it "
     "divides exactly."),
    ("7 // 2", "int", "`//` is floor division; int // int gives an int."),
    ('input("Age: ")', "str",
     "input() ALWAYS returns a str. Always. This is the one to never forget."),
    ("3 < 5", "bool", "A comparison evaluates to True or False."),
    ('"a" + "b"', "str", "str + str concatenates, giving another str."),
    ('float("3")', "float", "float() of anything gives a float: 3.0."),
    ("round(3.7)", "int",
     "round() with no second argument returns an int. round(3.7, 1) would "
     "give a float."),
    ("len([1, 2, 3])", "int", "A count of things is always a whole number."),
    ('7 == "7"', "bool",
     "It compares fine and the answer is False - different types are never "
     "equal. Only `<` and `>` raise a TypeError across types."),
    ("2 ** 10", "int", "int ** positive int stays an int: 1024."),
    ("10 % 3", "int", "The remainder of two ints is an int."),
]

VALUES = [
    ("7 // 2", ["3"], "Floor division: how many whole 2s fit into 7."),
    ("7 % 2", ["1"], "The remainder after taking out the whole 2s."),
    ("7 / 2", ["3.5"], "True division. Note the float."),
    ("6 / 3", ["2.0"],
     "2.0, NOT 2. `/` always returns a float. This exact distinction is "
     "worth a mark."),
    ("-7 // 2", ["-4"],
     "`//` rounds DOWN, towards minus infinity - not towards zero. "
     "int(-7 / 2) would give -3 instead."),
    ("2 + 3 * 4", ["14"], "`*` before `+`. Not 20."),
    ("(2 + 3) * 4", ["20"], "Brackets first, so now it IS 20."),
    ("2 ** 3 ** 2", ["512"],
     "`**` groups RIGHT to left: 2 ** (3 ** 2) = 2 ** 9. Everything else "
     "groups left to right."),
    ("10 - 4 - 3", ["3"],
     "Left to right: (10 - 4) - 3. If it grouped right it would be 9."),
    ("10.0 + 5.0 / 2", ["12.5"],
     "THE average bug. `/` beats `+`, so it is 10.0 + 2.5. Not the mean."),
    ("(10.0 + 5.0) / 2", ["7.5"], "Brackets fix it. This is the mean."),
    ("127 % 10", ["7"], "% 10 peels off the last digit."),
    ("127 // 10", ["12"], "// 10 removes the last digit."),
    ("int(3.9)", ["3"], "int() TRUNCATES. It does not round."),
    ("round(3.9)", ["4"], "round() rounds. Use it when you mean rounding."),
    ("int(-3.9)", ["-3"],
     "int() chops towards zero, so -3. But -3.9 // 1 would be -4.0. "
     "Two different behaviours."),
    ('"10" + "5"', ["105", "'105'"],
     "CONCATENATION, because both sides are strings. The classic "
     "forgot-the-float() bug."),
    ("-3 ** 2", ["-9"],
     "`**` beats the minus sign, so it is -(3 ** 2). (-3) ** 2 would be 9."),
    ("100 // 7 % 5", ["4"],
     "Same precedence level, so left to right: (100 // 7) % 5 = 14 % 5."),
    ("227 // 60", ["3"], "Whole minutes in 227 seconds."),
    ("227 % 60", ["47"], "Leftover seconds. // and % are always a pair."),
    ("bool(0)", ["false"], "0 is the only falsy number."),
    ('bool("False")', ["true"],
     "ANY non-empty string is True - even the text \"False\". Nasty one."),
    ("0.1 + 0.2 == 0.3", ["false"],
     "Floats are binary approximations, so the sum is 0.30000000000000004. "
     "Never compare floats with ==."),
    ("7 == 7.0", ["true"],
     "Equal in VALUE, even though the types differ. Compare with `is`, "
     "which asks a different question."),
]

TRACES = [
    (["total = 0",
      "for value in [3, 7, 11]:",
      "    total = total + value"],
     "total", ["21"],
     "The accumulator pattern: start at 0, visit each, add it on. 3+7+11."),

    (["total = 0",
      "for value in [3, 7, 11]:",
      "    total = value"],
     "total", ["11"],
     "`total = value` OVERWRITES instead of accumulating, so you are left "
     "with the last value. Look for the missing `total +` on line 3."),

    (["count = 0",
      "for value in [4, 8, 15, 16]:",
      "    if value % 2 == 0:",
      "        count = count + 1"],
     "count", ["3"],
     "4, 8 and 16 are even; 15 is not. A conditional count."),

    (["best = 0",
      "for value in [-5, -2, -9]:",
      "    if value > best:",
      "        best = value"],
     "best", ["0"],
     "BROKEN, and the answer 0 proves it - 0 is not even in the list. "
     "Seed the running best with values[0], never with 0."),

    (["numbers = [10, 5]",
      "total = 0",
      "for value in numbers:",
      "    total = total + value",
      "average = total / len(numbers)"],
     "average", ["7.5"],
     "15 / 2 = 7.5. The `/` gives a float, and len() means it still works "
     "if you add a third number."),

    (["number = 1274",
      "digits = 0",
      "while number > 0:",
      "    digits = digits + 1",
      "    number = number // 10"],
     "digits", ["4"],
     "Each pass removes one digit from the right. 1274 -> 127 -> 12 -> 1 "
     "-> 0, so four passes."),

    (["x = 5",
      "y = x",
      "x = 10"],
     "y", ["5"],
     "`y = x` copied the VALUE 5. Re-pointing x later does not follow "
     "through to y. (Lists are the exception - see the lists unit.)"),

    (["total = 10",
      "total = total + 5",
      "total = total * 2"],
     "total", ["30"],
     "Each line re-points the name: 10, then 15, then 30. Right-hand side "
     "always evaluated first."),

    (["first = \"10\"",
      "second = \"5\"",
      "joined = first + second"],
     "joined", ["105", "'105'"],
     "Both are strings, so + concatenates. This is what your program does "
     "when you forget float()."),

    (["seconds = 227",
      "minutes = seconds // 60",
      "seconds = seconds % 60"],
     "seconds", ["47"],
     "Line 3 overwrites `seconds` with the remainder. Careful - reusing a "
     "name for a different meaning is legal and confusing."),
]

CASTS = [
    ('float("3.5")', "3.5", "A valid real-number literal."),
    ('int("3.5")', "ValueError",
     "int() parses WHOLE numbers only; the dot is not valid in one. Use "
     "int(float(\"3.5\")) if you want 3."),
    ('float("ten")', "ValueError", "Words are not numbers. Catch this one."),
    ('int("42")', "42", "A clean whole-number string."),
    ('float("")', "ValueError",
     "The empty string. This is what you get when the user just presses "
     "Enter, so your validation must handle it."),
    ('float(" 7 ")', "7.0",
     "float() strips surrounding whitespace for you. A rare kindness."),
    ('float("12abc")', "ValueError",
     "All or nothing - it will not read the 12 and stop."),
    ('int(float("3.9"))', "3", "float() then int(), and int() truncates."),
    ('float("4e2")', "400.0",
     "Scientific notation IS a valid float literal: 4 x 10^2."),
    ('float("3,5")', "ValueError",
     "A comma is the decimal separator in much of the world, but Python "
     "insists on a dot. Worth saying so in your error message."),
]

FORMATS = [
    ('f"{1234.5678:.2f}"', "'1234.57'",
     ".2f means two decimal places, and it rounds."),
    ('f"{20 / 3:.1f}"', "'6.7'",
     "6.666... to one decimal place. You can put a calculation in the "
     "braces."),
    ('f"{1234.5:,.2f}"', "'1,234.50'",
     "The comma adds thousands separators; .2f keeps the trailing zero."),
    ('f"{7:.0f}"', "'7'", ".0f means no decimals at all."),
    ('f"{0.5:+.2f}"', "'+0.50'", "The + forces the sign to be shown."),
    ('f"{42}"', "'42'",
     "Any value becomes text inside an f-string - no str() needed."),
    ('f"{3.0}"', "'3.0'",
     "With no format spec you get Python's own repr, floats and all."),
    ('f"{2 + 3}"', "'5'",
     "The braces hold an EXPRESSION, which is evaluated first."),
]

BUGS = [
    (["first = input(\"First: \")",
      "second = input(\"Second: \")",
      "print((first + second) / 2)"],
     [1, 2],
     "Lines 1 and 2 are missing float(), so line 3 tries to divide a "
     "string. Either line is the right answer - the fix belongs at the "
     "input, not at the division."),

    (["first = float(input(\"First: \"))",
      "second = float(input(\"Second: \"))",
      "average = first + second / 2",
      "print(average)"],
     [3],
     "Line 3 needs brackets: (first + second) / 2. As written, `/` runs "
     "first and the answer is silently wrong."),

    (["total = 0",
      "for value in [3, 7, 11]:",
      "    total = value",
      "print(total)"],
     [3],
     "Line 3 overwrites the accumulator. It should be "
     "`total = total + value`."),

    (["numbers = [4, 8, 15]",
      "total = 0",
      "for value in numbers:",
      "    total = total + value",
      "average = total / 2"],
     [5],
     "Line 5 hard-codes 2 when there are 3 numbers. Use len(numbers) so "
     "the code cannot disagree with the data."),

    (["mark = float(input(\"Mark: \"))",
      "if mark = 100:",
      "    print(\"Perfect!\")"],
     [2],
     "Line 2 uses `=` (store) where it needs `==` (compare). SyntaxError."),

    (["values = []",
      "total = 0",
      "for value in values:",
      "    total = total + value",
      "print(total / len(values))"],
     [5],
     "Line 5 divides by zero when the list is empty. Guard it: "
     "`if len(values) == 0:` first."),

    (["sum = 0",
      "for value in [1, 2, 3]:",
      "    sum = sum + value",
      "print(sum([4, 5]))"],
     [1],
     "Line 1 shadows the built-in sum(), so line 4 fails with "
     "'int' object is not callable. Name it `total`."),

    (["price = float(input(\"Price: \"))",
      "pence = int(price * 100)",
      "print(pence)"],
     [2],
     "Line 2 truncates: 0.99 * 100 is stored as 98.99999999999999, so you "
     "get 98. Use int(round(price * 100))."),
]


# ===========================================================================
# question makers
# ===========================================================================

def q_type():
    expression, answer, why = random.choice(TYPES)
    options = list(TYPE_OPTIONS)
    return {
        "ask": "What is the data type of this expression?",
        "code": [expression],
        "numbered": False,
        "options": options,
        "answer": options.index(answer),
        "input": "choice",
        "why": why,
        "revise": "02_variables_and_types.py",
    }


def q_value():
    expression, accept, why = random.choice(VALUES)
    return {
        "ask": "What is the VALUE of this expression? Type it exactly as\n"
               "Python would show it - 3.5 and 3 and 3.0 are different "
               "answers.",
        "code": [expression],
        "numbered": False,
        "options": None,
        "answer": accept,
        "input": "free",
        "why": why,
        "revise": "03_operators.py",
    }


def q_trace():
    lines, variable, accept, why = random.choice(TRACES)
    return {
        "ask": "Trace this code. What is the final value of `%s`?" % variable,
        "code": lines,
        "numbered": True,
        "options": None,
        "answer": accept,
        "input": "free",
        "why": why,
        "revise": "01_trace_your_program.py",
    }


def q_cast():
    expression, answer, why = random.choice(CASTS)
    wrong = [other[1] for other in CASTS if other[1] != answer]
    options = random.sample(sorted(set(wrong)), 3) + [answer]
    random.shuffle(options)
    return {
        "ask": "What does this evaluate to? (ValueError means it raises one.)",
        "code": [expression],
        "numbered": False,
        "options": options,
        "answer": options.index(answer),
        "input": "choice",
        "why": why,
        "revise": "05_safe_input.py",
    }


def q_format():
    expression, answer, why = random.choice(FORMATS)
    wrong = [other[1] for other in FORMATS if other[1] != answer]
    options = random.sample(sorted(set(wrong)), 3) + [answer]
    random.shuffle(options)
    return {
        "ask": "What string does this f-string produce?",
        "code": [expression],
        "numbered": False,
        "options": options,
        "answer": options.index(answer),
        "input": "choice",
        "why": why,
        "revise": "04_input_output.py",
    }


def q_bug():
    lines, answers, why = random.choice(BUGS)
    return {
        "ask": "Exactly one thing is wrong here. Which LINE NUMBER is it?",
        "code": lines,
        "numbered": True,
        "options": None,
        "answer": [str(a) for a in answers],
        "input": "free",
        "why": why,
        "revise": "08_pitfalls.py",
    }


DRILLS = [
    ("1", "type", "Name That Type", 8, q_type),
    ("2", "value", "Predict The Value", 8, q_value),
    ("3", "trace", "Trace The Code", 7, q_trace),
    ("4", "cast", "Will It Convert?", 7, q_cast),
    ("5", "format", "Format It", 6, q_format),
    ("6", "bug", "Spot The Bug", 7, q_bug),
    ("7", "boss", "Boss Run (all six)", 14, None),
]


def build_run(key):
    if key == "boss":
        makers = [q_type, q_value, q_trace, q_cast, q_format, q_bug]
        run = [makers[i % len(makers)]() for i in range(14)]
        random.shuffle(run)
        return run
    drill = [d for d in DRILLS if d[1] == key][0]
    return [drill[4]() for _ in range(drill[3])]


# ===========================================================================
# input and answer checking
# ===========================================================================

class Quit(Exception):
    """Raised when the player types q - unwinds straight back to the menu."""


def normalise(text):
    """Reduce an answer to a comparable form."""
    cleaned = text.strip().lower().replace(" ", "")
    cleaned = cleaned.strip('"').strip("'")
    return cleaned


def ask_player(question):
    """Read one answer. Returns an option index, or a normalised string."""
    style = question["input"]
    if style == "choice":
        for i, option in enumerate(question["options"]):
            print("     %d) %s" % (i + 1, option))
    while True:
        if style == "choice":
            raw = input("   your answer (1-%d) > "
                        % len(question["options"])).strip()
        else:
            raw = input("   your answer > ").strip()

        if raw.lower() in ("q", "quit"):
            raise Quit
        if raw == "":
            continue

        if style == "free":
            return normalise(raw)

        try:
            value = int(raw)
        except ValueError:
            print("   Pick one of the numbers listed (or q to stop).")
            continue
        if not 1 <= value <= len(question["options"]):
            print("   Pick one of the numbers listed.")
            continue
        return value - 1


def is_right(question, given):
    if question["input"] == "choice":
        return given == question["answer"]
    return given in [normalise(a) for a in question["answer"]]


def shown_answer(question):
    if question["input"] == "choice":
        return question["options"][question["answer"]]
    return " or ".join(question["answer"])


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
    print("  %s - %d questions, %d lives. Type q at any prompt to stop."
          % (name, len(questions), LIVES))
    rule("=")

    try:
        for number, question in enumerate(questions, start=1):
            print()
            rule()
            print("  Q%d/%d    score %d    streak x%d    lives %s"
                  % (number, len(questions), score,
                     min(1 + streak // 2, 3),
                     "#" * lives + "." * (LIVES - lives)))
            rule()
            wrap(question["ask"])
            draw_code(question["code"], question["numbered"])

            given = ask_player(question)
            answered += 1

            if is_right(question, given):
                multiplier = min(1 + streak // 2, 3)
                gained = 10 * multiplier
                score += gained
                streak += 1
                correct += 1
                print()
                print("   CORRECT  +%d points%s"
                      % (gained, "  (x%d streak bonus)" % multiplier
                         if multiplier > 1 else ""))
            else:
                lives -= 1
                streak = 0
                print()
                print("   WRONG. The answer is %s." % shown_answer(question))
                misses[question["revise"]] = misses.get(
                    question["revise"], 0) + 1

            print()
            wrap("WHY: " + question["why"])

            if lives == 0:
                print()
                rule("=")
                print("  Out of lives after %d questions." % number)
                rule("=")
                break
    except Quit:
        print()
        print("   Stopped early - score still counts.")

    report(key, name, score, correct, answered, misses)


def report(key, name, score, correct, answered, misses):
    print()
    rule("=")
    print("  %s - final score %d" % (name, score))
    rule("=")
    if answered:
        print("  Correct: %d of %d (%.0f%%)"
              % (correct, answered, 100 * correct / answered))
    else:
        print("  Nothing answered.")

    if misses:
        print()
        print("  Go and re-read:")
        for filename in sorted(misses, key=lambda f: -misses[f]):
            print("      %-30s (%d missed)" % (filename, misses[filename]))
    elif answered:
        print()
        print("  Nothing missed. Try drill 7, the boss run.")

    scores = load_scores()
    best = scores.get(key, 0)
    if score > best:
        scores[key] = score
        save_scores(scores)
        print()
        print("  NEW BEST for this drill (was %d)." % best)
    elif answered:
        print()
        print("  Your best on this drill is %d." % best)


# ===========================================================================
# saved scores
# ===========================================================================

def load_scores():
    try:
        with open(SAVE) as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def save_scores(scores):
    try:
        with open(SAVE, "w") as handle:
            json.dump(scores, handle)
    except OSError:
        pass


# ===========================================================================
# menu
# ===========================================================================

def menu():
    scores = load_scores()
    print()
    rule("=")
    print("  VALUE LAB - A1.1 variables, types, operators and tracing")
    rule("=")
    print("  Predict what the code does BEFORE you run it. That is the skill.")
    print()
    for choice, key, name, count, _ in DRILLS:
        best = scores.get(key)
        tail = "best %d" % best if best else "not played"
        print("    %s)  %-22s %2d questions    %s"
              % (choice, name, count, tail))
    print()
    print("    q)  quit")
    print()


def main():
    while True:
        menu()
        choice = input("  pick a drill > ").strip().lower()
        if choice in ("q", "quit", ""):
            print()
            print("  Come back and beat those scores.")
            print("  Lessons:  python3 01_trace_your_program.py")
            print()
            return
        match = [d for d in DRILLS if d[0] == choice]
        if not match:
            print("\n  No such drill - pick a number from the list.")
            continue
        _, key, name, _, _ = match[0]
        play(key, name)
        input("\n  press Enter for the menu ")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("  Stopped.")
