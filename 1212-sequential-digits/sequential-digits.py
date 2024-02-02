class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
    
        for digit in range(1, 9):  # Starting from 1 because we want at least two digits
            num = digit
            next_digit = digit + 1
            
            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                next_digit += 1
        
        return sorted(result) 