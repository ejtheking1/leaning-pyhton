# Learning Python — IB DP Computer Science (first exams 2027/2028)

A hands-on Python course built around the **new IB DP Computer Science syllabus**.

## Current unit: B2.2 — Data structures (lists & arrays)

Everything lives in [`b2_2_lists_and_arrays/`](b2_2_lists_and_arrays/).

Work through it in this order:

| Step | File | What you learn |
|------|------|----------------|
| 1 | `00_notes.md` | The theory: static arrays vs dynamic lists, memory, the exam vocabulary |
| 2 | `01_lists_basics.py` | Creating, indexing, slicing and mutating a 1-D list |
| 3 | `02_traversal_patterns.py` | The 6 traversal algorithms IB asks for over and over |
| 4 | `03_static_arrays.py` | Writing Python that behaves like a *fixed-size array* (IB pseudocode style) |
| 5 | `04_two_dimensional.py` | 2-D arrays: rows, columns, nested loops |
| 6 | `05_pitfalls.py` | Aliasing, off-by-one, shallow copies — where marks get lost |
| 7 | `exercises.py` | 12 practice tasks with a built-in self-test |
| 8 | `solutions.py` | Worked answers (open only after trying!) |
| 9 | `quiz.md` | Exam-style written questions + mark-scheme answers |
| 10 | `game.py` | **Array Arcade** — six drills, three lives, scored |

### Play it

The same six drills exist twice. In the terminal:

```bash
python3 b2_2_lists_and_arrays/game.py
```

In a browser — click the boxes, trace the loops, pick the buggy line:
**[Array Arcade](https://claude.ai/artifact/PxTFC9T4FxVeJCtEidnsMC)**
(source in [`game/array-arcade.html`](game/array-arcade.html), which also runs
if you just open the file).

Both keep score, take a life for every wrong answer, explain the answer before
you move on, and finish by naming the file you should re-read.

### How to run

```bash
python3 b2_2_lists_and_arrays/01_lists_basics.py
```

Every script prints a narrated walk-through, so you can read the code **and**
watch what it does at the same time.

Check your exercise answers at any point:

```bash
python3 b2_2_lists_and_arrays/exercises.py
```
