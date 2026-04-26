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
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow

            

        