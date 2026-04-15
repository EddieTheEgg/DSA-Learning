class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c) -> int:
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0
            grid[r][c] = 0

            return (1 + dfs(r + 1, c) + dfs (r - 1, c) + dfs(r, c-1) + dfs(r, c+1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island_area = dfs(r, c)
                    if island_area > max_island_area:
                        max_island_area = island_area
        
        return max_island_area
                
                    