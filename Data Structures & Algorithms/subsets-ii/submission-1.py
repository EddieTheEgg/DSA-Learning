class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Sort the array first, this is so
        #we can skip choosing same values to get distinct subsets only
        nums.sort()
        #So for eaxmple 1, 2, 2, 3
        # We want (1, 2) and (1,2,2) but not the 1 then skip then 2 (that scenario is where we will use sorted to iterate until next value like 3)

        subSets = []
        curSet = []

        self.helper(0, curSet, subSets, nums)
        return subSets

    def helper(self, index, curSet, subSets, nums):
        #Base case, we reached beyond nums list
        if index >= len(nums):
            subSets.append(curSet.copy())
            return

        curSet.append(nums[index])
        self.helper(index+1, curSet, subSets, nums)
        curSet.pop()

        #So let's say we in that situation where we're at
        # [1] for curSet. We already added [1,2] before, so
        # adding [1,2] from the 2nd index fro mthat 1,2,2,3 list
        # woudl be preitve. we want that 3 instead, so we will iterate
        while index+1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        self.helper(index + 1, curSet, subSets, nums)