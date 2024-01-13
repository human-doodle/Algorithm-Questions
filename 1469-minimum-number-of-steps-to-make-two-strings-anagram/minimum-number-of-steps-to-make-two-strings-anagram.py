class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashs=dict()
        hasht=dict()
        for i in range(len(s)):
            hashs[s[i]] = 1 if s[i] not in hashs else hashs[s[i]]+1
            hasht[t[i]] = 1 if t[i] not in hasht else hasht[t[i]]+1
        cnt = 0
        for key, value in hashs.items():
            if key in hasht:
                if value == hasht[key]:
                    cnt+=value
                else:
                    cnt+=min(value, hasht[key])
        diff_char = len(s)  - cnt
        return diff_char
            
        
        