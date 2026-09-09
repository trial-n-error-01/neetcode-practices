class Solution:
# worse time performance of 3
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    stack = [root]
    while stack:
      node = stack.pop()
      # Swap children
      node.left, node.right = node.right, node.left

      if node.left:
        stack.append(node.left)
      if node.right:
        stack.append(node.right)

    return root