import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def log_tree(root):
    if root is None:
        logging.debug("None")
        return

    levels = {}
    node_positions = {}
    next_position = 0
    spacing = max(3, max(len(str(node.val)) for node in [root]))

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

        node_positions[node] = position
        levels.setdefault(depth, []).append(node)
        return position

    assign_position(root)
    max_position = max(node_positions.values())

    for depth in sorted(levels):
        level = levels[depth]
        value_line = [" "] * (max_position + spacing)
        for node in level:
            value = str(node.val)
            position = node_positions[node]
            start = max(0, position - len(value) // 2)
            value_line[start:start + len(value)] = value
        logging.debug("".join(value_line).rstrip())

        if depth == max(levels):
            continue

        branch_line = [" "] * (max_position + spacing)
        for node in level:
            parent_position = node_positions[node]
            for child, branch in ((node.left, "/"), (node.right, "\\")):
                if child is None:
                    continue
                child_position = node_positions[child]
                if child_position == parent_position:
                    branch_line[parent_position] = "|"
                else:
                    branch_position = (parent_position + child_position) // 2
                    branch_line[branch_position] = branch
        logging.debug("".join(branch_line).rstrip())


class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node, depth=0):
            nonlocal diameter

            indent = "  " * depth

            if node is None:
                logging.debug(f"{indent}None -> height 0")
                return 0

            logging.debug(f"{indent}Entering node {node.val}")

            left_height = height(node.left, depth + 1)
            right_height = height(node.right, depth + 1)

            path_through_node = left_height + right_height

            logging.debug(
                f"{indent}Node {node.val}: "
                f"left height = {left_height}, "
                f"right height = {right_height}, "
                f"path = {path_through_node}"
            )

            if path_through_node > diameter:
                diameter = path_through_node
                logging.debug(
                    f"{indent}Updated diameter to {diameter}"
                )

            node_height = 1 + max(left_height, right_height)

            logging.debug(
                f"{indent}Leaving node {node.val}: "
                f"height = {node_height}"
            )

            return node_height

        height(root)

        logging.debug(f"Final diameter: {diameter}")
        return diameter


root = TreeNode(
    1,
    right=TreeNode(
        2,
        left=TreeNode(3),
        right=TreeNode(4),
    ),
)

logging.debug("Tree before diameter processing:")
log_tree(root)
result = Solution().diameterOfBinaryTree(root)
print(f"Diameter: {result}")


root_without_root_diameter = TreeNode(
    1,
    left=TreeNode(
        2,
        left=TreeNode(3, left=TreeNode(4, left=TreeNode(5))),
        right=TreeNode(6, right=TreeNode(7, right=TreeNode(8))),
    ),
)

logging.debug("Tree before diameter processing:")
log_tree(root_without_root_diameter)
result = Solution().diameterOfBinaryTree(root_without_root_diameter)
print(f"Diameter without root: {result}")