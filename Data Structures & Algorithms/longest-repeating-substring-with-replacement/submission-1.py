class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #How this works
        # We keep a frequency track of each letter
        # Our window size continues to grow until the max letter frequency in the window
        # cannot fill the entire space with k replacements
        # so A B B A A, and k = 1, we need k = 2 to replace in the window but we cant
        # so now we decreasce window size, shift L to the right so remove that A, and also decrease frequency of that A too!
        # Keep doing this until R reaches the end in O(n) time


        count = {} # frequency map for current window
        L = 0
        max_freq = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_freq = max(max_freq, count[s[R]])

            # Check if window is invalid
            window_length = R - L + 1
            if (window_length - max_freq) > k:
                count[s[L]] -= 1
                L += 1
        return R - L + 1


       
            
