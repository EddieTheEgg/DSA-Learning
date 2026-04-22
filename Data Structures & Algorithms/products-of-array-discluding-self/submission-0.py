class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we want product of left of i and right of i
        # out of bounds would be just value 1
        # So how do we get value of right of i or left of i?

        
        output = []
        left_product_array = []
        right_product_array = [0] * len(nums)

        total = 1

        #First populate with product at each subarray
        for num in nums:
            total = num * total
            left_product_array.append(total)
        total = 1

        # Then from right to left
        for i in range(len(nums) - 1, -1, -1):
            total = nums[i] * total
            right_product_array[i] = total
            

        #Then for each area we multiple by left and right subarray
        for i in range(len(nums)):
            leftProduct = left_product_array[i-1] if i > 0 else 1
            rightProduct = right_product_array[i+1] if i < len(nums) - 1 else 1
            product = leftProduct * rightProduct
            output.append(product)

        return output


            