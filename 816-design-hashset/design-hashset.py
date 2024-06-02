class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:
    def __init__(self):
        # number of buckets
        self.bucket_size = 1000
        # array of buckets with dummy nodes
        self.buckets = [ListNode() for _ in range(self.bucket_size)]

    def add(self, key: int) -> None:
        # compute hash code
        bucket_index = key % self.bucket_size
        # find the last node in the linked list
        prev = self.buckets[bucket_index]
        curr = prev.next
        while curr:
            if curr.val == key:
                # key already exists
                return
            prev, curr = curr, curr.next
        # key doesn't exist, add a new node
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        # compute hash code
        bucket_index = key % self.bucket_size
        # find the node to remove
        prev = self.buckets[bucket_index]
        curr = prev.next
        while curr:
            if curr.val == key:
                # remove the node
                prev.next = curr.next
                return
            prev, curr = curr, curr.next

    def contains(self, key: int) -> bool:
        # compute hash code
        bucket_index = key % self.bucket_size
        # find the node
        curr = self.buckets[bucket_index].next
        while curr:
            if curr.val == key:
                # key found
                return True
            curr = curr.next
        # key not found
        return False