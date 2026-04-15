class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # 2, 1, -7, 1, 100
        # -5, -1, -2, 1
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(n, curSum + n)
            maxSum = max(curSum, maxSum)

        return maxSum
            


