# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = [(root, 1)]
        while queue:
            node, node_depth = queue.pop(0)
            if node_depth == depth - 1:
                left_child = TreeNode(val)
                right_child = TreeNode(val)
                left_child.left = node.left
                right_child.right = node.right
                node.left = left_child
                node.right = right_child
            else:
                if node.left:
                    queue.append((node.left, node_depth + 1))
                if node.right:
                    queue.append((node.right, node_depth + 1))

        return root