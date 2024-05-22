class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, path):
            if start == len(s):
                res.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    backtrack(end, path + [substring])
        
        def is_palindrome(substring):
            return substring == substring[::-1]
        
        res = []
        backtrack(0, [])
        return res  