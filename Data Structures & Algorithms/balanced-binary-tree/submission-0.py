class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(node):
            if node is None:
                print("Checking node=None -> returning height 0")
                return 0

            print(f"Checking node={node.val}")

            left_height = dfs(node.left)
            if left_height == -1:
                print(f"Node={node.val}: left subtree unbalanced -> returning -1")
                return -1

            right_height = dfs(node.right)
            if right_height == -1:
                print(f"Node={node.val}: right subtree unbalanced -> returning -1")
                return -1

            print(
                f"Node={node.val}: "
                f"left_height={left_height}, "
                f"right_height={right_height}"
            )

            if abs(left_height - right_height) > 1:
                print(f"Node={node.val}: difference too large -> returning -1")
                return -1

            height = 1 + max(left_height, right_height)
            print(f"Node={node.val}: balanced -> returning height {height}")
            return height

        result = dfs(root) != -1
        print(f"Final result: {result}")
        return result