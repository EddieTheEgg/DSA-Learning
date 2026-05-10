class TrieNode:
    def __init__(self):
        self.children = {} #max length of 26 character path for the chidl per letter
        self.lastLetter = None #If it is actual last letter, we store value as the whole word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #We first should build out tree, like as we iterate we
        # add our found letter to a children level but idk if
        # we should build our tree first or just iterate through

        #Step 1. First turn words list into a trie path
        trie_path = TrieNode()

        def insertWord(word : str):
            curr = trie_path
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.lastLetter = word #Set the last letter VALUE to have the word it ends with

        for word in words:
            insertWord(word)
        
        #Step 2: Backtracking through the grid and using out trie_path
        ROWS = len(board)
        COLS = len(board[0])

        valid_words = set()
        visit = set()

        def dfs(row, col, node):
            #Base case, a bad cell we need to backtrack up
            if row >= ROWS or col >= COLS or row < 0 or col < 0 or (row, col) in visit or board[row][col] not in node.children:
                return

            visit.add((row,col))
            node = node.children[board[row][col]]
            if node.lastLetter is not None:
                valid_words.add(node.lastLetter)
            
            dfs(row + 1, col, node)
            dfs(row - 1, col, node)
            dfs(row, col + 1, node)
            dfs(row, col - 1, node)

            visit.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie_path)

        return list(valid_words)