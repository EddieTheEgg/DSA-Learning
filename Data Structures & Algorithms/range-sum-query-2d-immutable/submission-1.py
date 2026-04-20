class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Create prefix matrix WITHOUT padding (same size as original)
        self.prefix = [[0] * cols for _ in range(rows)]
        
        # Build the prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                # Current cell value
                current = matrix[r][c]
                
                # Sum from above
                above = self.prefix[r - 1][c] if r > 0 else 0
                
                # Sum from left
                left = self.prefix[r][c - 1] if c > 0 else 0
                
                # Sum of overlap (top-left diagonal)
                overlap = self.prefix[r - 1][c - 1] if r > 0 and c > 0 else 0
                
                # Build cumulative sum
                self.prefix[r][c] = current + above + left - overlap

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Use +1 offset because prefix matrix is padded with 0s at index 0
        bottom_right = self.prefix[row2][col2]
        above_area = self.prefix[row1-1][col2] if row1 > 0 else 0
        left_area = self.prefix[row2][col1-1] if col1 > 0 else 0
        duplicated_area = self.prefix[row1-1][col1-1] if row1> 0 and col1> 0 else 0

        result = bottom_right - above_area - left_area + duplicated_area

        return result