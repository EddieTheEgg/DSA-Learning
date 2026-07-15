class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        def helper(i, perms):
            if i == len(nums):
                return [[]]
            
            res = []
            perms = helper(i+1, res)

            for perm in perms:
                for j in range(len(perm)+1):
                    permCopy = perm.copy()
                    permCopy.insert(j, nums[i])
                    res.append(permCopy)
            
            return res

        return helper(0, [])

                

