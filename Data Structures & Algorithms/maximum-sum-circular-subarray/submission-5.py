class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # -2 4 9 4 Max Subarray Sum: 15
        # -5 4 -5 Min Subarray Sum: -6
        # Total Sum with absolute: 21

        # -2 4 -5 9
        # Max Subarray Sum: 11
        # Min Subaraay Sum: -5
        # Total Sum 16

        # -2 4 9 -5 

        maxSum = nums[0]
        minSum = nums[0]
        curMaxSum = 0
        curMinSum = 0
        total = 0

# 5 -7 5
        for n in nums:
            curMaxSum = max(n + curMaxSum, n)
            curMinSum = min(n + curMinSum, n)
            total += n
            maxSum = max(curMaxSum, maxSum)
            minSum = min(curMinSum, minSum)
        
        if (maxSum <= 0):
            return maxSum
        
        return max(total - minSum, maxSum)
        #Most cases total-minSum wins, but if we have normal Kadane
        # [1, -2, 3, -2] has maxSum winning since 3 is maxSum and -2 is minSum
        





        

