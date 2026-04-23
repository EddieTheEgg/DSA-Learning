class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We need to iterate through each cell no matter what O(n)
        #We'll keep track hashset probably.

        #We prob have a 9 sets for columns
        # 9 sets for rows
        # a set of sub-boxes

        #sub boxes are trickier
        #Maybe our hashset 

        #Hashsets
        # If we're not allowed to use collections.defaultdict for some reason
        # we can check if the key exists in the row_set first. If not we create via row_set[row] = set()
        row_set = collections.defaultdict(set) # [row number : {1,2,3...}]
        col_set = collections.defaultdict(set) # col number : {1,2,3...}
        box_set = collections.defaultdict(set) #Box top left would be 0,0. Bot middle be 0,1 and so on

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                sub_box_row = row // 3
                sub_box_col = col // 3
                if board[row][col] in row_set[row] or board[row][col] in col_set[col] or board[row][col] in box_set[(sub_box_row, sub_box_col)]:
                    return False
                value = board[row][col]
                row_set[row].add(value)
                col_set[col].add(value)
                box_set[(sub_box_row,sub_box_col)].add(value)
        
        return True