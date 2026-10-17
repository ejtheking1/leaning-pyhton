# A1.1 — Variables, input and arithmetic

> The theory behind the five lines your teacher gave you. Read this once,
> then work through `01` to `08`. Come back to it before a test.

*(IB sub-topic codes move around between syllabus drafts — what matters is the
content, which every version of the course expects you to know.)*

---

## 1. The program we are pulling apart

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b
avg = total / 2

print("The average is", avg)
```

Five lines, and **six** separate ideas hiding in them:

| Idea | Where |
|------|-------|
| Getting data in from a user | `input(...)` |
| Converting between data types | `float(...)` |
| Storing a value under a name | `a = ...` |
| Doing arithmetic | `a + b`, `total / 2` |
| Order of evaluation | the nesting of the first line |
| Getting data back out | `print(...)` |

No wonder it did not click the first time. Nobody absorbs six ideas at once.

---

## 2. What a variable actually is

A variable is a **name that refers to a value stored in memory**.

```python
score = 7
```

Three things happen, in this order:

1. The value `7` is created in memory.
2. A name `score` is put in a lookup table (the *namespace*).
3. That name is pointed at that value.

```
    namespace            memory
  +-----------+        +--------+
  | score ----|------->|   7    |
  +-----------+        +--------+
```

So `=` is **not** "equals". It is **assignment** — "make this name refer to
this value". It always works right-to-left:

```python
total = a + b
#       \_____/  (1) work out the right-hand side first
# \___/          (2) THEN point the name at the answer
```

This is why `total = total + 1` is legal and sensible: compute the old `total`
plus one, *then* re-point the name at the new value.

### Assignment vs comparison

| Symbol | Name | Means | Gives you |
|--------|------|-------|-----------|
| `=` | assignment | "store this here" | nothing, it's a statement |
| `==` | comparison | "is this the same as that?" | `True` or `False` |

Mixing these up is the single most common beginner error. `if x = 5:` is a
syntax error in Python — which is a kindness; in some languages it silently
compiles and ruins your afternoon.

### Naming rules and naming manners

**Rules** (break these and Python refuses to run):
- letters, digits and underscores only
- cannot start with a digit
- cannot be a keyword (`if`, `for`, `class`, `None`, ...)
- case-sensitive: `total`, `Total` and `TOTAL` are three different names

**Manners** (break these and humans refuse to read your code):
- `snake_case` for variables: `first_number`, `total_marks`
- names that say what the thing *is*: `average`, not `avg2`, not `x`
- never shadow a built-in: naming a variable `list`, `sum`, `input` or `str`
  breaks the real one for the rest of the program

> **Exam phrasing:** "an identifier is a name given to a variable, constant,
> function or other program element."

---

## 3. Data types

Every value has a type. The type decides what operations are legal.

| Type | Name in Python | Example | Holds |
|------|----------------|---------|-------|
| Integer | `int` | `42`, `-7`, `0` | whole numbers, no size limit in Python |
| Real / float | `float` | `3.14`, `-0.5`, `2.0` | numbers with a decimal point |
| String | `str` | `"hello"`, `"42"` | a sequence of characters |
| Boolean | `bool` | `True`, `False` | one of exactly two values |

`type(value)` tells you which one you have. Use it constantly while learning.

```python
type(42)      # <class 'int'>
type(42.0)    # <class 'float'>   <- the .0 makes it a different type!
type("42")    # <class 'str'>     <- digits in quotes are TEXT
```

### `"42"` is not `42`

This is the idea your snippet depends on completely.

```python
"42" + "7"    # '427'   <- + on strings JOINS them (concatenation)
 42  +  7     #  49     <- + on numbers ADDS them
"42" +  7     #  TypeError: can only concatenate str (not "int") to str
```

Same symbol, two completely different jobs, chosen by the *types* either side
of it. The error is Python refusing to guess which one you meant.

### Casting (type conversion)

| Call | Does | Example |
|------|------|---------|
| `int(x)` | → integer | `int("42")` → `42`, `int(3.9)` → `3` (**truncates**, no rounding) |
| `float(x)` | → float | `float("3.5")` → `3.5`, `float(7)` → `7.0` |
| `str(x)` | → string | `str(42)` → `"42"` |
| `bool(x)` | → boolean | `bool(0)` → `False`, `bool(1)` → `True` |

- **Explicit** casting is you writing `float(...)`. Also called *coercion*.
- **Implicit** casting is Python widening a type on its own, which it only
  does between numbers: `3 + 0.5` gives `3.5`, an `int` promoted to `float`.

`int(3.9)` is `3`, not `4`. It throws the fractional part away. If you want
rounding, use `round(3.9)` → `4`.

---

## 4. `input()` always hands you a string

```python
answer = input("Enter first number: ")
```

Two things to burn into memory:

1. `input()` **pauses** the program and waits for Enter.
2. `input()` **always returns a `str`** — always, even when the user typed
   digits. Even `7` comes back as `"7"`.

So this is broken:

```python
a = input("First: ")     # "10"
b = input("Second: ")    # "5"
print(a + b)             # 105   <- joined, not added!
```

and this is the fix:

```python
a = float(input("First: "))
```

Read the nesting from the **inside out**:

```python
a = float(input("Enter first number: "))
#                \_____________________/  (1) show prompt, wait, return "10"
#         \____________________________/   (2) convert "10" -> 10.0
#   \_______________________________/      (3) point `a` at 10.0
```

Inner brackets finish before outer brackets start. That rule explains most
nested code you will ever read.

### `int()` or `float()`?

- Counting things that cannot be fractional (people, lives, marks out of 10)?
  `int()`.
- Measuring, averaging, or anything involving money or decimals? `float()`.

Your snippet uses `float()` — correct, because an average of whole numbers is
very often *not* whole.

---

## 5. Arithmetic operators

| Operator | Name | `7` and `2` | Result type |
|----------|------|-------------|-------------|
| `+` | addition | `7 + 2` → `9` | int |
| `-` | subtraction | `7 - 2` → `5` | int |
| `*` | multiplication | `7 * 2` → `14` | int |
| `/` | **true** division | `7 / 2` → `3.5` | **always float** |
| `//` | **floor** division | `7 // 2` → `3` | int (if both are int) |
| `%` | modulo (remainder) | `7 % 2` → `1` | int |
| `**` | exponent | `7 ** 2` → `49` | int |

Three of these are exam favourites:

- `/` **always** produces a float. `6 / 2` is `3.0`, not `3`.
- `//` rounds **towards negative infinity**, not towards zero:
  `-7 // 2` is `-4`, not `-3`.
- `%` is how you test divisibility: `n % 2 == 0` means "n is even".
  It is also how you extract digits: `127 % 10` is `7`.

### Precedence (BIDMAS, essentially)

Highest to lowest:

```
()        brackets
**        exponent
-x        unary minus
* / // %  multiply and divide (left to right)
+ -       add and subtract (left to right)
```

So:

```python
a + b / 2        # b is halved FIRST, then a is added  -- usually a bug
(a + b) / 2      # the average -- what you actually meant
```

When in doubt, bracket it. Extra brackets cost nothing and are never marked
wrong.

---

## 6. Output

```python
print("The average is", avg)
```

`print` takes several arguments and inserts a space between each one. That is
why there is a space after "is" in the output even though you did not type one.

Three ways to build output, best last:

```python
print("Average: " + str(avg))      # concatenation - needs str(), clumsy
print("Average:", avg)             # comma - easy, but spacing is fixed
print(f"Average: {avg:.2f}")       # f-string - full control
```

An **f-string** is a string with `f` in front. Anything in `{curly braces}`
is evaluated and dropped in:

```python
name = "Ama"
score = 17.4567
print(f"{name} scored {score:.1f}")     # Ama scored 17.5
```

Format specifiers you will use:

| Spec | Means | `17.4567` becomes |
|------|-------|-------------------|
| `{x:.2f}` | 2 decimal places | `17.46` |
| `{x:.0f}` | whole number | `17` |
| `{x:8.2f}` | 2 d.p., right-aligned in 8 columns | `   17.46` |
| `{x:,}` | thousands separators | (on `1234567`) `1,234,567` |

---

## 7. Why your snippet is fragile

It runs. It gives the right answer. It is still a weak program, for four
reasons, and fixing them is the whole point of this unit.

| Weakness | What goes wrong | Fixed in |
|----------|-----------------|----------|
| Names `a` and `b` say nothing | unreadable the moment it grows | `02` |
| Hard-coded `2` | add a third number and the answer is silently wrong | `06` |
| Crashes on bad input | type "ten" and it dies with a traceback | `05` |
| Logic tangled with input/output | cannot be tested without a human typing | `07` |

That last one is the real lesson. A program that mixes "get the data",
"work out the answer" and "show the answer" into one lump can only ever be
tested by hand. Split them apart and the middle piece becomes a function you
can check automatically — which is exactly how `exercises.py` marks you.

The destination:

```python
def average(values):
    """Return the mean of a non-empty list of numbers."""
    total = 0
    for value in values:
        total = total + value
    return total / len(values)


def read_numbers(how_many):
    """Ask the user for `how_many` numbers and return them as a list."""
    numbers = []
    for index in range(how_many):
        numbers.append(read_float(f"Enter number {index + 1}: "))
    return numbers


if __name__ == "__main__":
    data = read_numbers(2)
    print(f"The average is {average(data):.2f}")
```

Longer? Yes. But it works for 2 numbers or 200, it survives a user typing
"banana", and `average` can be tested without typing anything at all.

---

## 8. Exam vocabulary

| Term | Definition to write in an exam |
|------|-------------------------------|
| **Variable** | A named storage location whose value can change during execution. |
| **Constant** | A named value that does not change during execution. |
| **Identifier** | The name given to a variable, constant, function or other element. |
| **Data type** | The classification of a value that determines which operations are valid on it. |
| **Casting / coercion** | Converting a value from one data type to another. |
| **Assignment** | Storing the result of an expression in a variable. |
| **Expression** | A combination of values, variables and operators that evaluates to a single value. |
| **Statement** | An instruction the interpreter can execute. |
| **Operator precedence** | The order in which operators are applied within an expression. |
| **Concatenation** | Joining two strings end to end. |
| **Validation** | Checking that input is acceptable before using it. |
| **Trace table** | A table showing the value of every variable after each line executes. |

### Trace tables

Expect to be handed code and asked to fill one in. For our snippet, with the
user typing `10` then `5`:

| Line | `a` | `b` | `total` | `avg` | Output |
|------|-----|-----|---------|-------|--------|
| 1 | `10.0` | — | — | — | `Enter first number: ` |
| 2 | `10.0` | `5.0` | — | — | `Enter second number: ` |
| 3 | `10.0` | `5.0` | `15.0` | — | |
| 4 | `10.0` | `5.0` | `15.0` | `7.5` | |
| 5 | `10.0` | `5.0` | `15.0` | `7.5` | `The average is 7.5` |

Rules: one row per line executed, a dash for "does not exist yet", and carry
unchanged values forward. Do this by hand — it is the fastest way to stop
*guessing* what code does and start *knowing*.

---

## Next

| Step | File | What you get |
|------|------|--------------|
| 1 | `01_trace_your_program.py` | your five lines, traced value by value |
| 2 | `02_variables_and_types.py` | types, casting, and the `"42"` vs `42` trap |
| 3 | `03_operators.py` | `/` vs `//` vs `%`, precedence, the average bug |
| 4 | `04_input_output.py` | prompts, f-strings, formatting to 2 d.p. |
| 5 | `05_safe_input.py` | `try`/`except` so "banana" cannot kill your program |
| 6 | `06_two_to_many.py` | 2 numbers → N numbers (and into the lists unit) |
| 7 | `07_functions.py` | splitting logic from I/O so it can be tested |
| 8 | `08_pitfalls.py` | the ten mistakes that cost marks |
| 9 | `exercises.py` | 14 tasks, self-marking |
| 10 | `quiz.md` | exam-style questions with a mark scheme |
