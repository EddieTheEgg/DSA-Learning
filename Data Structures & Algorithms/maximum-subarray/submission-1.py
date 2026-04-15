class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # 10, 15, -2, 1, 100
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum , 0)
            curSum += n
            maxSum = max(curSum, maxSum)

        return maxSum
            


