class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # k = 2
        # X Y Y X
        # X X X X
        # L     R

        # return R - L + 1

        # If next curr letter is not equal to L and we haven't reached max k, switch curr to L

        # k = 2 -> 0
        # A A B B C B B
        # A A A A
        # L       
        #         R

        # any remainig k can be added to the longest length       




        # We store k locally for each L R window, and once we run out of k we update L to R, or if we run out of space, we return longest length
        # When we run out of k, we move L to the curr R spot and then repeat check 

        # We update L to R


        


        count = {} # frequency map for current window
        L = 0
        max_length = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_length = max(max_length, count[s[R]])

            # Check if window is invalid
            window_length = R - L + 1
            if (window_length - max_length) > k:
                count[s[L]] -= 1
                L += 1
        return len(s) - L


       
            
