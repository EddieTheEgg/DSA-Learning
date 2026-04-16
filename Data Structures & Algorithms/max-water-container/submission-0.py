class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Psuedocode
        # Have a left and right pointer on each edge, and decrease width
        # until we have a good box, where we take the min of each pointer multiply
        # by their index differences

        # We want height of the higher bar, but there's a chance
        # all the other bars may be shorter than this when we iterate

        #We need to keep track of max_area, and move inwards.
        # as we move inwards always min pointer towards larger pointer

        # if both bars have equal length, we move either pointer, lets do right pointer in
        # cause if we were to find a higher bar in the middle we just move the left pointer up

        #Implementation

        # constraints len(2), so there has to be two bars min
        L = 0
        R = len(heights) - 1
        max_area = 0

        while L < R:
            curr_area = min(heights[L], heights[R]) * (R - L)
            max_area = max(max_area, curr_area)

            if heights[L] > heights[R]:
                R -= 1
            elif heights[R] > heights[L]:
                L += 1
            else:
                # equal height bars, we can move right as a choice
                R-=1
        
        return max_area
                
            



