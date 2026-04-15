class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        #If the first cell is a 1 or the bottom right is 1 it's blocked
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1

        # only one box, so just 1 lol
        if len(grid) == 1: 
            return 1
        
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        queue = deque()
        visits = set()
        queue.append((0,0, 1))


        length = 0
        while queue:
            r, c, dist = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))


        return -1
    


        
        