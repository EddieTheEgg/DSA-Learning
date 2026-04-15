class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return 1

        # 2 4 3 2 2 5 1 4
        # L R
        #   L R
        #     L R

        L = 0
        R = 1
        longest = 1
        curr_longest = 1
        prev_diff = 0

        # 2 4 3 2 2 5 1 4
        # prev_diff = 2
        # curr_longest = 1


        while R < len(arr):
            curr_diff = arr[R] - arr[L]
            # previous diff was negative, so curr diff has to be posiitve
            if prev_diff <= 0 and curr_diff > 0:
                curr_longest += 1
                prev_diff = curr_diff #switch prev diff to posiitve
            # previous diff was positive, so curr diff has to be negative
            elif prev_diff >= 0 and curr_diff < 0:
                curr_longest += 1
                prev_diff = curr_diff #switch prev diff to negative
            else:
                prev_diff = curr_diff
                longest = max(longest, curr_longest)
                if curr_diff != 0:
                    curr_longest = 2  # current pair starts a new streak
                else:
                    curr_longest = 1

            # Shift window up by 1
            L += 1
            R += 1
            
        # in the scenario the turbulence went all the way through
        # without failure, we update curr_longest to longest
        return max(longest, curr_longest)

