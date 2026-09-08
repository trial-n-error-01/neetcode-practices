---

## Complexity note: balanced binary tree

The DFS-based solution in `Data Structures & Algorithms/balanced-binary-tree/submission-0.py` is linear on a tree.

- Time complexity: O(n)
- Space complexity: O(h), where `h` is the height of the tree
  - worst case: O(n) for a skewed tree
  - balanced tree: O(log n)

Why this is still O(V + E): a binary tree has `V = n` nodes and `E = n - 1` edges, so:

`O(V + E) = O(n + (n - 1)) = O(n)`

This is the standard DFS time bound for a tree, and each node is processed once.
