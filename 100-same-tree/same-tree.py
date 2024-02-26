# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        """
        O(n) O(n)
        """
        # BFS Queues
        stack = [p, q]
        while stack:
            n, m = stack.pop(0), stack.pop(0)
            if n is None and m is None:
                continue
            if n is None or m is None or n.val != m.val:
                return False
            stack += n.left, m.left, n.right, m.right
        return True