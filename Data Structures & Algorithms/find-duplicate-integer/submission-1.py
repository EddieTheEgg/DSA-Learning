class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Treat each value as a node, and we point them to each other
        #So at index 0, it points to 1
        # at index 1, it points to 2
        # at index 2, it points to 3,
        # at index 3, it points to 2
        # 2 already points to index 3 so we return number 2

        # We use a two pointer approach to detect such cycle

        slow = nums[0]
        fast = nums[0]

        # Cause there's def a duplicate
        while True:
            slow = nums[slow] # 2
            fast = nums[nums[fast]] # 3
            if slow == fast:
                break
        # we detected a cycle, meeting somewhere inside the cycle but we want to find the duplicate entrance causing this
        # Based on the head of the cycle duplicate logic, the distance from the duplicate
        # is the same as the remainder of the cycle

        #For eaxmple in 1, 2, 3, 2, 2. The cycle starts at the second 2 but our cycle detects at value 3
        # we are one iteration off so we start at head of array and the duplicate part which is slow to get the actual duplicate start
        slow2 = nums[0]
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow


            

        