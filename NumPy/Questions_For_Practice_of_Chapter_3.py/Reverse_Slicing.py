'''
Reverse slicing

arr2 = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

Using arr2, extract the last two rows and first three columns.

Expected:

[[110, 120, 130],
 [160, 170, 180]]

This tests whether you understand negative step slicing.

'''

import numpy as np

arr2 = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])


print(arr2[2:, [0,1,2] ])

result = arr2[-1:-3:-1, [0,1,2]]
print(result[::-1])

print(arr2[-1:-3:-1, [0,1,2]][::-1])  # a more shorter version


'''
## Negative Step Slicing with 2D Arrays

For a 2D NumPy array, slicing follows this structure:

```python
array[row_slicing, column_slicing]
```

### Example:

```python
print(arr2[-1:-3:-1, [0,1,2]][::-1])
```

Let's break this into two parts.

### Part 1: `arr2[-1:-3:-1, [0,1,2]]`

```python
arr2[-1:-3:-1, [0,1,2]]
```

The first part is:

```python
-1:-3:-1
```

This is row slicing.

* `-1` → start from the last row
* `-3` → stop before the row represented by `-3`
* `-1` → move backward by 1 row

Therefore, the rows are selected in this order:

```text
Row 3 → Row 2
```

The second part is:

```python
[0,1,2]
```

This selects columns 0, 1, and 2.

So the first operation gives:

```text
[[160, 170, 180],
 [110, 120, 130]]
```

Notice that the rows are in reverse order.

---

### Part 2: `[::-1]`

After selecting the rows, we apply:

```python
[::-1]
```

This means:

* start → automatically from the end
* stop → automatically at the beginning
* step `-1` → move backward

In simple words:

> `[::-1]` reverses the selected array.

So:

```text
Before:

Row 3
Row 2

After [::-1]:

Row 2
Row 3
```

The final result becomes:

```text
[[110, 120, 130],
 [160, 170, 180]]
```

### Complete expression

```python
arr2[-1:-3:-1, [0,1,2]][::-1]
```

Think of it as:

```text
First:
Select rows 3 → 2
and columns 0, 1, 2

Then:
Reverse the result

Final:
Rows 2 → 3
```

### Important Rule

```python
[start : stop : step]
```

* Positive step → move forward
* Negative step → move backward
* `[::-1]` → reverse the array

Also remember:

> In `[-1:-3:-1]`, the first two `-1` and `-3` are indices, while the final `-1` is the step.


'''