# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_values = []
        def inorder_traversal(root, sorted_values):
            if not root:
                return
            inorder_traversal(root.left, sorted_values)
            sorted_values.append(root.val)
            inorder_traversal(root.right, sorted_values)
            return root
        def create_balanced_bst(sorted_values, start, end):
            if start> end:
                return 
            mid = start+ (end-start)//2

            left_subtree = create_balanced_bst(sorted_values, start, mid-1)
            right_subtree = create_balanced_bst(sorted_values, mid+1, end)

            node = TreeNode(sorted_values[mid], left_subtree, right_subtree)
            return node
        inorder_traversal(root, sorted_values)
        return create_balanced_bst(sorted_values, 0, len(sorted_values)-1)
        
            