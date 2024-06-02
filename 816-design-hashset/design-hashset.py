class MyHashSet:

    def __init__(self):
        self.l = []

    def add(self, key: int) -> None:
        if key not in self.l:
            self.l.append(key)

    def remove(self, key: int) -> None:
        for i, num in enumerate(self.l):
            if num == key:
                del self.l[i]
        

    def contains(self, key: int) -> bool:
        for i in self.l:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)