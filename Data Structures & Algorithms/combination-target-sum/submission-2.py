class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultComb = []

        def helper( i, curComb, curSum):
            if curSum == target:
                resultComb.append(curComb.copy())
                return
            if curSum > target or i >= len(nums):
                return

            curComb.append(nums[i])
            helper(i, curComb, curSum + nums[i])
            curComb.pop()
            helper(i+1, curComb, curSum)
        
        helper(0, [], 0)
        return resultComb



    
            
            
