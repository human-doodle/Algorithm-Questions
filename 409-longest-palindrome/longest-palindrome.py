class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        flag = 0
        count = 0
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch, v in d.items():
            if v%2 == 0:
                count+=v
            else: 
                count += v-1
                if flag == 0:
                    count += 1
                    flag = 1
        return count