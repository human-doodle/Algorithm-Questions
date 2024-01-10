# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS
        result = []
        if not root:
            return result
        queue = collections.deque()
        queue.append(root)

        while(queue):
            level_sum = 0
            queue_size = len(queue)
            for i in range(queue_size):
                node = queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum/queue_size)
        
        return result

            

        

        