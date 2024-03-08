class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = dict()
        max_freq, res = 0, 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])
        
        for key, val in freq.items():
            if val == max_freq:
                res+=val
            
        return res
            