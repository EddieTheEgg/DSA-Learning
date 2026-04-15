class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #Step 1: Find where that rotton fruit is, so we can start a BFS from there

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0


        # First we go through the grid to get all fresh fruits and the specific rotten fruit for our start if it exist
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                #At each queue layer, or spread, we make all connected fresh fruits become rotten before moving onto next layer of queue, which is the next minute
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1 #-1 if there are fresh fruits but our rotten fruits could not spread or there wasn't a rotten fruit or fruits in the first place