'''
Problem Statement: 
Implement the MaxHeap class and its methods.

1. heapifyUp, HeapifyDown methods are used to maintain the heap property of the list of data.
 i. heapifydown operation is used to restore the heap property when a node violates the property of the max heap by having a value less than one of its children. 
    The operation is performed by swapping the node with its largest child and recursively applying the same operation to the swapped child until the heap property is restored.(Heapify method of the heapq module)
 ii. heapifyup operation is used to restore the heap property when a node violates the property of the max heap by having a parent with a smaller value.
     The operation is performed by swapping the node with its parent until the heap property is restored.
2. getMax method is used to return the maximum element of all the elements and remove it from the heap.
3. insert method is used insert a new element into the heap keeping the max property of heap.
4. print returns the heap as list where i is parent then 2i + 1 and 2i + 2 are left and right childs

Reference: https://www.youtube.com/watch?v=hkyzcLkmoBY

'''



class MaxHeap:
  def __init__(self, ls=None):
    self.size = 0
    self.maxheap = []
    if ls:
      self.maxheap = ls
      self.heapifyDown(0)  
    pass
  
  def heapifyDown(self, index):
    max_element_index = index
    if (self._hasLeftChild(index) and self.maxheap[max_element_index] < self._leftChild(index)):
        max_element_index = self._getLeftChildIndex(index)
    if (self._hasRightChild(index) and self.maxheap[max_element_index] < self._rightChild(index)):
        max_element_index = self._getRightChildIndex(index)
    if max_element_index != index:
      self._swap(index, max_element_index)
      self.heapifyDown(max_element_index)
    
  def insert(self, element):
    self.maxheap.append(element)
    self.heapifyUp(len(self.maxheap)-1)

  def getMax(self):
    if len(self.maxheap) == 0:
      return None
    maxelement = self.maxheap[0]
    self.maxheap[0] = self.maxheap[- 1]
    self.maxheap.pop()
    self.heapifyDown(0)
    return maxelement

  def heapifyUp(self, index):
    if (self._hasParent(index) and self._parent(index)<self.maxheap[index]):
      self._swap(self._getParentIndex(index), index)
      parent_index = self._getParentIndex(index)
      self.heapifyUp(parent_index) 

  def print(self):
    return self.maxheap
  
#   helper functions

  
  def _getParentIndex(self, index):
    return((index-1)//2)
  
  def _getLeftChildIndex(self, index):
    return 2*index + 1
  
  def _getRightChildIndex(self, index):
    return 2*index + 2
  
  def _parent(self, index):
    return self.maxheap[self._getParentIndex(index)]
  
  def _leftChild(self, index):
    return self.maxheap[self._getLeftChildIndex(index)]
  
  def _rightChild(self, index):
    return self.maxheap[self._getRightChildIndex(index)]
  
  def _hasParent(self, index):
    return self._getParentIndex(index)>=0
  
  def _hasLeftChild(self, index):
    return self._getLeftChildIndex(index) < len(self.maxheap)
  
  def _hasRightChild(self, index):
    return self._getRightChildIndex(index) < len(self.maxheap)
  
  def _swap(self, index1, index2):
    self.maxheap[index1], self.maxheap[index2] = self.maxheap[index2], self.maxheap[index1]

  
# Test code

# def test_max_heap(input):
#   mx = None
#   result = []
#   i = 0
#   while i < len(input):
#     if input[i] == 'MaxHeap':
#       mx = MaxHeap(input[i+1])
#       result.append(None)
#       i += 2
#     elif input[i] == 'insert':
#       result.append(mx.insert(input[i+1]))
#       i += 2
#     elif input[i] == 'getMax':
#       result.append(mx.getMax())
#       i += 1
#     elif input[i] == 'print':
#       res = mx.print()
#       result.append(res[:])
#       i += 1
#     else:
#       i += 1
#   return result 

# input = ['MaxHeap', [2, 3, 4], 'print', 'insert', 1, 'insert', 5, 'insert', 6, 'insert', 7,'getMax','print', 'insert', 8, 'print']
# print(test_max_heap(input)) 
# Ouput: [None, [4, 3, 2], None, None, None, None, 7, None, [8, 4, 6, 1, 3, 2, 5]]

