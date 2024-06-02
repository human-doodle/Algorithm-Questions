class ListNode:
    def __init__(self,key=-1,next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
    
    def hashkey(self,num):
        return num%1000

    def add(self, key: int) -> None:
        currNode = self.map[self.hashkey(key)]
        while currNode.next:
            if currNode.next.key == key:
                return
            else:
                currNode = currNode.next
        currNode.next = ListNode(key)

    def remove(self, key: int) -> None:
        currNode = self.map[self.hashkey(key)]
        while currNode and currNode.next:
            if currNode.next.key == key:
                currNode.next = currNode.next.next
                return
            currNode = currNode.next

    def contains(self, key: int) -> bool:
        currNode = self.map[self.hashkey(key)].next
        while currNode:
            if currNode.key == key:
                return True
            currNode = currNode.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)