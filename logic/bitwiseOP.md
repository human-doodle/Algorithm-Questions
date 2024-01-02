## AND (&) Operator:
Used for masking and checking if a specific bit is set.
```
int result = a & b; // bitwise AND
```
## OR (|) Operator:
Used for setting bits.
```
int result = a | b; // bitwise OR
```
## XOR (^) Operator:
Used for toggling bits and finding the non-common bits between two numbers.
```
int result = a ^ b; // bitwise XOR
```
## NOT (~) Operator:
Used for flipping bits.
```
int result = ~a; // bitwise NOT
```
## Left Shift (<<) Operator:
Used for multiplying a number by powers of 2.
```
int result = a << 1; // left shift by 1 (multiply by 2)
```
## Right Shift (>>) Operator:
Used for dividing a number by powers of 2.
```
int result = a >> 1; // right shift by 1 (divide by 2)
```

### Bit Manipulation Tricks:
Checking if a Number is a Power of 2:
```
bool isPowerOfTwo = (n > 0) && ((n & (n - 1)) == 0);
```
### Counting Set Bits (Hamming Weight):
```
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}
```
### Swapping Values without Temporary Variable:
```
a = a ^ b;
b = a ^ b;
a = a ^ b;
```
### Extracting the Rightmost Set Bit:
```
int rightmostSetBit = n & -n;
```

# Quick Intro to XOR

Before diving into the problems, let's understand the XOR operation, denoted as a^b. XOR compares each binary bit of a and b. If the bits are the same, it results in 0; if different, it's 1.

## XOR Properties
- XOR of a number with itself is always 0.
- XOR of any number with 0 or itself remains unchanged.
- XOR follows the commutative law: a ^ b ^ c = a ^ c ^ b.
  
Now, let's tackle these four questions.

## 136. Single Number

The goal is to find the number that appears only once in an array where all other numbers appear twice. A simple XOR operation does the trick.
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
```
### Complexity:
- Time: O(N) where N is the array length.
- Space: O(1)

## 137. Single Number II

Here, one number appears once, and the rest appear three times. We use a clever bit manipulation technique.

```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
```
Note: In Python, negative integers are represented using two's complement. If the result is negative, adjust it to the correct 32-bit representation.

## 645. Set Mismatch

Similar to the Single Number II problem, but now we have an error collection. 
```
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        a, b = 0, 0
        for n in nums:
            ret ^= n
        h = 1
        while ret & h == 0:
            h <<= 1
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n

        return [a, b]
```
Complexity:
- Time: O(N)
- Space: O(1)
  
## 260. Single Number III

This time, two numbers appear once, and others appear twice. We use XOR to find the unique numbers.

```
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        a, b = 0, 0
        for n in nums:
            ret ^= n
        h = 1
        while ret & h == 0:
            h <<= 1
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n

        return [a, b]
```
Complexity:
- Time: O(N)
- Space: O(1)

Related Questions

190. Reverse Binary Bits (simple)
191. The Number of Digits 1 (simple)
338. Bit Count (medium)
1072. Flip by Column to Get the Maximum Value and Other Rows (medium)
