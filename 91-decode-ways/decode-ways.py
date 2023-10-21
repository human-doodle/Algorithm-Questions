class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def rec(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0
            
            res = rec(i+1)
            if i+2 <= len(s) and int(s[i:i+2]) <= 26:
                res+=rec(i+2)
            dp[i] = res
            return res
        return rec(0)
    

    #  121
    # /.   \.  
    # 1     12 
    # / \.  /
    # 2. 21 1
    # /.   
    # 1    