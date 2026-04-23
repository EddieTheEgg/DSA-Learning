class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

      total = 0
      prefix = []

    # First build an array of the prefix sums in increasing order
      for num in nums:
        total += num
        prefix.append(total)

      count = 0
      sum_counts = {0: 1}

      for i in range(len(prefix)):
            # needed_sum should return 0 if our current prefix subtracts target
            needed_sum = prefix[i] - k
            count += sum_counts.get(needed_sum, 0)
            sum_counts[prefix[i]]= sum_counts.get(prefix[i], 0) + 1
            #Cur sum - prev sum = k
            #cur sum = k + prev_sum

      return count