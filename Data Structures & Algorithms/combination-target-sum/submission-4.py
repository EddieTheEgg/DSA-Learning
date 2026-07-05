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


    # other approach is a for loop given the problem says we have DISTINCT integers, which is slightly more efficient 
    # We select a value from the list, then keep iterating from that
    # value and up until we hit target or out of bound
    #for j in range(i, len(nums)):
        #curComb.append(nums[j])
        #helper(j, curComb, curSum + nums[j])
        #curComb.pop()
    
            
            
