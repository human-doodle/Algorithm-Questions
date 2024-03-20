# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        # Traverse list1 to find the a-1th and bth nodes
        prev_a = None
        current = list1
        for _ in range(a):
            prev_a = current
            current = current.next

        # Traverse list2 to find its tail
        tail_list2 = list2
        while tail_list2.next:
            tail_list2 = tail_list2.next

        # Connect the a-1th node to the head of list2
        if prev_a:
            prev_a.next = list2
        else:
            list1 = list2

        # Connect the tail of list2 to the b+1th node
        for _ in range(b - a + 1):
            current = current.next
        tail_list2.next = current

        return list1
            