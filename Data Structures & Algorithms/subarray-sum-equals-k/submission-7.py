class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        current_sum = 0
        sum_counts = {0: 1}

        for num in nums:
            current_sum += num
            count += sum_counts.get(current_sum - k, 0)
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

        return count