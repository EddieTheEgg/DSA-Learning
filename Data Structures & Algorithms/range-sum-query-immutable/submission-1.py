class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = []
        total = 0

        # Get prefix sums and populate
        # That way we can subtract left prefix from
        # right prefix to get remaining total
        for num in nums:
            total += num
            self.nums_array.append(total)
        
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.nums_array[right]
        if left > 0:
            leftSum = self.nums_array[left-1]
        else:
            leftSum = 0
        
        return rightSum - leftSum
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)