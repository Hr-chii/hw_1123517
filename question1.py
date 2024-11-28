#Your Name:Callie
#Student ID:1123517
#Date of Submission:2024/11/28

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_order):
    from collections import deque
    if not level_order or level_order[0] == -1:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if level_order[i] != -1:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] != -1:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter

level_order = [1, 2, -1, 3, -1, -1, -1]
root = build_tree(level_order)
print(diameter_of_binary_tree(root))  # 2

