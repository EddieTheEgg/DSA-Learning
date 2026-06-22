class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curSet = []
        subSet = []

        self.helper(0, nums, curSet, subSet)
        return subSet



    def helper(self, index, nums, curSet, subSet):
        if index >= len(nums):
            subSet.append(curSet.copy())
            return

        curSet.append(nums[index])
        self.helper(index+1, nums, curSet, subSet)
        curSet.pop()

        self.helper(index+1, nums, curSet, subSet)