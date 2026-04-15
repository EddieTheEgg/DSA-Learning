class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         #points first row
        left = 0
        #points last row
        right = len(matrix) - 1

        # Binary search to find the correct row
        while left <= right:
            middle = left + (right - left) // 2

            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                mainMatrix = matrix[middle]
                break  #Found the correct row, exit the loop
        else:
            return False
        
        # Binary search within the found row to find the target
        miniLeft = 0
        miniRight = len(matrix[0]) - 1

        while miniLeft <= miniRight:
            miniMiddle = miniLeft + (miniRight - miniLeft) // 2

            if target < mainMatrix[miniMiddle]:
                miniRight = miniMiddle - 1
            elif target > mainMatrix[miniMiddle]:
                miniLeft = miniMiddle + 1
            else:
                return True
        
        return False