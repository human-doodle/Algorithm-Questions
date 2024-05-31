class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # Step 1: XOR all numbers to get the XOR of the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Step 2: Find a set bit in xor_result (rightmost set bit)
        set_bit = (xor_result & xor_result-1)^xor_result
        
        # Step 3: Partition the numbers into two groups and XOR separately
        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit:
                print('%d',num & set_bit)
                print('ll',num)
                num1 ^= num
            else:
                print('%dff',num & set_bit)
                print(num)
                num2 ^= num
        
        return [num1, num2]
            