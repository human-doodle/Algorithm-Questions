'''

PROBlEM STATEMENT:

#recursion

Write a function pattern that generates all binary strings (strings that only contain characters '0' and '1') of a given length n such that none of the generated strings contain two consecutive '1's.
Note that the strings in your output should be ordered lexicographically.
One approach to solve this problem is to generate all binary strings of a certain length and then filter the
desired strings. Unfortunately, this approach doesn't scale well. For example, for n = 20, the number of
strings with our property is only 17711, but the number of binary strings of length 20 is 220 which is
1048576.
Another approach is to combine recursion with an additional invariant generate the strings with the desired
property and don't generate others. If you have an answer for n = k (say k = 3), how would you generate
the answer for n = k+1?
Examples
›>> pattern (1)
['0', '1']
›>> pattern (2)
['00', '01', '10']
>>> pattern (3)
['000', '001', '010', '100', '101']
›>> pattern (4)
['0000',
'0001', '0010', '0100', '0101', '1000', '1001', '1010']

'''

def pattern(n):
    arr = []
    def generate(n, s):
        
        if n == len(s):
            arr.append(s)
        else:
            if s=='' or s[-1]=='0':
                generate(n, s+'0')
                generate(n, s+'1')
            else:
                generate(n, s+'0')
    
    generate(n,'')
    return arr
