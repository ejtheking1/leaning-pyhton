# B2.2 — exam-style questions

Answer on paper first. Mark yourself afterwards. The marks in brackets show how
many separate points the examiner is looking for — if your answer has fewer
sentences than that, it is too short.

---

### 1. Distinguish between a static and a dynamic data structure. **[4]**

### 2. A program records the temperature every hour for one day. Another records every goal scored in a football season. State which structure suits each and justify your choice. **[4]**

### 3. The array `VALUES` holds `[12, 7, 19, 3]`.
a) State the value of `VALUES[2]`. **[1]**
b) State the value of `VALUES.length`. **[1]**
c) Explain why `VALUES[4]` causes an error. **[2]**

### 4. Construct an algorithm, in pseudocode or Python, that outputs the largest value in an array `NUMBERS`. You may not use a built-in maximum function. **[4]**

### 5. Explain why a linear search on an array of *n* elements has worst-case efficiency O(n), while reading `ARR[i]` is O(1). **[4]**

### 6. A 2-D array `SEATS` has 10 rows and 6 columns.
a) State how many elements it holds. **[1]**
b) State the index of the seat in the last row, last column. **[1]**
c) Construct an algorithm to count how many elements equal `"FREE"`. **[4]**

### 7. Identify the error in this code and state its output.
```python
numbers = [10, 20, 30]
for i in range(1, len(numbers)):
    print(numbers[i])
```
**[2]**

### 8. Explain, with reference to memory, why inserting an element into the middle of an array is more expensive than appending to the end. **[3]**

### 9. A student writes `copy = original` intending to make a backup of a list, then modifies `copy`. Explain what actually happens and give a correct alternative. **[3]**

### 10. Outline one advantage and one disadvantage of using a 2-D array rather than several separate 1-D arrays to store one class's marks in three tests. **[4]**

---
---

# Mark scheme

### 1. Static vs dynamic **[4]**
- Static: size is fixed when the structure is declared and cannot change during execution. **[1]**
- Static: memory is allocated as a single contiguous block, so access by index is fast and there is no pointer overhead; but unused slots waste memory and it can overflow. **[1]**
- Dynamic: size can grow and shrink while the program runs. **[1]**
- Dynamic: memory is allocated and released as needed, so it adapts to the amount of data; but it uses extra memory for bookkeeping/pointers and resizing takes time. **[1]**

### 2. Choosing a structure **[4]**
- Temperatures: an **array**, **[1]** because the number of readings is known in advance and fixed (24), so a fixed-size structure is sufficient and gives fast indexed access. **[1]**
- Goals: a **list**, **[1]** because the number of goals in a season is not known before the program runs, so the structure must be able to grow during execution. **[1]**

### 3. Indexing **[4]**
a) 19 **[1]**
b) 4 **[1]**
c) Indexing starts at 0, so the valid indices are 0 to 3. **[1]** Index 4 is outside the bounds of the array, so there is no such element and the program raises an out-of-bounds / `IndexError`. **[1]**

### 4. Largest value **[4]**
```
LARGEST = NUMBERS[0]                      // seed with the first element  [1]
loop I from 1 to NUMBERS.length - 1       // correct bounds               [1]
    if NUMBERS[I] > LARGEST then          // comparison                   [1]
        LARGEST = NUMBERS[I]
    end if
end loop
output LARGEST                            // output AFTER the loop        [1]
```
Mark allocation: seeding with element 0 (not 0), correct loop bounds, correct comparison, output after the loop. Starting `LARGEST = 0` loses the first mark because it fails for all-negative data.

### 5. Efficiency **[4]**
- Linear search examines elements one at a time from the start. **[1]**
- In the worst case (target last, or absent) it examines all *n* elements, so the number of operations grows in proportion to *n* → O(n). **[1]**
- Indexed access computes the element's address arithmetically: `base + i × element_size`. **[1]**
- That is a fixed number of operations regardless of *n* or of the value of *i*, so it is O(1) — constant time. **[1]**

### 6. 2-D array **[6]**
a) 10 × 6 = 60 **[1]**
b) `SEATS[9][5]` **[1]**
c)
```
COUNT = 0                                 // counter outside both loops   [1]
loop R from 0 to 9                        // outer loop over rows         [1]
    loop C from 0 to 5                    // inner loop over columns      [1]
        if SEATS[R][C] == "FREE" then
            COUNT = COUNT + 1             // conditional increment        [1]
        end if
    end loop
end loop
output COUNT
```

### 7. Error and output **[2]**
- The loop starts at index 1 instead of 0, so the first element is skipped — an off-by-one error. **[1]**
- Output: `20` then `30`. **[1]**

### 8. Insert vs append **[3]**
- An array occupies a contiguous block, and each element's position determines its address. **[1]**
- Inserting in the middle requires every element after the insertion point to be shifted one place along to make room. **[1]**
- That is up to *n* move operations → O(n), whereas appending writes a single element into the next free slot → O(1). **[1]**

### 9. Aliasing **[3]**
- `copy = original` copies the **reference**, not the data, so both names refer to the same list object in memory. **[1]**
- Modifying `copy` therefore also changes `original` — there is no backup. **[1]**
- A correct alternative: `copy = original[:]` (or `list(original)` / `original.copy()`), which creates a new list containing the same elements. For a 2-D array each row must also be copied. **[1]**

### 10. 2-D vs several 1-D arrays **[4]**
Advantage (any one, **[2]**):
- All the data is under one name, so the same nested loop handles any number of tests; adding a fourth test means changing a size, not adding a new variable and new code.

Disadvantage (any one, **[2]**):
- The code is harder to read and more error-prone — `marks[r][c]` gives no hint which index is which, and swapping them produces a wrong answer with no error message; it also forces every row to be the same length and every value to be the same kind of thing.

---

## Self-assessment

| Total | Where you are |
|---|---|
| 34–38 | Secure. Move on to B2.2.3 (stacks and queues). |
| 26–33 | Solid. Re-read the mark scheme wording and redo questions 4 and 6c from memory. |
| 17–25 | Re-run `02_traversal_patterns.py` and `04_two_dimensional.py`, then redo the whole quiz. |
| under 17 | Go back to `00_notes.md` §2 and §4, then do `exercises.py` 1–9 before trying again. |

Maximum: 38 marks.
