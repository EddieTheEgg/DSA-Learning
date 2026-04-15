class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L = 0
        R = len(numbers) - 1

        while L < R:
            curSum = numbers[L] + numbers[R]
            if curSum == target:
                return [L+1] + [R+1]
            if curSum > target:
                R -= 1
            if curSum < target:
                L += 1
        

        #Always one solution, so no need to fallback if we assume