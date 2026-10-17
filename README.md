# Learning Python — IB DP Computer Science (first exams 2027/2028)

A hands-on Python course built around the **new IB DP Computer Science syllabus**.
Every script prints a narrated walk-through, so you can read the code **and**
watch what it does at the same time.

```bash
python3 a1_1_fundamentals/01_trace_your_program.py
```

---

## Unit 1 — A1.1 Variables, input and arithmetic

**Start here.** Everything lives in [`a1_1_fundamentals/`](a1_1_fundamentals/).

This unit takes five lines of code —

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b
avg = total / 2

print("The average is", avg)
```

— and pulls out the six separate ideas hiding inside them, one file at a time,
until you can write the grown-up version yourself.

| Step | File | What you learn |
|------|------|----------------|
| 1 | `00_notes.md` | The theory: variables, types, operators, the exam vocabulary |
| 2 | `01_trace_your_program.py` | Those five lines, traced value by value |
| 3 | `02_variables_and_types.py` | Types, casting, and why `"42"` is not `42` |
| 4 | `03_operators.py` | `/` vs `//` vs `%`, precedence, the average bug |
| 5 | `04_input_output.py` | Prompts, f-strings, formatting to 2 d.p. |
| 6 | `05_safe_input.py` | `try`/`except` so "banana" cannot kill your program |
| 7 | `06_two_to_many.py` | 2 numbers → N numbers, and into the lists unit |
| 8 | `07_functions.py` | Splitting logic from I/O so it can be tested |
| 9 | `08_pitfalls.py` | The ten mistakes that cost marks |
| 10 | `exercises.py` | 14 practice tasks with a built-in self-test |
| 11 | `solutions.py` | Worked answers with reasoning (open only after trying!) |
| 12 | `quiz.md` | 16 exam-style questions + full mark scheme (66 marks) |
| 13 | `game.py` | **Value Lab** — six drills, three lives, scored |

---

## Unit 2 — B2.2 Data structures (lists & arrays)

Everything lives in [`b2_2_lists_and_arrays/`](b2_2_lists_and_arrays/).
Unit 1 ends exactly where this one begins.

| Step | File | What you learn |
|------|------|----------------|
| 1 | `00_notes.md` | The theory: static arrays vs dynamic lists, memory, the exam vocabulary |
| 2 | `01_lists_basics.py` | Creating, indexing, slicing and mutating a 1-D list |
| 3 | `02_traversal_patterns.py` | The 6 traversal algorithms IB asks for over and over |
| 4 | `03_static_arrays.py` | Writing Python that behaves like a *fixed-size array* |
| 5 | `04_two_dimensional.py` | 2-D arrays: rows, columns, nested loops |
| 6 | `05_pitfalls.py` | Aliasing, off-by-one, shallow copies — where marks get lost |
| 7 | `exercises.py` | 12 practice tasks with a built-in self-test |
| 8 | `solutions.py` | Worked answers (open only after trying!) |
| 9 | `quiz.md` | Exam-style written questions + mark-scheme answers |
| 10 | `game.py` | **Array Arcade** — six drills, three lives, scored |

---

## Check your answers

Both units self-mark. Replace each `raise NotImplementedError` with your own
code, then run the file again:

```bash
python3 a1_1_fundamentals/exercises.py
python3 b2_2_lists_and_arrays/exercises.py
```

## Play it

Each unit's drills exist twice — once in the terminal, once in a browser.
Both keep score, take a life for every wrong answer, explain the answer before
you move on, and finish by naming the file you should re-read.

```bash
python3 a1_1_fundamentals/game.py          # Value Lab
python3 b2_2_lists_and_arrays/game.py      # Array Arcade
```

In a browser — type the value, trace the loop, click the buggy line:

- **[Value Lab](https://claude.ai/artifact/7qcdhiLRipaMwqNbTyvTL7)** — types, operators, tracing
  (source in [`game/value-lab.html`](game/value-lab.html))
- **[Array Arcade](https://claude.ai/artifact/PxTFC9T4FxVeJCtEidnsMC)** — lists and arrays
  (source in [`game/array-arcade.html`](game/array-arcade.html))

Both HTML files also run if you just open them from disk.

---

## The order that works

1. Read `00_notes.md` for the unit.
2. Run the numbered lesson files in order. Change the numbers, re-run, break
   things on purpose — that is the fastest way to learn.
3. Do `exercises.py` until it says everything passes.
4. Only then open `solutions.py` and compare approaches.
5. Answer `quiz.md` on paper and mark yourself.
6. Play the game. Whatever it tells you to re-read, re-read.
