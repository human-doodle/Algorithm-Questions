# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs itertative
        if not root:
            return

        q = collections.deque()
        q.append((root, 0))

        d = dict()

        while q:
            curr, level = q.popleft()
            # print(curr.val, level)
            d[level] = d.get(level, [])
            d[level].append(curr.val)
            if curr.left:
                    q.append((curr.left, level+1))
            if curr.right:
                    q.append((curr.right, level+1))
            
        res = []
        for key, value in d.items():
            if key%2 == 0:
                res.append(value)
            else:
                res.append(value[::-1])

        return res

'''
bfs
lastLevel  = 0
if level!=lastLevel
    lastLevel+=1
    res.append([curr.val])
else:
    res[level].append(curr.val)
'''