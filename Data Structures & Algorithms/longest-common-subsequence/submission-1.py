class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # I think first go through the shortest array, cause that's
        # what would have the subsequence

        #cac
        #cract

        #Result: cac

        #rct
        #crabt

        # I think approach is we build the subsequences as we iterate once through an array
        # cat
        # ca
        # c
        # at
        # ct

        #abc
        #cba 


        #ctvaq
        #crabg

        dp = {} # "ab" : 2 "jef": 1


        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i,j)] 
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + lcs(i+1, j+1)
            else:
                dp[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))
            return dp[(i, j)]
            
        return lcs(0, 0)
