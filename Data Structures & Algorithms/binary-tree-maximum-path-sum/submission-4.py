# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")

        def dfs(node):
            nonlocal maxPath

            if(node== None):
                return 0

            
            
            leftPathForNode = max(0,dfs(node.left))
            rightPathForNode= max(0, dfs(node.right))

            passViaNode= node.val+leftPathForNode + rightPathForNode
            

            maxPath = max(maxPath, passViaNode)

            return node.val + max(leftPathForNode, rightPathForNode)

        dfs(root)
        return maxPath