class     Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        L = 0

# 3 7 6 4
# 0 1 2
        for R in range(len(nums)):
            # if number is in set/window, return true
            if nums[R] in window:
                return True 
            # if not, add that number to the window
            window.add(nums[R])
            # if the number we add to window make window length
            # greater than k, remove the leftmost window value and shift right
            if len(window) > k:
                window.remove(nums[L])
                L += 1
        return False