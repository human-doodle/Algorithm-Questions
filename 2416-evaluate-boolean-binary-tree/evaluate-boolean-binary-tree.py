# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def postorder(self,node):
        if node.val == 0 or node.val == 1:
            return node.val 
        if node.val == 2:
            return self.postorder(node.left) or self.postorder(node.right)
        elif node.val == 3:
            return self.postorder(node.left) and self.postorder(node.right)
        return False
        
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.postorder(root)


'''
Input: root = [2,1,3,null,null,0,1]
Output: true

T, F, T, AND, OR


'''