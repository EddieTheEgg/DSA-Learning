class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # we can either go down or right
        def dfs(row, col, cache):
            if (row >= m or col >= n):
                return 0
            if cache[row][col] > 0:
                return cache[row][col]
            #Found a path
            if ((row == m - 1) and (col == n-1)):
                return 1
            
            cache[row][col] = dfs(row + 1, col, cache) + dfs(row, col + 1, cache)

            return cache[row][col]
        
        return dfs(0, 0, [[0] * n for _ in range(m)])
        
        # This is the fastest way (looked at this solution)
        #We go through each row from right to left
        #Then we just add curr + right side of curr
        #This works on single array hard to picture but look at grid:
        # Each row will get replaced from right to left
        # 6 3 1
        # 3 2 1
        # 1 1 1
        # n-2 since last row and last col always have 1 way to reach end
        #dp = [1] * n

        #for i in range(m-2, -1, -1):
            #for j in range(n-2, -1, -  1):
                #p[j] += dp[j+1]

        #return dp[0]



        


        
        