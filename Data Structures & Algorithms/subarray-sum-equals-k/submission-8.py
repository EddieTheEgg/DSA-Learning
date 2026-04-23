class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

      # Prefix Sum + Hashmap pattern:
        # Check subarray difference (could be the same index in beginning) current_sum - previous_prefix = k
        # So we look for previous_prefix = current_sum - k
        # The hashmap tracks how many times each previous prefix sum has occurred
        # Each occurrence is a different left boundary for a valid subarray
            #Cause the diff is where we slice/chop off left off that diff to get the target

        #nums =   [1, 2, 1, 3]
        #prefix = [1, 3, 4, 7]

        #current_sum = 7, k = 4, diff = 3, so we need to remove this 3 prefix_sum to get the target
        # 3 is at index 1, so if we chop off remove all subarray to the left of it leaving us with 
        # the right target subarray!

        #Chop off prefix at index 1 (where prefix = 3):
        #remaining = [1, 3] = 4 

        #More complex example:
        #nums =   [1, 2, -3, 3, 1, 3]
        #prefix = [1, 3,  0, 3, 4, 7]

        #current_sum = 7, k = 4, diff = 3 (we need t remove this 3 to get target!)

        #Prefix 3 appears at index 1 and index 3:
        # Cause at some point from left to curSum each prefix accumulates tothat value,
        # so everytime we see that difff we need to remove/count it as a count

        #Chop at index 1 (prefix = 3):
        #remaining = [-3, 3, 1, 3] = 4 

        #Chop at index 3 (prefix = 3):
        #remaining = [1, 3] = 4 

         # Seed {0: 1} because a prefix of 0 exists before the array starts


        count = 0
        current_sum = 0
        sum_counts = {0: 1} 

        for num in nums:
            current_sum += num
            count += sum_counts.get(current_sum - k, 0)
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

        return count