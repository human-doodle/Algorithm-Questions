class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s: string) -> bool:
            if s[:] == s[::-1]:
                return True
            else:
                return False
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""
            

        