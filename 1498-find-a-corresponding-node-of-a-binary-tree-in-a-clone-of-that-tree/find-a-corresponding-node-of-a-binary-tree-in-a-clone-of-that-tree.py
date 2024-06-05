# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_1 = [original]
        stack_2 = [cloned]
        while stack_1 and stack_2:
            node1 = stack_1.pop()
            node2 = stack_2.pop()
            # print(target)
            if node1 == target:
                return node2
            if node1.right:
                stack_1.append(node1.right)
            if node1.left:
                stack_1.append(node1.left)
            if node2.right:
                stack_2.append(node2.right)
            if node2.left:
                stack_2.append(node2.left)
        


        