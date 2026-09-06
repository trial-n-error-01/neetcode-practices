# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxPath = 0

        def dfs(root):
            nonlocal maxPath
            if(root is None):
                return 0
            
            leftDia = dfs(root.left)
            rightDia = dfs(root.right)

            nodeDia = max(leftDia,rightDia)+1

            maxPath = max(maxPath, leftDia+rightDia)
            return nodeDia
        
        dfs(root)
        return maxPath
            
        