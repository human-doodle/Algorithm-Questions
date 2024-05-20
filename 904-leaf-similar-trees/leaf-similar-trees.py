# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        st1 = [root1]
        st2 = [root2]
        leaf1 = []
        leaf2 = []
        while st1:
            curr = st1.pop()

            if not curr.left and not curr.right:
                leaf1.append(curr.val)
            
            if curr.right:
                st1.append(curr.right)
            if curr.left:
                st1.append(curr.left)
        
        while st2:
            curr = st2.pop()

            if not curr.left and not curr.right:
                leaf2.append(curr.val)
            
            if curr.right:
                st2.append(curr.right)
            if curr.left:
                st2.append(curr.left)

        return leaf1 == leaf2   


        