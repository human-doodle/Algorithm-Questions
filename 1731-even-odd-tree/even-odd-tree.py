# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
  

        if not root:
            return False

        queue = deque([(root, 0)])  # Tuple: (node, level)
        
        while queue:
            level_size = len(queue)
            prev_value = None

            for _ in range(level_size):
                current_node, level = queue.popleft()
                
                if level % 2 == 0:  # Even-indexed level
                    if current_node.val % 2 == 0 or (prev_value is not None and current_node.val <= prev_value):
                        return False
                else:  # Odd-indexed level
                    if current_node.val % 2 == 1 or (prev_value is not None and current_node.val >= prev_value):
                        return False
                
                prev_value = current_node.val

                if current_node.left:
                    queue.append((current_node.left, level + 1))
                if current_node.right:
                    queue.append((current_node.right, level + 1))

        return True
