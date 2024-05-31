# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Recursively process the next node
        head.next = self.removeElements(head.next, val)
        
        # Decide whether to include the current node in the result
        if head.val == val:
            return head.next
        else:
            return head