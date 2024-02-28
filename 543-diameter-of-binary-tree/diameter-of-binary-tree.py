# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Variable to store the diameter

        def dfs(node):
            if not node:
                return 0
            
            # Recursively calculate the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the diameter if the current subtree has a longer path
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter

        