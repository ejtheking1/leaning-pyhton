# A1.1 — exam-style questions

Answer on paper first. Mark yourself afterwards. The marks in brackets show how
many separate points the examiner is looking for — if your answer has fewer
sentences than that, it is too short.

Trace-table questions are worth doing *on paper*, properly, in columns. It is
slow the first three times and then it is fast forever.

---

### 1. Define the terms **variable** and **data type**. **[2]**

### 2. State the data type of each of the following Python values. **[4]**
a) `42`
b) `42.0`
c) `"42"`
d) `True`

### 3. A student writes the following, intending to add two numbers.
```python
first = input("First: ")
second = input("Second: ")
print(first + second)
```
a) State the output if the user enters `10` and `5`. **[1]**
b) Explain why this output occurs. **[2]**
c) Correct the code. **[1]**

### 4. Distinguish between the operators `=` and `==`. **[2]**

### 5. State the value and data type of each expression. **[6]**
a) `7 / 2`
b) `7 // 2`
c) `7 % 2`
d) `6 / 3`
e) `2 ** 3 ** 2`
f) `-7 // 2`

### 6. Consider this code.
```python
first = 10
second = 4
result = first + second / 2
```
a) State the value of `result`. **[1]**
b) The programmer intended to calculate the average. Identify the error and
   correct it. **[2]**
c) Explain why this error is harder to find than a syntax error. **[2]**

### 7. Construct a trace table for the following program when the user enters
`8` and then `3`. **[5]**
```python
1  a = float(input("Enter first number: "))
2  b = float(input("Enter second number: "))
3  total = a + b
4  avg = total / 2
5  print("The average is", avg)
```

### 8. Explain why `int("3.5")` raises an error but `float("3.5")` does not. **[2]**

### 9. A program asks the user for a test mark out of 50.
a) State **two** kinds of invalid input the program should reject. **[2]**
b) Construct a Python function `read_mark()` that keeps asking until the user
   enters a valid mark, then returns it. **[5]**

### 10. Explain the difference between `round(x, 2)` and `f"{x:.2f}"`, and state
when each should be used. **[3]**

### 11. A student's program averages three numbers.
```python
total = first + second + third
average = total / 2
```
a) State the error. **[1]**
b) Explain why the program produces no error message. **[2]**
c) State a general rule that would have prevented this mistake. **[2]**

### 12. Consider this attempt to total a list.
```python
total = 0
for value in [3, 7, 11]:
    total = value
print(total)
```
a) State the output. **[1]**
b) Identify and correct the error. **[2]**

### 13. Explain why the expression `0.1 + 0.2 == 0.3` evaluates to `False`, and
state how a programmer should compare two floating-point values. **[4]**

### 14. A program calculates the average of a list of numbers entered by a user.
a) Explain why the program must check the number of values before dividing. **[2]**
b) State what the program should do if no values were entered, and justify
   your choice. **[2]**

### 15. Distinguish between **return** and **print** in a Python function, and
explain why a function that calculates a value should return it. **[4]**

### 16. Construct a Python function `average(values)` that returns the mean of a
list of numbers, or `None` if the list is empty. You may not use `sum()` or
`len()`. **[6]**

---
---

# Mark scheme

Award marks for any valid equivalent wording.

### 1. **[2]**
- **Variable:** a named storage location in memory whose value can change
  during program execution. **[1]**
- **Data type:** the classification of a value that determines which operations
  may be performed on it / how it is stored in memory. **[1]**

### 2. **[4]**
a) integer / `int` **[1]**
b) real / `float` **[1]**
c) string / `str` **[1]**
d) Boolean / `bool` **[1]**

### 3. **[4]**
a) `105` **[1]**
b) `input()` always returns a string **[1]**; the `+` operator applied to two
   strings performs concatenation rather than addition, so `"10"` and `"5"` are
   joined **[1]**.
c) `print(float(first) + float(second))`, or cast at the point of input:
   `first = float(input("First: "))` **[1]**

### 4. **[2]**
- `=` is the assignment operator: it stores the value of the expression on its
  right in the variable on its left. **[1]**
- `==` is the equality operator: it compares two values and evaluates to `True`
  or `False`. **[1]**

### 5. **[6]** (value and type both needed for the mark)
a) `3.5`, float **[1]**
b) `3`, int **[1]**
c) `1`, int **[1]**
d) `2.0`, float — `/` always returns a float **[1]**
e) `512`, int — `**` groups right to left, so `2 ** (3 ** 2)` **[1]**
f) `-4`, int — `//` rounds towards negative infinity, not towards zero **[1]**

### 6. **[5]**
a) `12.0` **[1]**
b) `/` has higher precedence than `+`, so `second / 2` is evaluated first
   **[1]**; correct to `result = (first + second) / 2` **[1]**
c) It is a logic (semantic) error, not a syntax error, so the program runs
   without any error message **[1]**; the output is a plausible-looking number,
   so the fault may go unnoticed unless the code is traced or tested with known
   values **[1]**

### 7. **[5]** — one mark per correct row
| Line | `a` | `b` | `total` | `avg` | Output |
|------|-----|-----|---------|-------|--------|
| 1 | `8.0` | — | — | — | `Enter first number: ` |
| 2 | `8.0` | `3.0` | — | — | `Enter second number: ` |
| 3 | `8.0` | `3.0` | `11.0` | — | |
| 4 | `8.0` | `3.0` | `11.0` | `5.5` | |
| 5 | `8.0` | `3.0` | `11.0` | `5.5` | `The average is 5.5` |

Accept `8` / `3` for the values provided the candidate has elsewhere shown that
`float()` produces a real number. Deduct if `avg` is given as `5` (integer
division has not been applied here).

### 8. **[2]**
- `int()` parses only a whole-number literal; the character `.` is not valid in
  one, so `"3.5"` raises a `ValueError`. **[1]**
- `float()` parses a real-number literal, for which a decimal point is valid.
  **[1]**

*(Accept: to convert such a string to an integer you must cast twice —
`int(float("3.5"))` — which truncates to `3`.)*

### 9. **[7]**
a) Any two of: non-numeric text (`"ten"`); an empty entry; a negative number; a
   number greater than 50; a number with a comma as the decimal separator.
   **[2]**

b) **[5]**
```python
def read_mark():
    """Ask until the user enters a mark from 0 to 50, then return it."""
    while True:                                      # [1] loop that repeats
        text = input("Mark out of 50: ")
        try:                                         # [1] try/except
            mark = float(text)
        except ValueError:
            print("That is not a number.")
            continue
        if 0 <= mark <= 50:                          # [1] range check
            return mark                              # [1] returns the value
        print("Enter a mark from 0 to 50.")          # [1] useful message
```
Award the marks for: a loop that repeats on invalid input; exception handling
around the conversion; a range check as well as a type check; returning the
valid value; informing the user what was wrong.

### 10. **[3]**
- `round(x, 2)` returns a new **number** rounded to two decimal places. **[1]**
- `f"{x:.2f}"` returns a **string** formatted to two decimal places; the
  underlying value is unchanged. **[1]**
- Use `round()` when the rounded value is needed in further calculations; use
  the format specifier for display only, so that full precision is retained for
  any later arithmetic. **[1]**

### 11. **[5]**
a) The divisor should be `3`, not `2` — or better, the number of values. **[1]**
b) It is a logic error: the expression is syntactically valid and the division
   is legal **[1]**, so the interpreter has no way to know that `2` is the wrong
   divisor and simply outputs a wrong but plausible result **[1]**.
c) Do not store the same fact in two places / never hard-code a count that is
   already determined by the data **[1]**; derive it instead, e.g.
   `average = total / len(numbers)` **[1]**.

### 12. **[3]**
a) `11` **[1]**
b) `total = value` overwrites the accumulator instead of adding to it **[1]**;
   correct to `total = total + value` (or `total += value`) **[1]**.

### 13. **[4]**
- Floating-point values are stored in binary with a fixed number of bits. **[1]**
- `0.1` and `0.2` have no exact representation in binary, so each is stored as a
  very close approximation. **[1]**
- The sum of the two approximations is `0.30000000000000004`, which is not
  identical to the stored value of `0.3`, so `==` is `False`. **[1]**
- Compare the absolute difference against a small tolerance instead, e.g.
  `abs(a - b) < 1e-9`. **[1]**

### 14. **[4]**
a) If the list is empty the divisor is zero **[1]**, which raises a
   `ZeroDivisionError` and terminates the program **[1]**.
b) Output a message such as "no values entered" / return `None` **[1]**, because
   the mean of an empty set is undefined — returning `0` would be misleading, as
   it asserts that the average is zero **[1]**.

### 15. **[4]**
- `print()` writes a value to the screen for a human to read; it does not make
  the value available to the rest of the program. **[1]**
- `return` sends a value back to the calling code, where it can be stored,
  tested or used in further calculations. **[1]**
- A function with no `return` statement returns `None`. **[1]**
- A function that returns its result separates calculation from input/output, so
  it can be re-used and tested automatically without user interaction. **[1]**

### 16. **[6]**
```python
def average(values):
    """Return the mean of values, or None if values is empty."""
    count = 0                         # [1] two accumulators initialised
    total = 0
    for value in values:              # [1] traverses every element
        total = total + value         # [1] accumulates the total correctly
        count = count + 1             # [1] counts the elements
    if count == 0:                    # [1] guards the empty case
        return None
    return total / count              # [1] returns the mean using true division
```
Award: both accumulators initialised before the loop; a loop visiting every
element; correct accumulation of the total; correct counting; an empty-list
guard; a correct returned mean using `/` rather than `//`.

Accept the guard placed before the loop using a separate emptiness test, and
accept `+=` shorthand throughout.

---

## How to use your score

Total available: **66 marks**.

| Score | What to do next |
|-------|-----------------|
| Under 30 / 66 | Re-read `00_notes.md`, then redo `01` to `03`. Do not skip the trace table. |
| 30-48 / 66 | Rerun the lesson files covering whatever you dropped marks on, then redo this quiz. |
| Over 48 / 66 | Finish `exercises.py` if you have not, then move on to `b2_2_lists_and_arrays/`. |

Questions you should be able to answer without hesitating, because they turn up
in some form every single year:

- what `input()` returns, and why `float()` is needed
- the difference between `/`, `//` and `%`
- why `first + second / 2` is not the average
- what a trace table looks like
- why dividing by a count means checking that count first
