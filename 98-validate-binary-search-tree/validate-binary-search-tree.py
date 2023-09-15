# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # RECURSION valid range
        # # DFS 
        # def valid(node, lb, ub):
        #     if not node:
        #         return True
        #     elif not (node.val > lb and node.val < ub):
        #         return False
        #     return (valid(node.left, lb, node.val) and
        #     valid(node.right, node.val, ub))
        # return valid(root, -float('inf'), float('inf'))
        
        # ITERATIVE VALID RANGE
        # DFS
        s = [(root, -float('inf'), float('inf'))]
        while s:
            node, lb, ub = s.pop()
            if not node:
                continue
            if not (node.val>lb and node.val<ub):
                return False
            s.append((node.left, lb, node.val))
            s.append((node.right, node.val, ub))
        return True



            


        