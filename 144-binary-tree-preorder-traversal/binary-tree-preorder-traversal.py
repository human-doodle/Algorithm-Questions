# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._preorderTraversal( root, [])
    def _preorderTraversal(self, node, l):
        if node is None:
            return 
        l.append(node.val)
        self._preorderTraversal( node.left, l)
        self._preorderTraversal( node.right, l)
        return l

        
        