class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.cache = dict()
        self.left, self.right = Node(0,0), Node(0,0)

        # LRU : left, MRU: right
        self.left.next , self.right.prev = self.right, self.left

  
    # insert from right
    def insert(self, node):
        nxt = self.right
        node.next = nxt
        node.prev = nxt.prev
        nxt.prev.next = node
        nxt.prev = node

     # remove from left
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)