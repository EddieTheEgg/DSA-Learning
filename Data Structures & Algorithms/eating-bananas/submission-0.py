class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #Set pointers for left and right on the array (1,2,3,4,...) these are k bananas per hour
        left = 1
        right = max(piles)
        res = right 


        while left <= right:
            k = left + (right-left) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                right = k -1
            else:
                left = k + 1
        return res



