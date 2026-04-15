class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0

        hashNums = {}
        while i < len(nums):
            otherNum = target - nums[i]
            if otherNum in hashNums:
                idx1, idx2 = hashNums[otherNum], i
                if idx1 < idx2:
                    return [idx1, idx2]
                else:
                    return [idx2, idx1]
            hashNums[nums[i]] = i
            i += 1
