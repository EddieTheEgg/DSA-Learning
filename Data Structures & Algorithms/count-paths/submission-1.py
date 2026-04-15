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


        


        
        