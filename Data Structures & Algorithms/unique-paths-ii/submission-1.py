class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #Lets do it sorta brute force dfs way first

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row >= rows or col >= cols or obstacleGrid[row][col] == 1:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1

            memo[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
            return memo[(row, col)]

        return dfs(0,0)