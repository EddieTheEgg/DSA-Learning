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
        #Keep track of distance here
        queue.append((0, 0))

        length = 1
        while queue:

            #for each queue "layer" or directional expansion, check validity
            for _ in range(len(queue)):
                        
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            length += 1

        return -1
    


        
        