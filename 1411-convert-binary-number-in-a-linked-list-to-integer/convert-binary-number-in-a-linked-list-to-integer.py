# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr= head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        num = 0
        for i, n in enumerate(res):
            num += 2**(len(res)-1-i)*n
        return num
        