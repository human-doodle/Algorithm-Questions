class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        dp = {len(s):1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i+2 <= len(s) and int(s[i:i+2]) <= 26 and int(s[i:i+2])>=10:
                dp[i]+=dp[i+2]
        return dp[0]
            
            
    

    #  121
    # /.   \.  
    # 1     12 
    # / \.  /
    # 2. 21 1
    # /.   
    # 1    