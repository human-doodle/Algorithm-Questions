class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        need_flip = [0] * n
        window_flips = 0
        
        for i in range(n):
            if i >= k:
                window_flips -= need_flip[i - k]
            
            if (nums[i] + window_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flip_count += 1
                window_flips += 1
                need_flip[i] = 1
        
        return flip_count
