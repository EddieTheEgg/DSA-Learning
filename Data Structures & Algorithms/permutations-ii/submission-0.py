class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Step 1: Track how much frequent we have of each number into a hashset
        res = []
        perm = []
        count = {}

        for n in nums:
            count[n] = 0

        for num in nums:
            count[num] += 1
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in count:
                    if count[num] > 0:
                        perm.append(num)
                        count[num] -= 1

                        dfs()
                        
                        count[num] += 1
                        perm.pop()
            
        dfs()
        return res

