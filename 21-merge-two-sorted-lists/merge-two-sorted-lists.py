# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode(0)
        curr = newList
        while(list1 and list2):
            if list1.val<=list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return newList.next
        

'''
newlist = ListNode(0)
curr = newList
if i<=j
curr = i
i = i.next
if j<i
curr.next = j
j=j.next
Input: list1 = [1,2,4]
                  i
list2 = [1,3,4]
         j
Output: [1,1,2,3,4,4]
'''