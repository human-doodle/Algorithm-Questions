'''

PROBLEM STATEMENT: 

Implement Huffman Coding to encode/ decode a message
1. Encode method: Performs Huffman encoding on a messages: s. The messages are composed of English letters. 
   Returns Encoded message and the corresponding encoding_map
2. Decode method: Decodes the methid given the encodded message and the corresponding encoding_map.
   Returns decoded message 
  
References: https://www.youtube.com/watch?v=L5MloiCxHPk

'''


from collections import Counter
import heapq

class node:
    def __init__(self, count, symbol, lchild=None, rchild=None):
        self.symbol = symbol
        self.count = count
        self.lchild = lchild
        self.rchild = rchild

    # override the '<' function to do the following
    # This is to solve the error I got: '<' not supported between instances of 'node' and 'node' 
    def __lt__(self, other):
        return self.count < other.count
        
class HuffmanCoding:

  def encode(self, s):
    
    # s: message to be encoded
    # Return the encoded message and codes used
    
    root = self._build_tree(s)
    encoding_map = self._build_map(root)
    encoded_message = ''.join([encoding_map[symbol] for symbol in s])
    return encoded_message, encoding_map
  
  def decode(self, s, d):
    
    # s: encoded message
    # d: encoding map
    # Return: decoded message

    # create a decoding map
    decoding_map = {code: symbol for symbol, code in d.items()}

    decoded_message = ''
    curr_code = ''

    for bit in s:
      # Adding current bit to the current code
      curr_code += bit

      # if current code in the decoding_map, add the corresponding symbol to the decoded_message
      if curr_code in decoding_map:
         decoded_message+=decoding_map[curr_code]
         
         # reset current code
         curr_code = ''
      
      
    return decoded_message


  # helper functions

  # function to build a min-heap given the message to be encoded
  def _build_tree(self,message):
    
     # counter gives set of pairs of the symbol and the frequency in the message
     counter = Counter(message)
    
     # build a min-heap with the symbol and it's frequency as it's node
     minheap = [node(counter[symbol], symbol) for symbol in counter]
    
     # The minheap is created using a list of node objects. 
     # If the node class does not support the < operator, it will not be possible to compare the nodes and sort the list. 
     # To fix this, I defined the __lt__ method in the node class that specifies how two nodes should be compared.
     heapq.heapify(minheap)
    
     while len(minheap) > 1:
        
        # get the two smallest nodes
        lchild = heapq.heappop(minheap)
        rchild = heapq.heappop(minheap)
        
        # create a parent with the sum of frequency of the children nodes: left, right
        parent = node( lchild.count + rchild.count, None, lchild, rchild)
        # add parent to the minheap
        heapq.heappush(minheap, parent)
        
     # return the root
     return heapq.heappop(minheap)
  
  # function to build a encoding map given the root of the min-heap
  def _build_map(self, root):
    
      # buil an encoding_map through dfs traversal
      def dfs(root, code, encoding_map):
        
         # check if the current node is a leaf node
         if root.symbol:
            # add the code to the encoding map
            encoding_map[root.symbol] = ''.join(code)
            
         else:
          
            # add '0' to the code for the left child node and traverse left
            code.append('0')
            dfs(root.lchild, code, encoding_map)
            # remove the last added bit from the code
            code.pop()
            
            # add '1' to the code for the right child node and traverse right
            code.append('1')
            dfs(root.rchild, code, encoding_map)
            # remove the last added bit from the code
            code.pop()
      
      encoding_map = {}
      dfs(root, [], encoding_map)
      
      return encoding_map

 

# test code to check encoding

hc = HuffmanCoding()
input = 'aabc'
print(hc.encode(input)) 
# output might vary, but one possible output: ('001011', {'a': '0', 'b': '10', 'c': '11'})

input = 'football'
print(hc.encode(input)) 
# output might vary, but one possible output: ('01010100111101110000', {'l': '00', 'f': '010', 't': '011', 'o': '10', 'b': '110', 'a': '111'})

# test code to check decoding

print(hc.decode('001011', {'a': '0', 'b': '10', 'c': '11'})) 
# output: 'aabc'
print(hc.decode('0011110110', {'a': '00', 'l': '01', 'e': '10', 'p': '11'})) 
# output: 'apple'


