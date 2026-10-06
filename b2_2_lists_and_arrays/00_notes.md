# B2.2 Data structures — arrays and lists

> Scope note: B2.2 of the new IB CS guide breaks down into
> **B2.2.1** comparing *static* and *dynamic* data structures,
> **B2.2.2** constructing programs that apply **arrays and lists**, and
> **B2.2.3** stacks and queues (LIFO / FIFO).
> This unit is B2.2.2, plus the B2.2.1 theory you need to answer the
> "compare and contrast" questions. Always check the wording in your own
> teacher's copy of the guide — that is the authority, not these notes.

---

## 1. The one idea behind the whole topic

A **data structure** is a way of organising many values so that a program can
store them under one name and reach any of them quickly.

Before data structures:

```python
mark1 = 65
mark2 = 72
mark3 = 48     # ...and 27 more? This does not scale.
```

After:

```python
marks = [65, 72, 48]   # one name, many values, reachable by position
```

The moment data lives in one structure, you can **loop** over it. That is the
real payoff: one algorithm handles 3 values or 3000 values without changing.

---

## 2. Array vs list — the distinction IB wants

These two words are used loosely in everyday programming, but in the exam they
mean different things.

| | **Array** (static) | **List** (dynamic) |
|---|---|---|
| Size | Fixed when created | Grows and shrinks at run time |
| Memory | One **contiguous** block, allocated once | Allocated as needed; may be scattered |
| Elements | Usually all the **same data type** | Can be mixed types |
| Access by index | O(1) — direct address arithmetic | O(1) in Python lists; O(n) in a linked list |
| Insert / delete in middle | Expensive — must shuffle elements | Cheaper in a linked list; still a shuffle in a Python list |
| Memory waste | Can over-allocate and waste, or run out | Uses only what it needs, plus pointer overhead |
| Typical use | Known, unchanging quantity (board of a game, pixels, days of week) | Unknown quantity (readings from a sensor, user's shopping basket) |

**How an array gets O(1) access.** If the array starts at memory address 1000
and each element takes 4 bytes, then element `i` sits at `1000 + 4 * i`. The
computer does one multiplication and one addition — the cost does not depend on
how big the array is, or how far in you reach. That is *why* arrays must be
contiguous and fixed-type.

**Exam phrasing to memorise:**
- Static structure → *size is determined at compile time / when declared and
  cannot change; memory is allocated in one contiguous block.*
- Dynamic structure → *size can change during execution; memory is allocated
  and released as the program runs.*
- Trade-off → *static is faster and has no pointer overhead, but inflexible and
  may waste memory; dynamic is flexible but uses extra memory for
  pointers/bookkeeping and may be slower to access.*

---

## 3. Where Python sits

Python has **no built-in static array**. `list` is a dynamic structure.

So in Python you will:
- use `list` for anything dynamic (nearly everything), **and**
- *discipline yourself* to treat a list as fixed-size when the question is
  really about an array — create it full of placeholders and never append.
  `03_static_arrays.py` shows exactly how.

(There is also `array.array` in the standard library, which is a real
single-type contiguous array, but it still resizes, and IB will not require it.
Mentioning it in an essay is fine; relying on it is not.)

---

## 4. Indexing — the rule everything depends on

```
marks  =  [ 65 , 72 , 48 , 91 , 55 ]
index      0    1    2    3    4        <- forwards, starts at ZERO
index     -5   -4   -3   -2   -1        <- Python-only, counts backwards
```

- First element: `marks[0]`
- Last element: `marks[len(marks) - 1]`, or in Python `marks[-1]`
- `len(marks)` is **5**, but the biggest valid index is **4**.
  That gap is the source of the single most common bug in this whole topic:
  the **off-by-one error**.
- A valid index for a list of length *n* satisfies `0 <= index <= n - 1`.
  Anything else raises `IndexError`.

In IB pseudocode you will see the same thing written as:

```
loop I from 0 to MARKS.length - 1
    output MARKS[I]
end loop
```

---

## 5. The operations you must be able to use

On a Python list `L`:

| Need | Code | Note |
|---|---|---|
| length | `len(L)` | not a method |
| read element | `L[i]` | |
| overwrite element | `L[i] = v` | size unchanged — an *array-safe* operation |
| add to end | `L.append(v)` | **dynamic only** |
| insert at position | `L.insert(i, v)` | shifts everything right |
| remove by position | `L.pop(i)` / `del L[i]` | returns the value / doesn't |
| remove by value | `L.remove(v)` | first occurrence only |
| is value present | `v in L` | returns `True`/`False` |
| position of value | `L.index(v)` | raises `ValueError` if absent |
| how many times | `L.count(v)` | |
| sort in place | `L.sort()` | changes `L`, returns `None` |
| sorted copy | `sorted(L)` | leaves `L` alone |
| reverse in place | `L.reverse()` | |
| slice (sub-list copy) | `L[a:b]` | includes `a`, **excludes** `b` |
| join two | `L + M` | new list |
| repeat | `[0] * 5` | `[0, 0, 0, 0, 0]` |

### Built-ins vs writing the algorithm yourself

`sum(L)`, `max(L)`, `min(L)`, `sorted(L)` exist and are fine in your IA or
Paper-2-style code. **But** exam questions often say *"construct an algorithm
to find the largest value"* — there, calling `max()` answers nothing and earns
nothing. You must be able to write the loop. `02_traversal_patterns.py` drills
all of them.

---

## 6. Two-dimensional arrays

A 2-D array is "an array whose elements are arrays". It models anything laid out
in a grid: a seating plan, a noughts-and-crosses board, a spreadsheet, a class's
marks across several tests.

```python
grid = [
    [1, 2, 3],     # row 0
    [4, 5, 6],     # row 1
]
grid[1][2]   # -> 6     row FIRST, then column
```

- `len(grid)` → number of **rows** (2)
- `len(grid[0])` → number of **columns** (3)
- Walking the whole thing needs **nested loops**: outer over rows, inner over
  columns.
- Real 2-D arrays are stored in memory in **row-major order** —
  `[1, 2, 3, 4, 5, 6]` laid end to end — and the address of `grid[r][c]` is
  `base + (r * number_of_columns + c) * element_size`. That formula is worth
  knowing; it shows you understand *why* a 2-D array needs equal-length rows.

`grid[row][col]` — say "row, column" out loud every time. Swapping them is the
second most common bug in this topic.

---

## 7. Choosing the right structure in an exam answer

If a question asks you to justify a structure, say **what changes**:

- *Fixed, known size, speed matters, all one type* → **array**.
  (chess board, 24 hourly temperatures, RGB pixels)
- *Size unknown or changing* → **list**.
  (log of events, queue of orders, students who signed up)
- *Add/remove only at one end, last-in-first-out* → **stack** (B2.2.3).
- *Add at back, remove from front, first-in-first-out* → **queue** (B2.2.3).

A good answer names the structure, gives one property of it, and ties that
property to the scenario. "A list, because the number of sensor readings is not
known before the program runs and a list can grow during execution" — three
marks' worth of sentence.

---

## 8. Vocabulary checklist

element · index · traverse · iterate · static · dynamic · contiguous ·
allocate · bounds · off-by-one · one-dimensional · two-dimensional ·
row-major · linear search · aliasing · mutate · in place · nested loop

If you cannot define one of those in a sentence, go back and find it above.
