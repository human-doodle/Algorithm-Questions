'''

# priority queue #min-heap #heap

Implement a class to find a trending word. The class TrendingWord which you’ll implement
has two methods of interest, insert and get. insert takes a line, i.e., a string of words separated by spaces,
as an argument and processes the words in the line to answer a future get query. The get method returns
the 5th most frequent word and the number of times that word occurred so far among all the words seen so
far (i.e., words from all the lines that have been inserted so far). The expected time complexity of insert is
O(n), where n is the length of the line given as input to the insert method, and the expected time complexity
of get is O(1).
The following contrived example should make the problem statement clearer.
>>> tw = TrendingWord()
>>> tw.insert("annoying annoying")
>>> tw.insert("phone phone phone")
>>> tw.insert("cat cat cat cat")
>>> tw.insert("boat boat boat boat boat")
>>> tw.insert("water water water water water water")
>>> tw.get()
('annoying', 2)
>>> tw.insert("gold gold gold gold gold gold gold")
>>> tw.insert("prime prime prime prime prime prime prime prime")
>>> tw.insert("okay okay okay okay okay okay okay okay okay")
>>> tw.get()
('boat', 5)

'''

import heapq

class TrendingWord:
    def __init__(self):
        self.freq = {}
        self.heap = []

    def insert(self, s: str):
        words = s.strip().split()
        for word in words:
            self.freq[word] = self.freq.get(word, 0) + 1
        
        heap = []
        for word, count in self.freq.items():
            if len(heap) < 5:
                heapq.heappush(heap, (count, word))
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, word))
        self.heap = heap
        

    def get(self):
        print(self.heap)
        if len(self.heap)<5:
            return None
        count, word = self.heap[-5]
        return word, count

