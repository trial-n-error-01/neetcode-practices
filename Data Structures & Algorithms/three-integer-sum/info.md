# 3Sum

Problem: [Three Integer Sum](https://neetcode.io/problems/three-integer-sum/question)

Given an integer array `nums`, return every unique triplet whose values add up to
`0`. The three indices must be distinct, but the triplets and the output may be
returned in any order.

## Solution 1: Sort and use two pointers

This is the standard approach used in [submission-1.py](submission-1.py).

### How it works

1. Sort `nums` in ascending order.
2. Iterate through the array and treat `nums[i]` as the first value.
3. Set `left = i + 1` and `right = len(nums) - 1`.
4. Compare `nums[i] + nums[left] + nums[right]` with zero:
 - If the sum is too small, increment `left`.
 - If the sum is too large, decrement `right`.
 - If the sum is zero, save the triplet and move both pointers inward.
5. Skip equal values for `i`, `left`, and `right` so the result contains no
 duplicate triplets.

Sorting makes the pointer moves valid: increasing `left` can only increase the
sum, while decreasing `right` can only decrease it.

### Complexity

- Sorting: $O(n \log n)$
- Two-pointer search: $O(n^2)$
- Total time: $O(n^2)$
- Auxiliary space: $O(1)$ if the sort's internal memory is ignored; Python's
  in-place sort may use up to $O(n)$ auxiliary memory.
- The space required for the returned triplets is not included in auxiliary
  space.

## Solution 2: Hash set without sorting

This approach is implemented in [submission-2.py](submission-2.py).

### How it works

1. Choose each value as `val1` and skip repeated outer values.
2. For the values after `val1`, use a hash map to implement a two-sum search.
3. For each `val2`, calculate the required complement:

 ```text
 complement = -val1 - val2
 ```

4. If the complement has already been seen in the current inner loop, a valid
 triplet has been found.
5. Sort each discovered triplet before storing it in a result set. This makes
 different index orders, such as `[-1, 0, 1]` and `[0, -1, 1]`, count as the
 same triplet.

### Complexity

- Total time: $O(n^2)$
- Auxiliary space: $O(n)$ for the hash map, outer duplicate tracking, and
  result set, excluding the returned list itself.

This solution is valid, but sorting plus two pointers is usually preferred
because duplicate handling is simpler and it uses less extra bookkeeping.

## Key edge cases

- `[-1, 0, 1, 2, -1, -4]` returns `[[-1, -1, 2], [-1, 0, 1]]`.
- `[0, 1, 1]` returns `[]`.
- `[0, 0, 0]` returns `[[0, 0, 0]]`.
