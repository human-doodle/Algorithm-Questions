class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(s)<len(t):
            return ""

        # freq of t
        freq_t = Counter(t)

        # number of unique characters in t, which need to be in the required window
        req = len(freq_t)

        # left and right pointer
        left, right = 0,0

        # done variable is used to keep track of the uniquw characters in the s also presnt in t with deisred frequncy
        done = 0

        # dictionary to keep track of all elements in the current window
        window_freq = dict()

        # answer : tuple of form (window length, left and right)
        answer = float("inf"), None, None

        while right < len(s):

            window_freq[s[right]] = window_freq.get(s[right], 0) + 1

            if s[right] in freq_t and window_freq[s[right]] == freq_t[s[right]]:
                done += 1

            # contract
            while done == req and left <= right:
                
                if right - left + 1 < answer[0]:
                    answer = (right-left+1, left, right)

                window_freq[s[left]]-=1
                if s[left] in freq_t and window_freq[s[left]] < freq_t[s[left]]:
                    done -= 1
                
                left += 1

            # expand
            right += 1

        
        return "" if answer[0] == float("inf") else s[answer[1]:answer[2]+1]