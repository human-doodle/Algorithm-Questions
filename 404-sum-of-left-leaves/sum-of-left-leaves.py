# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            # Check if the current node is a leaf node and is a left child
            if not node.left and not node.right and is_left:
                return node.val
            # Recursively traverse the left and right subtrees
            left_sum = dfs(node.left, True)
            right_sum = dfs(node.right, False)
            return left_sum + right_sum
        
        return dfs(root, False)