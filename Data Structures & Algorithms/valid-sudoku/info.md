LINK: <https://neetcode.io/problems/valid-sudoku/history>

## Bitwise solution explanation

The solution uses each integer as a compact set of digits. Each bit position represents whether a digit has appeared:

| Digit | Bit position | Value |
| --- | ---: | ---: |
| `1` | 0 | `1` (`000000001`) |
| `2` | 1 | `2` (`000000010`) |
| `3` | 2 | `4` (`000000100`) |
| `4` | 3 | `8` |
| ... | ... | ... |
| `9` | 8 | `256` |

```python
rows = [0] * 9
cols = [0] * 9
boxes = [0] * 9
```

Each position stores the digits already seen. For example, `rows[0]` stores the digits seen in row `0`. Initially every value is `0`, meaning no digits have been seen.

### Creating a bit for a digit

```python
bit = 1 << (int(val) - 1)
```

`<<` means shifting binary bits to the left. If `val == "3"`:

```python
int(val) - 1  # 2
1 << 2        # 4
```

In binary:

```text
1      = 000000001
1 << 2 = 000000100
```

The subtraction maps each digit to a bit position:

```text
digit 1 -> bit 0
digit 2 -> bit 1
digit 3 -> bit 2
...
digit 9 -> bit 8
```

### Checking whether a digit already exists

```python
if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
 return False
```

`&` is bitwise AND. It compares binary positions:

```text
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
```

Suppose a row has already seen digit `3`:

```text
rows[r] = 000000100
bit      = 000000100
```

Then `rows[r] & bit` is nonzero, which Python treats as `True`. If the row has not seen digit `3`, the result is `0`, which Python treats as `False`.

The condition checks whether the digit already exists in its row, column, or box.

### Recording a digit

```python
rows[r] |= bit
cols[c] |= bit
boxes[box_idx] |= bit
```

`|` is bitwise OR. It turns the digit's bit on without affecting the other bits.

For example, if a row has seen digits `1` and `3`, then we see digit `2`:

```text
000000101
| 000000010
-----------
000000111
```

Now the row records digits `1`, `2`, and `3`.

### Finding the 3-by-3 box

```python
box_idx = (r // 3) * 3 + (c // 3)
```

The boxes are numbered as follows:

```text
0 1 2
3 4 5
6 7 8
```

Integer division, `//`, determines which group of three a row or column belongs to. For cell `(r=4, c=7)`:

```python
r // 3  # 1
c // 3  # 2

box_idx = 1 * 3 + 2  # 5
```

So that cell belongs to box `5`.

### Overall flow

For every non-empty cell, the algorithm:

1. Converts its digit into one bit.
2. Finds its 3-by-3 box.
3. Checks whether the bit already exists in its row, column, or box.
4. Returns `False` if it does.
5. Otherwise, turns that bit on in all three places.
6. Returns `True` after processing the entire board.

A set-based solution may be easier to understand initially, but the bitwise solution stores the same information compactly in integers.

- Time: $O(81)$, effectively $O(1)$ for a fixed 9-by-9 board
- Space: $O(27)$ integers for 9 rows, 9 columns, and 9 boxes

If the file is run independently, the solution also needs this import:

```python
from typing import List
```
