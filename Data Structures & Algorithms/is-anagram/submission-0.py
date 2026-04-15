class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a hash table
        existing_char_s = {}
        existing_char_t = {}

        # If the two input list are not equal, then return false
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            existing_char_s[s[i]] = 1 + existing_char_s.get(s[i], 0)
            existing_char_t[t[i]] = 1 + existing_char_t.get(t[i], 0)
        
        return existing_char_s == existing_char_t
