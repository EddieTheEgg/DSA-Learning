class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        



        # The save space way
        M, N = len(obstacleGrid), len(obstacleGrid[0])
    
        # initialize bottom row, break when we reach a blockage (1) since
        # anything on the left of block can't go right hence 0 paths
        dp = [0] * N
        for j in range(N - 1, -1, -1):
            if obstacleGrid[M - 1][j] == 1:
                break
            dp[j] = 1
        
        # fill rest bottom-up
        for i in range(M - 2, -1, -1):
            for j in range(N - 1, -1, -1): #Unlike unique path 1, can't assume last column is not blocked so start at last column
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j + 1 < N: # Leave last column as is if not blocked
                    dp[j] += dp[j + 1]
        
        return dp[0]