class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = len(nums) + 1
        runningSum = 0
        L = 0

        # 2 1 5 1 5 3
        # 2 1 5 1 5   = 14
        #       L R

        for R in range(len(nums)):
            runningSum += nums[R]
            while runningSum >= target:
                minLength = min(minLength, R - L + 1)
                runningSum -= nums[L]
                L += 1
                    
        if minLength > len(nums):
            return 0

        return minLength

