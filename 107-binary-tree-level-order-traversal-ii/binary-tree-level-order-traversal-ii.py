# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        d = defaultdict(list)
        q = deque()
        q.append((root, 0))
        maxLevel = 0
        
        while q:
            curr, level = q.popleft()
            d[level].append(curr.val)
            maxLevel = max(maxLevel, level)

            if curr.left:
                q.append((curr.left, level+1))
            if curr.right:
                q.append((curr.right, level+1))

        res = []
        for i in range(maxLevel, -1, -1):
            res.append(d[i])
        
        return res