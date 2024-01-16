import random

class RandomizedSet:

    def __init__(self):
        self.s = set()
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s.add(val)
            self.elements.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            self.elements.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if self.elements:
            return random.choice(self.elements)
        else:
            # Handle the case where the set is empty
            return None      
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()