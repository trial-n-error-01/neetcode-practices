import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def log_tree(root):
    if root is None:
        logging.debug("Generated input tree: None")
        return

    levels = {}
    positions = {}
    next_position = 0
    spacing = 4

    def assign_position(node, depth=0):
        nonlocal next_position

        if node is None:
            return None

        left_position = assign_position(node.left, depth + 1)
        right_position = assign_position(node.right, depth + 1)

        if left_position is not None and right_position is not None:
            position = (left_position + right_position) // 2
        elif left_position is not None:
            position = left_position
        elif right_position is not None:
            position = right_position
        else:
            position = next_position
            next_position += spacing

        positions[node] = position
        levels.setdefault(depth, []).append(node)
        return position

    assign_position(root)
    width = max(positions.values()) + spacing + 1
    lines = []

    for depth in sorted(levels):
        value_line = [" "] * width
        for node in levels[depth]:
            value = str(node.val)
            start = max(0, positions[node] - len(value) // 2)
            value_line[start:start + len(value)] = value
        lines.append("".join(value_line).rstrip())

        if depth == max(levels):
            continue

        branch_line = [" "] * width
        for node in levels[depth]:
            parent_position = positions[node]
            for child, branch in ((node.left, "/"), (node.right, "\\")):
                if child is None:
                    continue
                child_position = positions[child]
                branch_position = (parent_position + child_position) // 2
                branch_line[branch_position] = branch
        lines.append("".join(branch_line).rstrip())

    logging.debug("Generated input tree:\n" + "\n".join(lines))

class Solution:
    def maxPathSum(self,root):
        maxPath = float("-inf")

        def dfs(node):
            nonlocal maxPath

            if node is None:
                logging.debug("Checking node=None -> returning path 0")
                return 0

            logging.debug(f"Checking node={node.val}")
            leftPathForNode = max(0, dfs(node.left))
            rightPathForNode = max(0, dfs(node.right))
            pathThroughNode = node.val + leftPathForNode + rightPathForNode
            maxPath = max(maxPath, pathThroughNode)

            logging.debug(
                f"Node={node.val}: left_path={leftPathForNode}, "
                f"right_path={rightPathForNode}, "
                f"path_through_node={pathThroughNode} -> "
                f"returning path {node.val + max(leftPathForNode, rightPathForNode)}"
            )
            return node.val + max(leftPathForNode, rightPathForNode)

        
          
            
        dfs(root)
        logging.debug(f"Final path result: {maxPath}")
        return maxPath

root = TreeNode(
    -15,
    left=TreeNode(10),
    right=TreeNode(
        20,
        left=TreeNode(
            15, 
            left=TreeNode(-5),
            ),
        right=TreeNode(5),
    ),
)
log_tree(root)
result = Solution().maxPathSum(root)
print(f"Path: {result}")

