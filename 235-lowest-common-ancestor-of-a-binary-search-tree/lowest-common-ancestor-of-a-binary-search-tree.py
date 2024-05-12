# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None
        node = root
        while node:
            if p.val<node.val and q.val<node.val:
                    node = node.left
            elif p.val>node.val and q.val>node.val:
                    node = node.right
            else:
                    return node

            




'''
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

'''        