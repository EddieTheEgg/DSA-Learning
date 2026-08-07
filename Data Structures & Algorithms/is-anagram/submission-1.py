class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        letterS, letterT = {}, {}

        for i in range(len(s)):
            letterS[s[i]] = 1 + letterS.get(s[i], 0)
            letterT[t[i]] = 1 + letterT.get(t[i], 0)

        return letterS == letterT
            


