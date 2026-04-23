class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #2, -1, 1, 2
        #2,  1, 2, 4
        #4,  2, 1, 2
        
        inc = []
        total = 0
        curSum = 0
        res = 0
        prefixSums = { 0: 1}


        for n in nums:
            total += n
            inc.append(n)

        for n in inc:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)


        return res

            
            
            
            
            

        




