# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = [(root, -float('inf'))]
        count = 0
        while s:
            node, pmax = s.pop()
            print(node.val, pmax)
            if node.val>=pmax:
                count+=1
            new_pmax = max(node.val, pmax)
            
            if node.right:
                s.append((node.right, new_pmax))
            
            if node.left:
                s.append((node.left, new_pmax))
            
        return count

        
        