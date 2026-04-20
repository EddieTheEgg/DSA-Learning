class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Create prefix sum matrix (add 1 extra row/col for padding)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Build the prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                # Add current cell + sum from left + sum from above - overlap
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] + 
                    self.prefix[r][c + 1] + 
                    self.prefix[r + 1][c] - 
                    self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Use +1 offset because prefix matrix is padded with 0s at index 0
        return (self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )