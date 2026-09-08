# Longest Consecutive Sequence

## Problem

[NeetCode submission history](https://neetcode.io/problems/longest-consecutive-sequence/history?submissionIndex=1)

## Complexity

- **Time:** $O(N)$ average, where $N = \text{len(nums)}$.
- **Space:** $O(N)$ for the set of numbers.

Although the algorithm contains a nested `while` loop, each number is visited at most once while counting sequences. Set lookups are assumed to be $O(1)$ on average.
