class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 0:
            return 0
        if len(s) == 1:
            return 1

        window_set = set()
        longest = 0
        L = 0

        for R, char in enumerate(s):
            while char in window_set:
                window_set.remove(s[L])
                L += 1
            window_set.add(char)
            longest = max(longest, R-L + 1)
        
        return longest