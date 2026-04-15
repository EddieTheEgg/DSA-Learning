class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
            if num_count.get(num) > 1:
                return True

        return False 
