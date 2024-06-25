# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # right -> center -> left
        
        def reverse_traverse(root, sum_inlist):
            if not root:
                return 
            reverse_traverse(root.right, sum_inlist)
            sum_inlist[0] += root.val
            root.val = sum_inlist[0]
            reverse_traverse(root.left, sum_inlist)
            return root
        
        return reverse_traverse(root, [0])   
            
        

