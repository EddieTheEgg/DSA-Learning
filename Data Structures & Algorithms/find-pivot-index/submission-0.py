class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
       #Prefix, 
       #We keep track of total of entire array
       # Total - leftSum = rightSum, this is our answer

        total = 0
        leftSum = 0
        for num in nums:
            total += num
        
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]

            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]

        return -1


