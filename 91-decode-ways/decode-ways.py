class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def recursive(i):
            if  i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = recursive(i+1)
            if i+1 < len(s) and int(s[i:i + 2]) <= 26:
                res+=recursive(i+2)
            dp[i] = res
            return res
        if not s:
            return 0
        return recursive(0)
