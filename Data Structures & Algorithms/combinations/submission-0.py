class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allComb = []
        self.helper(1, [], allComb, n, k)
        return allComb
    

    def helper(self, i, curComb, allComb, n, k):
        if len(curComb) == k:
            allComb.append(curComb.copy())
            return
        if i > n:
            return

        for num in range(i, n+1):
            curComb.append(num)
            self.helper(num+1, curComb, allComb, n, k)
            curComb.pop()


        